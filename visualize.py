import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import cos, sin, pi

class CannonBall():
    g = 9.81
    
    def __init__(self, v0, y0, x0=0, theta=0, t0=0, time_step=0.01):
        """
        v0 - velocity at the beggining\n
        y0 - height at the beggining\n
        x0 - where the ball is placed on the x-axis\n
        theta - angle between ground and the ball\n
        t0 - from which point of throw you want to see the trajectory\n
        time_step - by how far in each update the ball should move\n
        """
        self.v0 = v0

        self.theta = theta

        self.x0 = x0
        self.y0 = y0

        self.t = t0
        self.time_step = time_step
        
        self.x, self.y = self.get_moment_in_time(self.t)

    def update(self):
        """
        Updates the balls position in time
        """
        self.t += self.time_step

        self.x = self.x0 + self.v0*self.t*cos(self.theta)
        self.y = self.y0 + self.v0*self.t*sin(self.theta) - 0.5 * self.g * (self.t**2)

    def get_moment_in_time(self, t):
        x = self.x0 + self.v0*t*cos(self.theta)
        y = self.y0 + self.v0*t*sin(self.theta) - 0.5 * self.g * (t**2)
        return x, y

    def get_state(self):
        """
        Returns the current state of the ball, e. i. x, y and time postion
        """
        return self.x, self.y, self.t

class Anim():

    def __init__(self, xlims, ylims, obj, interval):
        """
        xlims - tuple from which point to which point you want the x axis\n
        ylims - tuple from which point to which point you want the y axis\n
        obj - the object which will be travelling on the graph\n
        interval - interval between each advance of the animation\n
        """
        self.obj = obj
        self.xlims = xlims
        self.ylims = ylims

        self.fig, self.ax = plt.subplots()  # get the figure and axis
        self.x_axis = [] # set the x axis to be empty
        self.y_axis = [] # set the y axis to be empty
        self.ax.set_xlim(xlims)
        self.ax.set_ylim(ylims)
        self.line, = self.ax.plot(self.x_axis, self.y_axis)

        self.anim = FuncAnimation(self.fig, self.animate, init_func=self.ii, interval=interval)

    def ii(self):
        self.line.set_data(self.x_axis, self.y_axis)

    def animate(self, frame):
        """
        Gets called every advance of the animation\n
        frame - the current frame of the animation\n
        """
        x, y, t = self.obj.get_state()
        
        print(f"X coordinate: {x}", f"Y coordinate: {y}", f"Time: {t}", sep="\t")

        # Pause the animation if the object would go out of the borders of the graph
        if x < self.xlims[0] or x > self.xlims[1] or y < self.ylims[0] or y > self.ylims[1]:
            self.anim.pause()

        self.x_axis.append(x)
        self.y_axis.append(y)

        self.obj.update()

        self.line.set_data(self.x_axis, self.y_axis)

    
    def start_animation(self):
        plt.show()



cannonBall = CannonBall(10, 0, theta=pi/8, x0=0)
anim = Anim((0, 30), (0, 12), cannonBall, 1)
anim.start_animation()