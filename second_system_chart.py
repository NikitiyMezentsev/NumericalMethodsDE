import numpy as np
import cmath
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
from sympy import symbols, Eq, Function
from sympy.solvers.ode.systems import dsolve_system


class MplWidget(FigureCanvasQTAgg):
    def __init__(self, euler_steps, runge_steps, parent=None):
        self.euler_steps = euler_steps
        self.runge_steps = runge_steps
        fig = Figure()
        super(MplWidget, self).__init__(fig)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        x = np.linspace(-2.0, 8.0, 20)
        y = np.linspace(-2.0, 2.0, 20)
        X, Y = np.meshgrid(x,y)
        t = 0
        u, v = np.zeros(X.shape), np.zeros(Y.shape)
        NI, NJ = X.shape
        for i in range(NJ):
            for j in range(NJ):
                x = X[i, j]
                y = Y[i, j]
                yprime = self.f([x, y], t)
                u[i, j] = yprime[0]
                v[i, j] = yprime[1]
        dyu = v/np.sqrt(v**2 + u**2)
        dxu = u/np.sqrt(v**2 + u**2)
        self.ax.quiver(X, Y, dxu, dyu, color='purple', headlength=3, pivot='middle',
                       scale=5, linewidth=.2, units='xy', width=.02)
        self.ax.set_xlabel("x(t)", fontsize=15)
        self.ax.set_ylabel("y(t)", fontsize=15)
        self.ax.grid()
        self.ax.set_xlim([-1, 1])
        self.ax.set_ylim([-1, 1])


        self.mouse_click = self.mpl_connect("button_press_event", self.onclick_mouse)
        self.key_click = self.mpl_connect('key_press_event', self.onclick_key)

    def euler_method(self, x_start, y_start, n_steps):
        x_arr = np.zeros(n_steps + 1)
        y_arr = np.zeros(n_steps + 1)
        t_arr = np.zeros(n_steps + 1)
        t_arr[0] = 0
        x_arr[0] = x_start
        y_arr[0] = y_start
        t_start = 0
        t_end = 30
        dt = (t_end - t_start) / n_steps
        for i in range(1, n_steps + 1):
            x = x_arr[i - 1]
            y = y_arr[i - 1]
            t = t_arr[i - 1]
            dxdt = y - x * (x*x + y*y)
            dydt = -x - y * (x*x + y*y)
            x_arr[i] = x + dxdt*dt
            y_arr[i] = y + dydt*dt
            t_arr[i] = t + dt
        self.ax.plot(x_arr, y_arr, linewidth=1.5, color='red')
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.draw()

    def runge_kutta(self, x_start, y_start, n_steps):
        t_start = 0
        t_end = 30
        x_arr_runge = np.zeros(n_steps + 1)
        y_arr_runge = np.zeros(n_steps + 1)
        t_arr_runge = np.zeros(n_steps + 1)
        t_arr_runge[0] = t_start
        x_arr_runge[0] = x_start
        y_arr_runge[0] = y_start
        dt = (t_end - t_start) / n_steps
        for i in range(1, n_steps + 1):
            x = x_arr_runge[i - 1]
            y = y_arr_runge[i - 1]
            t = t_arr_runge[i - 1]
            dxdt = y - x * (x*x + y*y)
            dydt = -x - y * (x*x + y*y)
            k0 = dt * dxdt
            l0 = dt * dydt
            
            t2 = t + dt/2
            x2 = x + k0/2
            y2 = y + l0/2
            dxdt2 = y2 - x2 * (x2*x2 + y2*y2)
            dydt2 = -x2 - y2 * (x2*x2 + y2*y2)
            k1 = dt * dxdt2
            l1 = dt * dydt2

            t3 = t + dt/2
            x3 = x + k1/2
            y3 = y + l1/2
            dxdt3 = y3 - x3 * (x3*x3 + y3*y3)
            dydt3 = -x3 - y3 * (x3*x3 + y3*y3)
            k2 = dt * dxdt3
            l2 = dt * dydt3

            t4 = t + dt
            x4 = x + k2
            y4 = y + l2
            dxdt4 = y4 - x4 * (x4*x4 + y4*y4)
            dydt4 = -x4 - y4 * (x4*x4 + y4*y4)
            k3 = dt * dxdt4
            l3 = dt * dydt4
            x_arr_runge[i] = x + (k0 + k1*2 + k2*2 + k3)/6
            y_arr_runge[i] = y + (l0 + l1*2 + l2*2 + l3)/6
        self.ax.plot(x_arr_runge, y_arr_runge, linewidth=1.5, color='blue')
        self.draw()

    def accurate_solution(self, x_start, y_start):
        t0 = 0
        t_big = 100000
        x_points = []
        y_points = []
        t_k = 0
        for t in range(t0, t_big):
            theta0 = None
            r0 = None
            rk = None
            if (x_start == y_start) and (x_start == 0):\
                r0 = rk = 0
            else:
                r0 = cmath.sqrt((x_start**2) + (y_start**2)) 
            if x_start > 0 and y_start >= 0:
                theta0 = cmath.atan(y_start/x_start)
            elif x_start > 0 and y_start < 0:
                theta0 = cmath.atan(y_start/x_start) + (2*cmath.pi)
            elif x_start < 0:
                theta0 = cmath.atan(y_start/x_start) + cmath.pi
            elif x_start == 0 and y_start > 0:
                theta0 = cmath.pi / 2
            elif x_start == 0 and y_start < 0:
                theta0 = (3 * cmath.pi) / 2
            theta_k = -t_k + theta0
            r_k = 1/(cmath.sqrt(2*t_k + (1/(r0**2))))
            x_k = r_k * cmath.cos(theta_k)
            y_k = r_k * cmath.sin(theta_k)
            x_points.append(x_k)
            y_points.append(y_k)
            t_k = t * (t_big / 1000000)
        self.ax.plot(x_points, y_points, linewidth=1.5, color='green')
        self.draw()

    def f(self, Y, t):
        x, y = Y
        first = y - x*(x*x + y*y)
        second = -x - y*(x*x + y*y)
        return [first, second]

    def onclick_mouse(self, event):
        if event.button == 1:
            self.euler_method(event.xdata, event.ydata, int(self.euler_steps))
        elif event.button == 3:
            self.runge_kutta(event.xdata, event.ydata, int(self.runge_steps))
        elif event.button == 2:
            self.accurate_solution(event.xdata, event.ydata)
        
    def onclick_key(self, event):
        if event.key == 'c':
            for line in self.ax.lines:
                    line.remove()
            self.draw()    

class TopLevelWindowSystem2(QtWidgets.QMainWindow):
    def __init__(self, euler_steps, runge_steps):
        self.euler_steps = euler_steps
        self.runge_steps = runge_steps
        super().__init__()
        self.canvas = MplWidget(self.euler_steps, self.runge_steps)
        self.canvas.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.canvas.setFocus()
        self.setCentralWidget(self.canvas)
        self.setFixedWidth(1000)
        self.setFixedHeight(1000)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = TopLevelWindowSystem2()
    w.show()

    sys.exit(app.exec_())