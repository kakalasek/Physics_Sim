class Physical2D():
    """_The interface for a generic physical object/movement\n
    These properties are required: x, y, t, time_step _
    """

    def get_state(self) -> tuple[float, float, float]:
        """_Returns the the x and y position and current time position respectively_

        Returns:
            tuple[float, float, float]: x, y, t (x position, y position, position in time)
        """
        pass

    def get_moment_in_time(self, t: float) -> tuple[float, float]:
        """_Returns the x and y position in certain point in time_

        Args:
            t (float): _The point in time, which we want to observe_

        Returns:
            tuple[float, float]: _x, y coordinate respectively_
        """
        pass

    def update(self) -> None:
        """_Updates the x and y position of the object according to the time step_
        """
        pass