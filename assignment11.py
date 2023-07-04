#Q!.Given a non-negative integer`x`, return the square root of`x`rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#You must not use any built-in exponent function or operator.
def sqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

# Example usage
print(sqrt(16))  # Output= 4
print(sqrt(8))   # Output=2


#Q2.A peak element is an element that is strictly greater than its neighbors.
#Given a 0-indexed integer array`nums`, find a peak element, and return its index. If the array contains
# multiple peaks, return the index to any of the peaks.
#You may imagine that nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be
# strictly greater than a neighbor that is outside the array.
#You must write an algorithm that runs in`O(log n)`time.

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example
nums = [1, 2, 3, 1]
print(findPeakElement(nums))  # Output: 2

nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))  # Output: 5

#Q3.Given an array`nums`containing`n`distinct numbers in the range[0, n]
# return the only number in the range that is missing from the array.
def missingNumber(nums):
    missing = len(nums)  # Initialize missing as the last index

    for i, num in enumerate(nums):
        missing ^= i ^ num  # XOR the current index and element

    return missing

# Example
nums = [3, 0, 1]
print(missingNumber(nums))  # Output: 2

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))  # Output: 8


#Q4.Given an array of integers`nums`containing`n + 1`integers where each integer is in the range`[1, n]`inclusive.
#There is only one repeated number in`nums`, return this repeated number.
#You must solve the problem without modifying the array`nums`and uses only constant extra space.
def findDuplicate(nums):
    # Find the intersection point of the two runners
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the entrance to the cycle
    ptr1 = nums[0]
    ptr2 = tortoise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Example usage
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2

nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))  # Output: 3


#Q5.Given two integer arrays nums1`and`nums2`, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]
print(intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))  # Output: [9, 4]

#Q6.Suppose an array of length`n`sorted in ascending order is rotated between`1`
# and`n`times. For example, the array nums = [0,1,2,4,5,6,7]`might become:
#`[4,5,6,7,0,1,2]`if it was rotated`4`times.
#`[0,1,2,4,5,6,7]`if it was rotated`7`times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]`1 time results in the array
# `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.
#Given the sorted rotated array nums`of unique elements, return the minimum element of this array.
#You must write an algorithm that runs in O(log n) time.`

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example
nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0

nums = [3, 4, 5, 1, 2]
print(findMin(nums))  # Output: 1




