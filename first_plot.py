import numpy as np
import sympy as sp
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from sympy import symbols, Eq, Function
from sympy.solvers.ode.systems import dsolve_system
from sympy.calculus.util import continuous_domain



# class Test1(QtGui.QMain)



class MplWidget(FigureCanvasQTAgg):
    def __init__(self, euler_steps, runge_steps, parent=None):
        self.euler_steps = euler_steps
        self.runge_steps = runge_steps
        self.dy = lambda x,y: -x / y
        fig = Figure(figsize=(10,10))
        super(MplWidget, self).__init__(fig)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        x, y = np.arange(-10, 10, 0.6), np.arange(-10, 10, 0.6)
        X, Y = np.meshgrid(x, y)
        dy = -X/Y
        dx = np.ones(dy.shape)
        dyu = dy/np.sqrt(dx**2 + dy**2)
        dxu = dx/np.sqrt(dx**2 + dy**2)
        circle = Circle((0,0), 10, linewidth=2, edgecolor = 'black', alpha = 0.3, facecolor="none")
        self.ax.add_patch(circle)
        self.ann = self.ax.annotate("Click inside the grey circle!",
                    xy=(-6,8), xytext=(-10.5,10.1), fontsize=15,
                    arrowprops=dict(facecolor='purple',
                    linewidth=1.5))
        self.ax.quiver(X, Y, dxu, dyu, color='purple', headaxislength=30, headlength=0, pivot='mid',
        scale=4, linewidth=.2, units='xy', width=.05, headwidth=1)
        self.ax.add_patch(circle)
        self.ax.grid()
        self.mouse_click = self.mpl_connect("button_press_event", self.onclick_mouse)
        self.key_click = self.mpl_connect('key_press_event', self.onclick_key)

    def euler_method(self, x, y, n):
        x_start = -10
        x_end = 10
        x_current = x
        y_current = y
        h = float((x_end - x_start) / n) 
        x_plot = []
        y_euler = []
        for i in range(1, n + 1):
            x_plot.append(x_current)
            y_euler.append(y_current)
            y_current = y_current + self.dy(x_current, y_current) * h
            x_current = x_current + h
        print(x_plot)
        print(y_euler)
        self.ax.plot(x_plot, y_euler, color='red', linewidth=3)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.draw()

    def runge_kutta(self, x, y, n):
        x_start = -10
        x_end = 10
        h = float((x_end - x_start) / n) 
        x_plot = []
        y_runge = []
        for i in range(1, n + 1):
            x_plot.append(x)
            y_runge.append(y)
            k1 = self.dy(x, y)
            k2 = self.dy(x + h / 2, y + (h * k1) / 2)
            k3 = self.dy(x + h / 2, y + (h * k2) / 2)
            k4 = self.dy(x + h, y + h * k3)
            y_delta = (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
            y = y + y_delta
            x = x + h
        self.ax.plot(x_plot, y_runge, color='blue', linewidth=3)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.draw()

    def accurate_solution(self, x_init, y_init):
        x_start = -10
        x_end = 10
        x = sp.Symbol('x')
        f = sp.Function("f")(x)
        diff_eq = sp.Eq(f.diff(), -x/f)
        sol = sp.dsolve(diff_eq, f)
        initial_condition = {f.subs(x, x_init): y_init}
        ipv = sp.dsolve(diff_eq, ics=initial_condition)
        domain = continuous_domain(ipv, x, sp.S.Reals)
        ends = str(domain)[9:-1]
        ends = ends.split(", ")
        ends = [round(float(end), 1) for end in ends]
        points = list(np.arange(-10, 10, 0.02))
        points_included = [i for i in points if domain.contains(i)]
        y_points = [float(ipv.rhs.subs(x, i)) for i in points_included]
        points_included = [ends[0]] + points_included + [ends[1]]
        y_points = [0] + y_points + [0]
        self.ax.plot(points_included, y_points, color='green', linewidth=3)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.draw()


    def onclick_mouse(self, event):
        if (event.button == 1) and (event.xdata ** 2 + event.ydata ** 2 <= 100):
            self.euler_method(event.xdata, event.ydata, int(self.euler_steps))
        elif (event.button == 3) and (event.xdata ** 2 + event.ydata ** 2 <= 100):
            self.runge_kutta(event.xdata, event.ydata, int(self.runge_steps))
        elif (event.button == 2) and (event.xdata ** 2 + event.ydata ** 2 <= 100):
            self.accurate_solution(event.xdata, event.ydata)
        
    def onclick_key(self, event):
        if event.key == 'c':
            for line in self.ax.lines:
                    line.remove()
            self.draw()    

class TopLevelWindow3(QtWidgets.QMainWindow):
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

    w = TopLevelWindow3()
    w.show()

    sys.exit(app.exec_())