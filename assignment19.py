#Q1.You are given an array of `k` linked-lists`lists`, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.*

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged = mergeTwoLists(l1, l2)
            new_lists.append(merged)
        lists = new_lists

    return lists[0]

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy.next

#Q2.Given an integer array nums, return an
# integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

def countSmaller(nums):
    counts = [0] * len(nums)

    def mergeSort(start, end):
        if start >= end:
            return []

        mid = (start + end) // 2
        left = mergeSort(start, mid)
        right = mergeSort(mid + 1, end)

        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                counts[left[i][1]] += end - mid
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    mergeSort(0, len(nums) - 1)
    return counts

#Q3Given an array of integers`nums`, sort the array in ascending order and return it.
#You must solve the problem without using any built-in functions in `O(nlog(n))`time complexity and with the smallest space complexity possible.
def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sortArray(nums):
    return mergeSort(nums)

#Q4.Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
# The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

def pushZerosToEnd(nums):
    left = 0
    right = 0

    while left < len(nums):
        if nums[left] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
        left += 1

    return nums

#Q5.Given an array of positive and negative numbers**, arrange them in an alternate fashion such that every positive number is followed by a negative and vice-versa maintaining the **order of appearance**. The number of positive and negative numbers need not be equal. If there are more positive numbers they appear
# at the end of the array. If there are more negative numbers, they too appear at the end of the array.

def arrangeNumbers(nums):
    positive = 0
    negative = 0

    # Partition the array into positive and negative numbers
    while positive < len(nums):
        if nums[positive] >= 0:
            positive += 1
        else:
            nums[positive], nums[negative] = nums[negative], nums[positive]
            positive += 1
            negative += 1

    # Move remaining positive numbers to the end
    start_positive = positive
    while positive < len(nums):
        nums[positive], nums[negative] = nums[negative], nums[positive]
        positive += 1
        negative += 2

    # Move remaining negative numbers to the end
    start_negative = negative
    while negative < len(nums):
        nums[negative], nums[start_positive] = nums[start_positive], nums[negative]
        negative += 1
        start_positive += 2

    return nums


#Q6.Given two sorted arrays, the task is to merge them in a sorted manner.

def mergeSortedArrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


#Q7.Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order

def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = set()

    for num in nums2:
        if num in set1:
            intersection.add(num)

    return list(intersection)

#Q8.Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the
# result must appear as many times as it shows in both arrays and you may return the result in any order.

from collections import defaultdict

def intersection(nums1, nums2):
    frequencyMap = defaultdict(int)

    for num in nums1:
        frequencyMap[num] += 1

    intersection = []

    for num in nums2:
        if frequencyMap[num] > 0:
            intersection.append(num)
            frequencyMap[num] -= 1

    return intersection
