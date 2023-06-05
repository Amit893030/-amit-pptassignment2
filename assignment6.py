#Q1.A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a
# string s of length n where:
#s[i] == 'I' if perm[i] < perm[i + 1], and
#s[i] == 'D' if perm[i] > perm[i + 1].
#Given a string s, reconstruct the permutation perm and return it. If there are multiple valid
# permutations perm, return any of them.

print('doubt in question 1')

#Q2.You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.
#You must write a solution in O(log(m * n)) time complexity.

def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] < target:
            left = mid + 1
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            return True

    return False
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

result = search_matrix(matrix, target)
print(result)


#Q3.Given an array of integers arr, return *true if and only if it is a valid mountain array*.
#Recall that arr is a mountain array if and only if:
#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def valid_mountain_array(arr):
    n = len(arr)
    i = 0

    if n < 3:
        return False

    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1
arr = [0, 3, 2, 1]

result = valid_mountain_array(arr)
print(result)

#Q4.Given a binary array nums, return *the maximum length of a contiguous subarray with
# an equal number of* 0 and 1.
print('doubt in question no.4')


#Q5.The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all
# 0 <= i < a.length (0-indexed).
#For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
#Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed
# to **rearrange** the **order** of the elements in nums1.

def minProductSum(nums1, nums2):
    nums1.sort()  # Sort nums1 in non-decreasing order
    nums2.sort()  # Sort nums2 in non-decreasing order

    left, right = 0, len(nums1) - 1
    minProductSum = 0

    while left <= right:
        minProductSum += nums1[left] * nums2[left]
        left += 1
        minProductSum += nums1[right] * nums2[right]
        right -= 1

    return minProductSum

#Q6.An integer array original is transformed into a doubled array changed by appending **twice the
# value of every element in original, and then randomly shuffling the resulting array.
#Given an array changed, return original if changed is a doubled array. If changed is not a
# doubled array, return an empty array. The elements in* original *may be returned in any order.

from typing import List

def findOriginalArray(changed: List[int]) -> List[int]:
    elements = set()
    original = []

    for num in changed:
        elements.add(num)

    for num in changed:
        if num / 2 not in elements:
            return []
        elements.remove(num / 2)

    return list(elements)

#Q7.Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

print('doubt in question7')

#Q8.Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2
#of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

print("doubt in question 8")