# Print a string in reverse order.
# You can easily solve this problem iteratively, i.e. looping through the string starting from its last character. But how about solving it recursively?

def print_reverse(str):
    if len(str) == 0:
        return
    else:
        string = str[1:]
        last = str[0]
        print_reverse(string)
        print(last, end="")


def main():
    """
    test
    """
    string1 = "abcde"
    print_reverse(string1)
    print()


main()
