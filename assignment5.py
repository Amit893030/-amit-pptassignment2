#Q1.Convert 1D Array Into 2D Array
#You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n.
# You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the
# elements from original.
#The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the
# constructed 2D array, the elements from indices n to 2 * n - 1 (**inclusive**) should form the
# second row of the constructed 2D array, and so on.
#Return an m x n *2D array constructed according to the above procedure, or an empty 2D array if it is
# impossible

def construct_2d_array(original, m, n):
    if len(original) != m * n:
        return []

    array_2d = []

    for i in range(m):
        row = original[i * n: (i + 1) * n]
        array_2d.append(row)

    return array_2d
original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3

result = construct_2d_array(original, m, n)
for row in result:
    print(row)

#Q2.You have n coins and you want to build a staircase with these coins. The staircase consists of k rows
# where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#Given the integer n, return *the number of **complete rows** of the staircase you will build.

def arrange_coins(n):
    left = 1
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        coins_needed = (mid * (mid + 1)) // 2

        if coins_needed == n:
            return mid
        elif coins_needed < n:
            left = mid + 1
        else:
            right = mid - 1

    return right
n = 8

complete_rows = arrange_coins(n)
print(complete_rows)

#Q3.Given an integer array nums sorted in non-decreasing order, return an array of the squares of
# each number sorted in non-decreasing order.
def sorted_squares(nums):
    squared_nums = [num * num for num in nums]
    squared_nums.sort()
    return squared_nums
nums = [-4, -2, 0, 2, 4]

sorted_squared_nums = sorted_squares(nums)
print(sorted_squared_nums)

#Q4.Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#answer[0] is a list of all distinct integers in nums1 which are not present in num2
#answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#Note that the integers in the lists may be returned in any order.

def find_disjoint_nums(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)

    return [distinct_nums1, distinct_nums2]
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 3, 5]

result = find_disjoint_nums(nums1, nums2)
print(result)


#Q5.Given two integer arrays arr1 and arr2, and the integer d, *return the distance value between the two
# arrays*.
#the distance value is defined as the number of elements arr1[i] such that there is not any element
# arr2[j] where |arr1[i]-arr2[j]| <= d.

def distance_value(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                break
        else:
            distance += 1

    return distance
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

result = distance_value(arr1, arr2, d)
print(result)

#Q6.Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.
#You must write an algorithm that runs in O(n) time and uses only constant extra space.

def find_duplicates(nums):
    result = []

    for num in nums:
        index = abs(num)
        if nums[index] < 0:
            result.append(index)
        else:
            nums[index] = -nums[index]

    return result
nums = [4, 3, 2, 7, 8, 2, 3, 1]

duplicates = find_duplicates(nums)
print(duplicates)

#Q7.Suppose an array of length n sorted in ascending order is **rotated** between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
#[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#Given the sorted rotated array nums of **unique** elements, return *the minimum element of this array*.
#You must write an algorithm that runs in O(log n) time.

print("doubt")

#Q8.An integer array original is transformed into a doubled array changed by appending twice the
#value of every element in original, and then randomly shuffling the resulting array.
#Given an array changed, return original if changed is a doubled array. If changed is not a doubled array,
# return an empty array. The elements in original may be returned in any order.
print("doubt")
