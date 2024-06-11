import sys


def check_odd_or_even(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if len(sys.argv) < 2:
    exit()
elif len(sys.argv) != 2:
    print("AssertionError: incorrect number of arguments")
    exit()
try:
    number = int(sys.argv[1])
except Exception:
    print("AssertionError: argument is not an integer")
    exit()
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
