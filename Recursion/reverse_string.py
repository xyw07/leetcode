"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    last_index = len(s) - 1
    first_index = 0
    while (last_index >= first_index):
        temp = s[last_index]
        s[last_index] = s[first_index]
        s[first_index] = temp
        last_index -= 1
        first_index += 1
    return s


# why ot gives me Nonetpye error? how to let python know that I want to return a list?
def reverseString2(s):
    if len(s) == 0:
        return []
    else:
        s_remain = s[1:]
        last = s[0]
        return reverseString2(s_remain).append(last)


def main():
    s = ["h","e","l","l","o"]
    print(reverseString2(s))

main()
