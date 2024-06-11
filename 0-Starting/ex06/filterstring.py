import sys
from ft_filter import ft_filter


def main():
    """
    Filter words from a given text based on length.

    Expects exactly two command-line arguments:
    1. A string of text.
    2. An integer specifying the minimum word length.

    Filters and prints words longer than the specified length.

    Example:
    python script_name.py "This is a sample text" 3
    Output: ['This', 'sample', 'text']
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad.")
        text = sys.argv[1]
        num = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(num, int):
            raise AssertionError("Invalid argument types.")

        f_words = \
            list(ft_filter(lambda word: len(word) > num, text.split()))

        print(f_words)
    except AssertionError or ValueError:
        print("AssertionError:", "the arguments are bad.")


if __name__ == "__main__":
    main()
