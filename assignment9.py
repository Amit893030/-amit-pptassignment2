#Q1.Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings
# equal.
def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])

    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + ord(s1[i-1]),
                    dp[i][j-1] + ord(s2[j-1]),
                    dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1])
                )

    return dp[m][n]

#Q2.Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid.
def isValid(s):
    stack = []
    star_count = 0

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '*':
                stack.pop()
                star_count += 1
            else:
                return False

    while stack:
        if stack[-1] == '(':
            if star_count == 0:
                return False
            star_count -= 1
        stack.pop()

    return True

#Q3.Given two strings word1 and word2, return the minimum number of steps required to make
# word1 and word2 the same.
def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i

    for j in range(1, n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + 1
                )

    return dp[m][n]

#Q4.You need to construct a binary tree from a string consisting of parenthesis and integers.
#The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
# The integer represents the root's value and a pair of parenthesis contains a child binary tree with the
# same structure.
#You always start to construct the left child node of the parent first if it exists.

print('doubt in question 4')

#Q5.Given an array of characters chars, compress it using the following algorithm:
#Begin with an empty string s. For each group of consecutive repeating characters in chars:
#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be stored in the input
# character array chars. Note that group lengths that are 10 or longer will be split into multiple
# characters in chars.
#After you are done modifying the input array, return the new length of the array.
#You must write an algorithm that uses only constant extra space

def compress(chars):
    write = 0
    read = 0
    count = 1

    while read < len(chars):
        if read < len(chars) - 1 and chars[read] == chars[read + 1]:
            count += 1
        else:
            chars[write] = chars[read]
            write += 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
                count = 1
        read += 1

    return write

#Q6.Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def findAnagrams(s, p):
    result = []
    p_counts = [0] * 26
    s_counts = [0] * 26
    window_counts = [0] * 26

    for char in p:
        p_counts[ord(char) - ord('a')] += 1

    left, right = 0, 0

    while right < len(s):
        window_counts[ord(s[right]) - ord('a')] += 1

        if right - left == len(p):
            window_counts[ord(s[left]) - ord('a')] -= 1
            left += 1

        if window_counts == p_counts:
            result.append(left)

        right += 1

    return result

#Q7.Given an encoded string, return its decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
#You may assume that the input string is always valid; there are no extra white spaces, square brackets
# are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
#The test cases are generated so that the length of the output will never exceed 105.

def decodeString(s):
    stack = []

    for char in s:
        if char == ']':
            decoded_str = ''
            while stack and stack[-1] != '[':
                decoded_str = stack.pop() + decoded_str

            stack.pop()  # Remove '['
            repeat_count = int(stack.pop())
            decoded_str *= repeat_count
            stack.append(decoded_str)
        else:
            stack.append(char)

    return ''.join(stack)



