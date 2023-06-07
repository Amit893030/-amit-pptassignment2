#Q1.Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order
# of characters. No two characters may map to the same character, but a character may map to itself.

def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for s_char, t_char in zip(s, t):
        if s_char in s_map:
            if s_map[s_char] != t_char:
                return False
        else:
            s_map[s_char] = t_char

        if t_char in t_map:
            if t_map[t_char] != s_char:
                return False
        else:
            t_map[t_char] = s_char

    return True
print(isomorphic_strings("egg", "add"))  # True
print(isomorphic_strings("foo", "bar"))  # False
print(isomorphic_strings("paper", "title"))  # True
print(isomorphic_strings("abb", "aba"))  # False


#Q2.Given a string num which represents an integer, return true if num is a strobogrammatic number.
#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)

def is_strobogrammatic(num):
    mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in mapping:
            return False
        if mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True
print(is_strobogrammatic("69"))  # True
print(is_strobogrammatic("88"))  # True
print(is_strobogrammatic("818"))  # True
print(is_strobogrammatic("123"))  # False

#Q3.Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and*
# num2 as a string.
#You must solve the problem without using any built-in library for handling large integers
# (such as BigInteger). You must also not convert the inputs to integers directly.

def addStrings(num1, num2):
    result = ""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        digit_sum = digit1 + digit2 + carry
        result += str(digit_sum % 10)
        carry = digit_sum // 10

        i -= 1
        j -= 1

    if carry > 0:
        result += str(carry)

    result = result[::-1]
    return result
print(addStrings("123", "456"))  # "579"
print(addStrings("999", "1"))  # "1000"
print(addStrings("0", "0"))  # "0"
print(addStrings("99", "99"))  # "198"


#Q4.Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
print(reverseWords("Hello World"))
print(reverseWords("The sky is blue"))
print(reverseWords("Python is fun"))


#Q5.Given a string s and an integer k, reverse the first k characters for every 2k characters counting
# from the start of the string.If there are fewer than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters, then reverse
#the first k characters and leave the other as original.

def reverseStr(s, k):
    chars = list(s)
    i = 0
    while i < len(chars):
        if len(chars) - i >= 2 * k:
            chars[i:i + k] = chars[i:i + k][::-1]
            i += 2 * k
        else:
            chars[i:] = chars[i:][::-1]
            break
    return ''.join(chars)
print(reverseStr("abcdefg", 2))
print(reverseStr("abcdefgh", 3))
print(reverseStr("abcdef", 4))


#Q6.Given two strings s and goal, return true if and only if s can become goal after some number of
# shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.

def can_shift(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)
s = "abcde"
goal = "cdeab"

s + s = "abcdeabcde"

#Q7.Given two strings s and t, return true *if they are equal when both are typed into empty text editors
#  '#' means a backspace character.
#Note that after backspacing an empty text, the text will continue empty.

def process_string(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)


def apply_backspaces(s, t):
    processed_s = process_string(s)
    processed_t = process_string(t)
    return processed_s == processed_t
print(apply_backspaces("ab#c", "ad#c"))
print(apply_backspaces("ab##", "c#d#"))
print(apply_backspaces("a##c", "#a#c"))
print(apply_backspaces("a#c", "b"))

#Q8.You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

print('doubt in question 8')

