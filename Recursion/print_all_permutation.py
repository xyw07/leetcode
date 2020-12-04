"""
Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
"""

def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print("hit the base")
        print(toString(a))
    else:
        print("deep + 1")
        for i in range(l,r+1): # this is important
            print("i =", i, "l =", l)
            print("a[i] =", a[i], "a[l] =", a[l])
            a[l], a[i] = a[i], a[l]
            print(a)
            permute(a, l+1, r)
            print("i =", i, "l =", l)
            print("a[i] =", a[i], "a[l] =", a[l])
            a[l], a[i] = a[i], a[l] # backtrack
            print("back track:", a)
            # since it manipulate list, it should restore the list

# Driver program to test the above function
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 