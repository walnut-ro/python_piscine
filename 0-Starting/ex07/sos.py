import sys


def to_morse(text):
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morse = []
    for char in text.upper():
        if char in NESTED_MORSE:
            morse.append(NESTED_MORSE[char])
        else:
            raise AssertionError("Unsupported symbol: {}".format(char))
    return morse


def main():
    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 or not isinstance(
                sys.argv[1], str):
            raise AssertionError(" the arguments are bad")
        in_text = sys.argv[1]
        print(' '.join(to_morse(in_text)))
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
