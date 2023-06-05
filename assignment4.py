#Q1.Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a
# sorted array of only the integers that appeared in all three arrays.

def find_common_elements(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0

    # Iterate until any array reaches its end
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If the current element is common to all three arrays
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # If the current element is smaller, move to the next element in the array with the smallest value
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 5, 7, 9]
arr3 = [1, 4, 5, 8, 10]

common_elements = find_common_elements(arr1, arr2, arr3)
print(common_elements)

#Q2.Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 *where:
#answer[0] is a list of all distinct integers in nums1 which are not present in nums2
#answer[1] is a list of all **distinct integers in nums2 which are not present in nums1.

def find_missing_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    distinct_nums1 = [num for num in set1 if num not in set2]
    distinct_nums2 = [num for num in set2 if num not in set1]

    return [distinct_nums1, distinct_nums2]
nums1 = [1, 2, 2, 3, 4, 5]
nums2 = [2, 3, 6, 7]

missing_elements = find_missing_elements(nums1, nums2)
print(missing_elements)


#Q3.Given a 2D integer array matrix, return the transpose of matrix.
#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's
# row and column indices.

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with flipped dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate over the original matrix and assign values to the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = transpose(matrix)
for row in transposed:
    print(row)


#Q4.Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    # Sum the minimum elements in each pair
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum
nums = [1, 4, 3, 2]

maximized_sum = array_pair_sum(nums)
print(maximized_sum)

#Q5.You have n coins and you want to build a staircase with these coins. The staircase consists of k
# rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.
#Given the integer n, return *the number of **complete rows** of the staircase you will build*.

def arrange_coins(n):
    complete_rows = 0
    row_coins = 1

    while n >= row_coins:
        n -= row_coins
        row_coins += 1
        complete_rows += 1

    return complete_rows

n = 8

complete_rows = arrange_coins(n)
print(complete_rows)


#Q6.Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
# number sorted in non-decreasing order.

def sorted_squares(nums):
    squared_nums = [num * num for num in nums]
    squared_nums.sort()
    return squared_nums
nums = [-4, -2, 0, 2, 4]

sorted_squared_nums = sorted_squares(nums)
print(sorted_squared_nums)

#Q7.You are given an m x n matrix M initialized with all 0's and an array of operations ops,
# where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
#Count and return *the number of maximum integers in the matrix after performing all the operations*

def max_count(m, n, ops):
    if not ops:
        return m * n

    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)

    return min_a * min_b
m = 3
n = 4
ops = [[2, 2], [3, 3]]

max_integers = max_count(m, n, ops)
print(max_integers)

#Q8.Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

def rearrange_array(nums):
    n = len(nums) // 2
    rearranged = []

    for i in range(n):
        rearranged.append(nums[i])
        rearranged.append(nums[i + n])

    return rearranged

nums = [1, 2, 3, 4, 5, 6]

rearranged_nums = rearrange_array(nums)
print(rearranged_nums)

