import numpy as np
import sympy as sp
import math
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
        self.dy = lambda x,y: 0.5*(y**2 - 1)
        fig = Figure(figsize=(10,10))
        super(MplWidget, self).__init__(fig)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.ann = None
        nx, ny = .3, .3
        x, y = np.arange(-5, 5, nx), np.arange(-5, 5, ny)
        X, Y = np.meshgrid(x, y)
        dy = 0.5*(Y**2 - 1)
        dx = np.ones(dy.shape)
        dyu = dy/np.sqrt(dx**2 + dy**2)
        dxu = dx/np.sqrt(dx**2 + dy**2)
        self.mouse_click = self.mpl_connect("button_press_event", self.onclick_mouse)
        self.key_click = self.mpl_connect('key_press_event', self.onclick_key)
        self.ax.quiver(X, Y, dxu, dyu, color='purple', headaxislength=30, headlength=0, pivot='mid',
        scale=4, linewidth=.2, units='xy', width=.02, headwidth=1)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        

    def euler_method(self, x, y, n):
        if self.ann != None:
            self.ann.remove()
            self.ann = None
        x_start = -5
        x_end = 5
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
            y_current = y_current - self.dy(x_current, y_current) * h
            x_current = x_current - h
            if np.isnan(y_current) == True:
                break_iteration = i
                last_x = x_plot[-1]
                last_y = y_euler[-1]
                break
        self.ax.plot(x_plot, y_euler, color='red', linewidth=2)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
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
        self.ax.plot(x_plot, y_runge, color='blue', linewidth=2)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.draw()

    def f(self, x, c):
        y = (-2/(c*math.exp(x) - 1) - 1)
        return y

    def accurate_solution(self, x_init, y_init):
        if self.ann != None:
            self.ann.remove()
            self.ann = None
        c = (-2 / ((y_init + 1) * math.exp(x_init)) + 1/math.exp(x_init))
        low = -5
        high = 5
        xs1 = []
        ys1 = []
        xs2 = []
        ys2 = []

        while low <= high:
            x = low
            y = self.f(x, c)
            if (c*math.exp(x) - 1) < 0:
                xs1.append(x)
                ys1.append(y)
                low = low + 0.02
            elif (c*math.exp(x) - 1) > 0:
                xs2.append(x)
                ys2.append(y)
                low = low + 0.02
            else:
                low = low + 0.02
                continue


        self.ax.plot(xs1, ys1, color='green', linewidth=2)
        self.ax.plot(xs2, ys2, color='green', linewidth=2)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
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
                line.remove()
                i = i + 1
            self.draw()    

class TopLevelWindow5(QtWidgets.QMainWindow):
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


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)

#     w = TopLevelWindow5()
#     w.show()

#     sys.exit(app.exec_())