
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics for a given set of numbers.

    Args:
        *args: Variable length argument list of numbers.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None

    Raises:
        None
    """
    args_list = list(args)
    total = 0
    values = []
    num_args = 0
    for arg in args:
        num_args += 1
        total += arg
        values.append(arg)

    if num_args == 0:
        for value in kwargs.items():
            print("ERROR")
        return

    mean = total / num_args
    
    i = 0
    while i < num_args - 1:
        j = 0
        while j < num_args - i - 1:
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
            j += 1
        i += 1

    median_index = num_args // 2
    if num_args % 2 == 0:
        median = (values[median_index - 1] + values[median_index]) / 2
    else:
        median = values[median_index]

    q1_index = num_args // 4
    q3_index = q1_index * 3
    quartile = [float(values[q1_index]), float(values[q3_index])]

    variance_total = 0
    for value in values:
        variance_total += (value - mean) ** 2
    variance = variance_total / num_args
    std_deviation = (variance ** 0.5)

    result = {"mean": mean, "median": median, "quartile": quartile,
              "std": std_deviation, "var": variance}

#    if value in result.keys():
#        print(f"{value} : {result[value]}")

    for key, value in kwargs.items():
        if value in result:
            print(f"{value} : {result[value]}")