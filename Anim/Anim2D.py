import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Physical.Physical2D import Physical2D

class Anim2D():
    """A class for animating a 2D movement\n
    The animation is paused if the object would pass the borders of it
    """

    def __init__(self, xlims: tuple[float, float], ylims: tuple[float, float], movement: Physical2D, interval: float = 1, grid: bool = False):
        """The constructor

        Args:
            xlims (tuple[float, float]): The limits (size) of the x axis (from .. to ..)
            ylims (tuple[float, float]): The limits (size) of the y axis (from .. to ..)
            movement (Physical2D): The physical movement to simulate
            interval (float): The interval between each update of the animation. Defaults to 1.
            grid (bool): If the graphs should have a grid. Defaults to False.
        """
        self.movement = movement
        self.xlims = xlims
        self.ylims = ylims

        self.fig, self.ax = plt.subplots()  # get the figure and axis
        self.x_axis = [] # set the x axis to be empty
        self.y_axis = [] # set the y axis to be empty
        self.ax.set_xlim(xlims)
        self.ax.set_ylim(ylims)
        self.ax.grid() if grid else None
        self.line, = self.ax.plot(self.x_axis, self.y_axis)

        self.anim = FuncAnimation(self.fig, self.animate, interval=interval)

    def animate(self, frame):
        """Is called every advance of the animation

        Args:
            frame: The current frame of the animation
        """
        x, y, t = self.movement.get_state()
        
        print(f"X coordinate: {x}", f"Y coordinate: {y}", f"Time: {t}", sep="\t")

        # Pause the animation if the object would go out of the borders of the graph
        if x < self.xlims[0] or x > self.xlims[1] or y < self.ylims[0] or y > self.ylims[1]:
            self.anim.pause()

        self.x_axis.append(x)
        self.y_axis.append(y)

        self.movement.update()

        self.line.set_data(self.x_axis, self.y_axis)

    
    def start_animation(self) -> None:
        """Starts the animation
        """
        plt.show()