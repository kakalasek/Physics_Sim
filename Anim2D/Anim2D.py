import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Physical2D.Physical2D import Physical2D

class Anim2D():

    def __init__(self, xlims, ylims, obj: Physical2D, interval):
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