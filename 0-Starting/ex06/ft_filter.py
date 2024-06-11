def ft_filter(function, iterable):
    """
    My your own ft_filter, it is the behave like the original built-in function
    filter.__doc__
    """
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
