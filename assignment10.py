#Q1.Given an integer`n`, return`true`if it is a power of three. Otherwise, return`false`*.
#An integer`n`is a power of three, if there exists an integer`x`such that`n == 3x`.
import math

def isPowerOfThree(n):
    if n <= 0:
        return False

    x = math.log(n, 3)
    return abs(x - round(x)) < 1e-10
print(isPowerOfThree(9))   # True
print(isPowerOfThree(27))  # True
print(isPowerOfThree(45))  # False
print(isPowerOfThree(0))   # False


#Q2.You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:
#Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
#Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
#Keep repeating the steps again, alternating left to right and right to left, until a single number remains

def applyAlgorithm(arr):
    while len(arr) > 1:
        # Remove every other number from left to right
        arr = arr[::2]

        if len(arr) == 1:
            break

        # Remove every other number from right to left
        arr = arr[-2::-2]

    return arr[0] if arr else None
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = applyAlgorithm(arr)
print(result)  # 5


#Q3.Given a set represented as a string,
# write a recursive code to print all subsets of it. The subsets can be printed in any order.

def printSubsets(set_str, subset=""):
    if len(set_str) == 0:
        print(subset)
    else:
        # Include the first character in the current subset
        printSubsets(set_str[1:], subset + set_str[0])

        # Exclude the first character from the current subset
        printSubsets(set_str[1:], subset)
set_str = "abc"
printSubsets(set_str)


#Q4.Given a string calculate length of the string using recursion.
def calculateLength(string):
    # Base case: an empty string has length 0
    if string == "":
        return 0

    # Recursive case: remove the first character and calculate the length of the remaining string
    return 1 + calculateLength(string[1:])
string = "Hello, World!"
length = calculateLength(string)
print(length)  # 13


#Q5.We are given a string S, we need to find count of all contiguous substrings starting and ending with
# same character.
def countSubstrings(S):
    count = 0
    n = len(S)

    for i in range(n):
        for j in range(i, n):
            if S[i] == S[j]:
                count += 1

    return count
S = "ababa"
count = countSubstrings(S)

print(count)  # 9


#Q7.Given a stringstr, the task is to print all the permutations ofstr. Apermutationis an arrangement of all or
# part of a set of objects, with regard to the order of the arrangement. For instance, the
# words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word

def permuteString(str, left, right):
    if left == right:
        print(''.join(str))
    else:
        for i in range(left, right + 1):
            # Swap characters
            str[left], str[i] = str[i], str[left]

            # Recursively generate permutations
            permuteString(str, left + 1, right)

            # Undo the swap for backtracking
            str[left], str[i] = str[i], str[left]

# Function to print permutations of a string
def printPermutations(str):
    n = len(str)
    permuteString(list(str), 0, n - 1)

str = "abc"
printPermutations(str)


#Q8.Given a string, count total number of consonants in it. A consonant is an English alphabet character
# that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.
def countConsonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in string:
        if char in consonants:
            count += 1

    return count
string = "Hello, World!"
count = countConsonants(string)
print(count)  # 8

