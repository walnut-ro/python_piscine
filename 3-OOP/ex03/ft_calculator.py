class calculator:
    """
    A class representing a calculator.

    Attributes:
    - vector: A list of numbers representing the vector.

    Methods:
    - __init__(self, vector): Initializes the calculator object with a vector.
    - __add__(self, object): Adds a number to each element in the vector.
    - __mul__(self, object): Multiplies each element in the vector by a number.
    - __sub__(self, object): Subtracts a number from each element in the vector.
    - __truediv__(self, object): Divides each element in the vector by a number.
    """

    def __init__(self, vector):
        """
        Initializes the calculator object with a vector.

        Parameters:
        - vector: A list of numbers representing the vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adds a number to each element in the vector.

        Parameters:
        - object: A number to be added to each element in the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """
        Multiplies each element in the vector by a number.

        Parameters:
        - object: A number to multiply each element in the vector by.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        """
        Subtracts a number from each element in the vector.

        Parameters:
        - object: A number to be subtracted from each element in the vector.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        """
        Divides each element in the vector by a number.

        Parameters:
        - object: A number to divide each element in the vector by.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not supported.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)