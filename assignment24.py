#Q1.Roman numerals are represented by seven different symbols:`I`,V`,`X`,`L`,`C`,`D`and`M`.


#SymbolValueI             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000


#For example,`2`is written as`II`in Roman numeral, just two ones added together.`12`is written as`XII`, which is simply`X + II`. The number`27`is written as`XXVII`, which is`XX + V + II`.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not`IIII`. Instead, the number four is written as`IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

#`I`can be placed before`V`(5) and`X`(10) to make 4 and 9.
# `X`can be placed before`L`(50) and`C`(100) to make 40 and 90.
# `C`can be placed before`D`(500) and`M`(1000) to make 400 and 900.

def integerToRoman(num):
    # Create two lists to store the Roman numeral symbols and their corresponding values
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Initialize an empty string to store the Roman numeral representation
    roman = ""

    # Iterate through the symbols and values lists
    for i in range(len(symbols)):
        # Repeat the current symbol while the value is less than or equal to the number
        while num >= values[i]:
            roman += symbols[i]
            num -= values[i]

    return roman
# Provide an integer
num = 27

# Convert the integer to Roman numeral representation
roman = integerToRoman(num)

# Print the Roman numeral representation
print("Roman numeral representation:", roman)


#Q2.Given a strings, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    # Create a dictionary to store the last occurrence index of each character
    char_map = {}

    # Initialize variables for the start and end of the sliding window
    start = 0
    max_length = 0

    # Iterate through the string
    for end in range(len(s)):
        # Check if the current character is already in the dictionary
        if s[end] in char_map:
            # Move the start of the sliding window to the next index after the last occurrence
            start = max(start, char_map[s[end]] + 1)

        # Update the last occurrence index of the current character
        char_map[s[end]] = end

        # Update the maximum length of the substring
        max_length = max(max_length, end - start + 1)

    return max_length
# Provide a string
s = "abcabcbb"

# Find the length of the longest substring without repeating characters
length = lengthOfLongestSubstring(s)

# Print the length of the longest substring
print("Length of the longest substring without repeating characters:", length)


#Q3.Given an array`nums`of size`n`, return the majority element.
#The majority element is the element that appears more than`⌊n / 2⌋`times. You may assume that
# the majority element always exists in the array.

def majorityElement(nums):
    count = 0
    candidate = None

    # Find the potential majority element
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
# Provide an array
nums = [2, 2, 1, 1, 1, 2, 2]

# Find the majority element in the array
majority = majorityElement(nums)

# Print the majority element
print("Majority element:", majority)


#Q4.Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

def groupAnagrams(strs):
    # Create a hashmap to store the sorted version of each string as the key
    # and a list of anagrams as the value
    anagram_map = {}

    # Iterate through each string in the array
    for string in strs:
        # Sort the string and use it as the key in the hashmap
        sorted_string = "".join(sorted(string))

        # Add the string to the list of anagrams corresponding to the sorted key
        if sorted_string in anagram_map:
            anagram_map[sorted_string].append(string)
        else:
            anagram_map[sorted_string] = [string]

    # Return the values of the hashmap as the grouped anagrams
    return list(anagram_map.values())
# Provide an array of strings
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Group the anagrams together
anagram_groups = groupAnagrams(strs)

# Print the grouped anagrams
for group in anagram_groups:
    print(group)
['eat', 'tea', 'ate']
['tan', 'nat']
['bat']


#Q5.An ugly number is a positive integer whose prime factors are limited to`2`,`3`, and`5`.
#Given an integer`n`, return the`nth'ugly number.

def nthUglyNumber(n):
    # Initialize an array to store the ugly numbers
    ugly_numbers = [1]

    # Initialize pointers for each factor
    pointer_2 = pointer_3 = pointer_5 = 0

    # Initialize variables for the next ugly number and its factors
    next_ugly = 1
    next_2 = 2
    next_3 = 3
    next_5 = 5

    # Generate the ugly numbers up to the given n
    for _ in range(1, n):
        # Calculate the next ugly number as the minimum of the factors
        next_ugly = min(next_2, next_3, next_5)

        # Add the next ugly number to the array
        ugly_numbers.append(next_ugly)

        # Update the factors based on the next ugly number
        if next_ugly == next_2:
            pointer_2 += 1
            next_2 = ugly_numbers[pointer_2] * 2
        if next_ugly == next_3:
            pointer_3 += 1
            next_3 = ugly_numbers[pointer_3] * 3
        if next_ugly == next_5:
            pointer_5 += 1
            next_5 = ugly_numbers[pointer_5] * 5

    return ugly_numbers[-1]
# Provide an integer n
n = 10

# Find the nth ugly number
nth_ugly = nthUglyNumber(n)

# Print the nth ugly number
print("The", n, "th ugly number is:", nth_ugly)


#Q6.Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.
#Return the answer sorted by  the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

import heapq
from collections import Counter

def topKFrequent(words, k):
    # Create a counter to count the frequency of each word
    word_count = Counter(words)

    # Create a priority queue to store the top k frequent words
    pq = []

    # Iterate through the counter items
    for word, count in word_count.items():
        # Push a tuple of negative count and lexicographical order into the priority queue
        heapq.heappush(pq, (-count, word))

    # Extract the top k frequent words from the priority queue
    top_k = []
    for _ in range(k):
        count, word = heapq.heappop(pq)
        top_k.append(word)

    return top_k

# Provide an array of strings and an integer k
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

# Find the k most frequent strings
top_k_frequent = topKFrequent(words, k)

# Print the k most frequent strings
print("The", k, "most frequent strings are:")
for word in top_k_frequent:
    print(word)

#The 2 most frequent strings are:
#i
#love


#Q7.You are given an array of integers`nums`, there is a sliding window of size`k`which is moving from the
# very left of the array to the very right. You can only see the`k`numbers in the window.
# Each time the sliding window moves right by one position.
#Return the max sliding window.

from collections import deque

def maxSlidingWindow(nums, k):
    # Create a deque to store the indices of elements in the current window
    window = deque()

    # Initialize the result list to store the maximum elements in each window
    result = []

    # Iterate through the array
    for i in range(len(nums)):
        # Remove indices of elements that are no longer in the current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove indices of elements that are smaller than the current element
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add the index of the current element to the window
        window.append(i)

        # If the current window is of size k or larger, add the maximum element to the result list
        if i >= k - 1:
            result.append(nums[window[0]])

    return result
# Provide an array of integers and the window size
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# Find the maximum sliding window
maximums = maxSlidingWindow(nums, k)

# Print the maximum sliding window
print("The maximum sliding window is:", maximums)


#Q8.Given a sorted integer array `arr`, two integers `k` and `x`, return the `k`closest integers to `x`in the
# array. The result should also be sorted in ascending order.
#An integer `a`is closer to `x` than an integer `b`if:
#`|a - x| < |b - x|`, or
#`|a - x| == |b - x|` and`a < b`

def findClosestElements(arr, k, x):
    # Initialize two pointers for the left and right boundaries of the window
    left = 0
    right = len(arr) - k

    # Perform a binary search to find the starting index of the k closest elements
    while left < right:
        mid = left + (right - left) // 2

        # Check if the right end of the window is closer to x than the left end
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    # Return the k closest elements starting from the left index
    return arr[left:left + k]
# Provide a sorted array, an integer k, and an integer x
arr = [1, 2, 3, 4, 5]
k = 4
x = 3

# Find the k closest elements to x in the array
closest_elements = findClosestElements(arr, k, x)

# Print the k closest elements
print("The", k, "closest elements to", x, "are:", closest_elements)
