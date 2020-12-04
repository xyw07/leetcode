"""
Given a sorted array of positive integers, rearrange the array alternately
i.e first element should be maximum value, second minimum value,
third second max, fourth second min and so on.
Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}
Input: arr[] = {1, 2, 3, 4, 5, 6}
Output: arr[] = {6, 1, 5, 2, 4, 3}
"""


def main():
    # Driver code
    # Test method 1---Success
    # arr = [1, 2, 3, 4, 5, 6]
    # n = len(arr)
    # print("Original Array")
    # print(arr)
    # print("Modified Array")
    # print(rearrange(arr, n))
    # arr = [1, 2, 3, 4, 5, 6]
    # n = len(arr)
    # print("Original Array")
    # print(arr)
    # print("Modified Array")
    # print(rearrange(arr, (n-3)))
    # print(rearrange([1], 1))

    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print("Original Array")
    print(arr)
    print("Modified Array")
    print(rearrange2(arr, n))
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print("Original Array")
    print(arr)
    print("Modified Array")
    print(rearrange2(arr, (n-3)))
    print(rearrange2([1], 1))


def rearrange(arr, n):
    temp = []
    small_index = 0
    large_index = len(arr) - 1
    attemp = 0
    while (large_index >= small_index and attemp < n):
        temp.append(arr[large_index])
        large_index -= 1
        attemp += 1
        if (attemp < n):
            temp.append(arr[small_index])
            small_index += 1
            attemp += 1
    return temp


def rearrange2(arr, n):
    # Auxiliary array to hold modified array
    temp = n*[None]
 
    # Indexes of smallest and largest elements
    # from remaining array.
    small, large = 0, n-1
 
    # To indicate whether we need to copy rmaining
    # largest or remaining smallest at next position
    flag = True
 
    # Store result in temp[]
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1
 
        flag = bool(1-flag)
 
    # Copy temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]
    return arr


main()
