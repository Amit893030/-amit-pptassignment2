#Q1.Given an integer array nums of length n and an integer target, find three integers
#in nums such that the sum is closest to the target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return target

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            else:
                right -= 1

    return closestSum
