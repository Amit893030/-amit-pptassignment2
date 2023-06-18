
#question
def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# Example:
num = 16
result = mySqrt(num)
print(result)
#output is 4
