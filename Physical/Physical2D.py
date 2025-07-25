class Physical2D():
    """The interface for a generic physical object/movement\n
    These properties are required: x, y, t, time_step 
    """

    def get_state(self) -> tuple[float, float, float]:
        """Returns the the x and y position and current time position respectively

        Returns:
            tuple[float, float, float]: x, y, t (x position, y position, position in time)
        """
        pass

    def get_moment_in_time(self, t: float) -> tuple[float, float]:
        """Returns the x and y position in certain point in time

        Args:
            t (float): The point in time, which we want to observe

        Returns:
            tuple[float, float]: x, y coordinate respectively
        """
        pass

    def update(self) -> None:
        """Updates the x and y position of the object according to the time step
        """
        pass