import numpy as np
import sympy as sp
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
import mpmath
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from sympy import symbols, Eq, Function
from sympy.solvers.ode.systems import dsolve_system
from sympy.calculus.util import continuous_domain

class MplWidget(FigureCanvasQTAgg):
    def __init__(self, euler_steps, runge_steps, parent=None):
        self.euler_steps = euler_steps
        self.runge_steps = runge_steps
        self.dy = lambda x,y: np.sqrt(1 - y**2)
        fig = Figure(figsize=(10,10))
        super(MplWidget, self).__init__(fig)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ann = None
        nx, ny = .3, .3
        x, y = np.arange(-3, 3, nx), np.arange(-2, 2, ny)
        X, Y = np.meshgrid(x, y)
        dy = np.sqrt(1 - Y**2)
        dx = np.ones(dy.shape)
        dyu = dy/np.sqrt(dx**2 + dy**2)
        dxu = dx/np.sqrt(dx**2 + dy**2)
        xs = [-2, 2]
        ys = [1, 1]
        ys2 = [-1, -1]
        self.mouse_click = self.mpl_connect("button_press_event", self.onclick_mouse)
        self.key_click = self.mpl_connect('key_press_event', self.onclick_key)
        self.ax.quiver(X, Y, dxu, dyu, color='purple', headaxislength=30, headlength=0, pivot='mid',
        scale=4, linewidth=.2, units='xy', width=.02, headwidth=1)
        self.ax.plot(xs, ys, color='purple', linestyle='dashed', linewidth=3)
        self.ax.plot(xs, ys2, color='purple', linestyle='dashed', linewidth=3)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        

    def euler_method(self, x, y, n):
        if self.ann != None:
            self.ann.remove()
            self.ann = None
        x_start = -2
        x_end = 2
        x_current = x
        y_current = y
        h = float((x_end - x_start) / n) 
        x_plot = []
        y_euler = []
        break_iteration = None
        last_x = None
        last_y = None
        for i in range(1, n + 1):
            x_plot.append(x_current)
            y_euler.append(y_current)
            y_current = y_current + self.dy(x_current, y_current) * h
            x_current = x_current + h
            if np.isnan(y_current) == True:
                break_iteration = i
                last_x = x_plot[-1]
                last_y = y_euler[-1]
                break
            print(str(x_current), str(y_current))
        print(break_iteration)
        msg = "Выполнено " + str(break_iteration - 1) + " шагов из " + str(n)
        self.ann = self.ax.annotate(msg,
                    xy=(last_x,last_y), xytext=(0, 1.3), fontsize=15,
                    arrowprops=dict(facecolor='purple',
                    linewidth=1.2))
        self.ax.plot(x_plot, y_euler, color='red', linewidth=2)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.draw()

    def runge_kutta(self, x, y, n):
        if self.ann != None:
            self.ann.remove()
            self.ann = None
        x_start = -2
        x_end = 2
        x_current = x
        y_current = y
        h = float((x_end - x_start) / n) 
        x_plot = []
        y_runge = []
        break_iteration = None
        last_x = None
        last_y = None
        for i in range(1, n + 1):
            x_plot.append(x_current)
            y_runge.append(y_current)
            k1 = self.dy(x_current, y_current)
            k2 = self.dy(x_current + h / 2, y_current + (h * k1) / 2)
            k3 = self.dy(x_current + h / 2, y_current + (h * k2) / 2)
            k4 = self.dy(x_current + h, y_current + h * k3)
            y_delta = (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
            if np.isnan(y_current) == True:
                break_iteration = i
                last_x = x_plot[-2]
                last_y = y_runge[-2]
                break
            y_current = y_current + y_delta
            x_current = x_current + h
        msg = "Выполнено " + str(break_iteration - 1) + " шагов из " + str(n)
        self.ann = self.ax.annotate(msg,
                    xy=(last_x,last_y), xytext=(0, 1.3), fontsize=15,
                    arrowprops=dict(facecolor='purple',
                    linewidth=1.2))
        self.ax.plot(x_plot, y_runge, color='blue', linewidth=2)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.draw()


    def accurate_solution(self, x_init, y_init):
        if self.ann != None:
            self.ann.remove()
            self.ann = None
        x = sp.Symbol('x')
        f = sp.Function("f")(x)
        diff_eq = sp.Eq(f.diff(), sp.sqrt(1 - f**2))
        sol = sp.dsolve(diff_eq, f)
        c = mpmath.asin(y_init) - x_init
        f_n = sp.Function("f_n")(x)
        f_n = sp.sin(x + c)
        domain = continuous_domain(f_n, x, sp.S.Reals)
        ans = mpmath.sin(x_init + c)
        x_points = []
        y_points = []
        if (ans < 1) and (ans > -1):
            z = 0
            while z < 30:
                x_points.append(float(mpmath.asin(-1) - c) - z)
                y_points.append(-1)
                z = z + 1
            while (ans > -1) and (x_init >= mpmath.asin(-1) - c):
                x_points.append(float(x_init))
                y_points.append(float(ans))
                x_init = x_init - 0.05
                ans = float(mpmath.sin(x_init + c))
            while (ans < 1) and (x_init <= mpmath.asin(1) - c):
                x_points.append(float(x_init))
                y_points.append(float(ans))
                x_init = x_init + 0.05
                ans = float(mpmath.sin(x_init + c))
            k = 0
            while k < 30:
                x_points.append(float(mpmath.asin(1) - c) + k)
                y_points.append(1)
                k = k + 1
            
        x_points = sorted(x_points)
        y_points = sorted(y_points)
        self.ax.plot(x_points, y_points, color='green', linewidth=2)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.draw()


    def onclick_mouse(self, event):
        if event.button == 1:
            self.euler_method(event.xdata, event.ydata, int(self.euler_steps))
        elif event.button == 3:
            self.runge_kutta(event.xdata, event.ydata, int(self.runge_steps))
        elif event.button == 2:
            self.accurate_solution(event.xdata, event.ydata)
        
    def onclick_key(self, event):
        if event.key == 'c':
            i = 0
            for line in self.ax.lines:
                if (i != 0) and (i != 1):
                    line.remove()
                i = i + 1
            self.draw()    

class TopLevelWindow4(QtWidgets.QMainWindow):
    def __init__(self, euler_steps, runge_steps):
        self.euler_steps = euler_steps
        self.runge_steps = runge_steps
        super().__init__()
        self.canvas = MplWidget(euler_steps, runge_steps)
        self.canvas.euler_steps = self.euler_steps
        self.canvas.runge_steps = self.runge_steps
        self.canvas.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.canvas.setFocus()
        self.setCentralWidget(self.canvas)
        self.setFixedWidth(1000)
        self.setFixedHeight(1000)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = TopLevelWindow4()
    w.show()

    sys.exit(app.exec_())