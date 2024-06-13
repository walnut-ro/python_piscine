from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    The King class represents a king in the game of thrones.
    It inherits from the Baratheon and Lannister classes.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new instance of the King class.

        Args:
            first_name (str): The first name of the king.
            is_alive (bool, optional): Indicates if the king is alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Sets the color of the king's eyes.

        Args:
            color (str): The color of the eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Sets the color of the king's hairs.

        Args:
            color (str): The color of the hairs.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Returns the color of the king's eyes.

        Returns:
            str: The color of the eyes.
        """
        return self.eyes

    def get_hairs(self):
        """
        Returns the color of the king's hairs.

        Returns:
            str: The color of the hairs.
        """
        return self.hairs