#Q1.Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

#Q2.Given an array `nums` with `n` objects colored red, white, or blue, sort them [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers `0`,`1`, and`2`to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

#Q3.You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#Suppose you have`n`versions`[1, 2, ..., n]`and you want to find out the first bad one, which causes all the following ones to be bad.
#You are given an API`bool isBadVersion(version)`which returns whether`version`is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

#Q4.Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.
#You must write an algorithm that runs in linear time and uses linear extra space

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element and calculate the number of digits
    max_num = max(nums)
    num_digits = len(str(max_num))

    # Radix sort
    for d in range(num_digits):
        buckets = [[] for _ in range(10)]
        for num in nums:
            digit = (num // 10**d) % 10
            buckets[digit].append(num)
        nums = [num for bucket in buckets for num in bucket]

    # Calculate the maximum difference between two successive elements
    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i-1])

    return max_diff

#Q5.Given an integer array`nums`, return`true`if any value appears at least twice in the array,
# and return`false`if every element is distinct.
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


#Q6.There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.
#Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    count = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:
            count += 1
            end = points[i][1]
        else:
            end = min(end, points[i][1])

    return count

#Q7.Given an integer array nums, return the length of the longest strictly increasing
def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


#Q8.Given an array of`n`integers`nums`, a 132 pattern is a subsequence of three integers `nums[i]`,`nums[j]`and nums[k]`such that i < j < k` and `nums[i] < nums[k] < nums[j]`.
#Return `true`if there is a 132 pattern in `nums`, otherwise, return `false`.

def find132pattern(nums):
    stack = []
    s3 = float('-inf')

    for num in reversed(nums):
        if num < s3:
            return True
        while stack and stack[-1] < num:
            s3 = max(s3, stack.pop())
        stack.append(num)

    return False
