
from S1E9 import Character


class Baratheon(Character):
    """
    A class representing a Baratheon character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Indicates if the character is alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Sets the character's is_alive attribute to False, indicating that the character has died.
        """
        self.is_alive = False

    def __str__(self):
        """
        Returns a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """
        Returns a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')>"

class Lannister(Character):
    """
    A class representing a Lannister character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive or not. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Set the character's is_alive attribute to False, indicating that the character has died.
        """
        self.is_alive = False
    
    def __str__(self):
        """
        Returns a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Returns a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Create a new instance of the Lannister class.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): Whether the character is alive or not.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
