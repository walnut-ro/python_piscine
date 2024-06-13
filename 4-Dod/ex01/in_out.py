def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.

    Parameters:
    x (int | float): The number to be squared.

    Returns:
    int | float: The square of the input number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate the power of a number.

    Args:
        x (int | float): The base number.

    Returns:
        int | float: The result of raising x to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    This function takes in a number `x` and a function `function` as parameters.
    It returns an inner function that performs the following operations:
    1. Calls the `function` with the input `x` and stores the result.
    2. Updates the value of `x` with the result.
    3. Increments a counter variable `count` by 1.
    4. Returns the updated value of `x`.
    """
    count = 0
    
    def inner() -> float:
        """
        This inner function performs the following operations:
        1. Calls the `function` with the input `x` and stores the result.
        2. Updates the value of `x` with the result.
        3. Increments the counter variable `count` by 1.
        4. Returns the updated value of `x`.
        """
        nonlocal x
        result = function(x)
        x = result
        nonlocal count
        count += 1
        return x
    return inner