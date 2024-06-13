class calculator:
    """
    This class represents a calculator that performs various vector operations.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        dot_product = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts one vector from another element-wise and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")