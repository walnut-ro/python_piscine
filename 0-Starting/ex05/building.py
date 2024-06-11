import sys


def explore_text(text):
    """
    Analyzes a given text and prints the count of various character types.

    Parameters:
    text (str): The text to be analyzed.

    This function calculates and prints the following:
    - Total number of characters in the text.
    - Number of uppercase letters.
    - Number of lowercase letters.
    - Number of punctuation marks.
    - Number of spaces.
    - Number of digits.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    total_symbols = len(text)
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punct_count = sum(1 for char in text if char in punctuation)
    space = sum(1 for char in text if char.isspace())
    digit = sum(1 for char in text if char.isdigit())

    print(f"The text contains {total_symbols} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """
    Main function to handle input and initiate text analysis.

    This function handles the following:
    - If no command-line arguments are provided,
    it prompts the user to input text.
    - If one command-line argument is provided,
    it uses that as the text to analyze.
    - If more than one command-line argument is provided,
    it raises an AssertionError.

    After handling input, it calls the explore_text function
      to analyze the provided text.
    """
    try:
        if len(sys.argv) < 2:
            s = input("What is the text to count?\n")
            s += "\n"
        elif len(sys.argv) == 2:
            s = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        explore_text(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
