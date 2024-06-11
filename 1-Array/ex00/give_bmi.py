def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI for each corresponding pair of weight and height.

    Parameters:
    weights (list of int/float): List of weights in kilograms.
    heights (list of int/float): List of heights in meters.

    Returns:
    list of float: List of calculated BMI values.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Lists must have the same length.")
        bmis = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise TypeError(
                    "Lists must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Lists values must be positive.")
            bmis.append(w / (h ** 2))
        return bmis
    except Exception as error:
        print("Error:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determines if BMI values are above a specified limit.

    Parameters:
    bmi (list[int | float]): A list of BMI values, which can be either integers or floats.
    limit (int): The threshold limit to compare the BMI values against.

    Returns:
    list[bool]: A list of boolean values where each element corresponds to whether
                the corresponding BMI value in the input list is greater than the limit.

    Raises:
    TypeError: If 'limit' is not an integer or if any value in 'bmi' is not an integer or float.
    Exception: For any other unexpected errors.

    Example:
    apply_limit([22.5, 27.0, 31.5], 25)
    [False, True, True]
    """
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be int.")
        bmi_above = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI values must be integers or floats.")
            bmi_above.append(value > limit)
        return bmi_above
    except Exception as error:
        print("Error: " + error)
        return []
    