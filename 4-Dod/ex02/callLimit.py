def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the function can be called.

    Returns:
        function: The decorated function.

    """

    count = 0

    def callLimiter(function):
        """
        Inner decorator function that limits the number of times the function can be called.

        Args:
            function (function): The function to be decorated.

        Returns:
            function: The decorated function.

        """

        def limit_function(*args, **kwds):
            """
            Wrapper function that checks the call count and calls the original function.

            Args:
                *args: Variable length argument list.
                **kwds: Arbitrary keyword arguments.

            Returns:
                The result of the original function.

            Raises:
                AssertionError: If the function is called more times than the specified limit.

            """

            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)

        return limit_function

    return callLimiter