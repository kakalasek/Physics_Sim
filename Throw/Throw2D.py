from math import cos, sin
from Physical.Physical2D import Physical2D

class Throw2D(Physical2D):
    """_Represents a throw in 2D not considering the air resistance_
    """
    g: float = 9.81 # Gravitational constant
    
    def __init__(self, v0: float, y0: float, x0: float = 0, theta: float = 0, t0: float = 0, time_step: float = 0.01):
        """The construtor

        Args:
            v0 (float): The initial velocity
            y0 (float): The initial height
            x0 (float, optional): The initial x position. Defaults to 0.
            theta (float, optional): The angle of the throw in radians. Defaults to 0.
            t0 (float, optional): The time from which you want to observer the throw. Defaults to 0.
            time_step (float, optional): The time step of the throw. Smaller time step means more precise results but slower calculation. Defaults to 0.01.
        """
        self.v0 = v0

        self.theta = theta

        self.x0 = x0
        self.y0 = y0

        self.t = t0
        self.time_step = time_step
        
        self.x, self.y = self.get_moment_in_time(self.t)

    def update(self) -> None:
        """Updates the x and y coordinate by one time step
        """
        self.t += self.time_step

        self.x = self.x0 + self.v0*self.t*cos(self.theta)
        self.y = self.y0 + self.v0*self.t*sin(self.theta) - 0.5 * self.g * (self.t**2)

    def get_moment_in_time(self, t: float) -> tuple[float, float]:
        """Returns the x and y position at a specified point of time

        Args:
            t (float): The point of time which you want to observe

        Returns:
            tuple[float, float]: x and y position respectively
        """
        x = self.x0 + self.v0*t*cos(self.theta)
        y = self.y0 + self.v0*t*sin(self.theta) - 0.5 * self.g * (t**2)
        return x, y

    def get_state(self) -> tuple[float, float, float]:
        """Returns the current x and y coordinate and point of time

        Returns:
            tuple[float, float, float]: x coordinate, y coordinate and point in time respectively
        """
        return self.x, self.y, self.t