#Q1.Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.
#An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
print(isPowerOfTwo(4))
print(isPowerOfTwo(5))
print(isPowerOfTwo(16))
print(isPowerOfTwo(17))

#Q2.Given a number n, find the sum of the first natural numbers.
sum = (n * (n + 1)) / 2
def sumOfNaturalNumbers(n):
    return (n * (n + 1)) // 2
print(sumOfNaturalNumbers(5))  # output=15
print(sumOfNaturalNumbers(10)) # output=55
print(sumOfNaturalNumbers(20)) # output=210

#Q3.Given a positive integer, N. Find the factorial of N.
def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)
print(factorial(5))  # output=120

#Q4.Given a number N and a power P, the task is to find the exponent of this number raised to the given power,
# i.e. N^P.

def calculateExponent(N, P):
    result = N ** P
    return result
print(calculateExponent(2, 3))   # 8
print(calculateExponent(5, 2))   # 25
print(calculateExponent(10, 0))  # 1 (any number raised to the power 0 is 1)

#Q5.def findMax(arr, start, end):
    # Base case: if there is only one element in the array
    if start == end:
        return arr[start]

    # Find the midpoint of the array
    mid = (start + end) // 2

    # Recursive calls to find the maximum of the left and right halves of the array
    max_left = findMax(arr, start, mid)
    max_right = findMax(arr, mid + 1, end)

    # Compare the maximums of the left and right halves to find the overall maximum
    return max(max_left, max_right)

arr = [10, 7, 25, 18, 42, 3, 1]
max_element = findMax(arr, 0, len(arr) - 1)
print(max_element)  #output= 42


#Q6.Given first term (a), common difference (d) and a integer N of the
# Arithmetic Progression series, the task is to find Nth term of the series.

Nth_term = a + (N - 1) * d
def findNthTerm(a, d, N):
    nth_term = a + (N - 1) * d
    return nth_term
a = 3
d = 5
N = 7
nth_term = findNthTerm(a, d, N)
print(nth_term)  #output= 33


#Q7.Given a string S, the task is to write a program to print all permutations of a given string.
def permuteString(S, left, right):
    if left == right:
        print(''.join(S))
    else:
        for i in range(left, right + 1):
            # Swap characters
            S[left], S[i] = S[i], S[left]

            # Recursively generate permutations
            permuteString(S, left + 1, right)

            # Undo the swap for backtracking
            S[left], S[i] = S[i], S[left]

# Function to generate permutations of a string
def printPermutations(S):
    n = len(S)
    permuteString(list(S), 0, n - 1)

#Q8.Given an array, find a product of all array elements.
def findProduct(arr):
    product = 1
    for num in arr:
        product *= num
    return product
arr = [2, 3, 4, 5]
product = findProduct(arr)
print(product)  # output= 120




