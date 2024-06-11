import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (matrix) from the given start index to end index.

    Parameters:
    family (list): A 2D list (matrix) to be sliced.
    start (int): The starting index for the slice.
    end (int): The ending index for the slice.

    Returns:
    list: A new 2D list (matrix) that is a slice of the original.
    
    Raises:
    AssertionError: If the input is not a list and two integers, or if 
                    the items in the list have different sizes.

    Example:
    slice_me([[1, 2], [3, 4], [5, 6]], 1, 3)
    [[3, 4], [5, 6]]
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("The list have item with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return ""
