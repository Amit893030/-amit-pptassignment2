#Q1.Given a string s,
# find the first non-repeating character in it and return its index. If it does not exist, return -1.

def first_non_repeating_character(s):
    frequency = {}

    # Update frequency of each character
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Find first non-repeating character
    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i

    return -1

#Q2.Given a circular integer array `nums`of length `n`, return the maximum possible sum of a non-empty subarray of`nums`.
#A circular array means the end of the array connects to the beginning of the array. Formally, the next element of`nums[i]`is`nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.
#A subarray may only include each element of the fixed buffer`nums`at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

def max_subarray_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0

    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


def max_sum_circular_array(nums):
    max_sum_without_wrap = max_subarray_sum(nums)
    total_sum = sum(nums)
    inverted_nums = [-num for num in nums]
    max_sum_with_wrap = total_sum + max_subarray_sum(inverted_nums)

    if max_sum_with_wrap == 0:  # All elements are negative, return the maximum element
        return max(nums)

    return max(max_sum_without_wrap, max_sum_with_wrap)

#Q3.The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
#The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:
#If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.
#Otherwise, they will**leave it** and go to the queue's end.
#This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
#You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `ith` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the`jth`student in the initial queue (`j = 0` is the front of the queue). Return *the number of students that are unable to eat.

print("doubt in question 3")

#Q4.You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.
# Implement the `RecentCounter` class:
#RecentCounter()` Initializes the counter with zero recent requests.
#int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.
#It is **guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)

#Q5.There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `ith` friend brings you to the `(i+1)th` friend for `1 <= i < n`, and moving clockwise from the `nth` friend brings you to the `1st` friend.
#The rules of the game are as follows:
#1. **Start** at the `1st` friend.
#2. Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.
#3. The last friend you counted leaves the circle and loses the game.
#4. If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.
#5. Else, the last friend in the circle wins the game.
#Given the number of friends, `n`, and an integer `k`, return *the winner of the game*.

class Friend:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_winner(n, k):
    # Create the circular linked list of friends
    first = Friend(1)
    prev = first

    for i in range(2, n + 1):
        curr = Friend(i)
        prev.next = curr
        prev = curr

    prev.next = first  # Connect the last friend to the first friend

    # Simulate the game
    curr = first
    while curr.next != curr:
        for _ in range(k - 1):
            curr = curr.next

        curr.next = curr.next.next
        curr = curr.next

    return curr.value

#Q6.You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `ith` card is `deck[i]`.
#You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
#You will do the following steps repeatedly until all cards are revealed:
#1. Take the top card of the deck, reveal it, and take it out of the deck.
#2. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
#3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.
#Return an ordering of the deck that would reveal the cards in increasing order*.
#Note that the first entry in the answer is considered to be the top of the deck.

def deck_revealed_increasing(deck):
    deck.sort()  # Sort the deck in increasing order
    n = len(deck)
    result = []

    for i in range(n - 1, -1, -1):
        if result:
            result.insert(0, result.pop())
        result.insert(0, deck[i])

    return result


#Q7.Design a queue that supports `push` and `pop` operations in the front, middle, and back.
# Implement the `FrontMiddleBack` class:
#- `FrontMiddleBack()` Initializes the queue.
#- `void pushFront(int val)` Adds `val` to the **front** of the queue.
#- `void pushMiddle(int val)` Adds `val` to the **middle** of the queue.
#- `void pushBack(int val)` Adds `val` to the **back** of the queue.
#- `int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `1`.
#- `int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `1`.
#- `int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `1`.
#Notice** that when there are **two** middle position choices, the operation is performed on the **frontmost** middle position choice. For example:
#- Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
#- Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.

class FrontMiddleBack:
    def __init__(self):
        self.front = []
        self.back = []

    def pushFront(self, val):
        self.front.append(val)

    def pushMiddle(self, val):
        if len(self.front) == len(self.back) or len(self.front) > len(self.back):
            self.front.insert(len(self.front) // 2, val)
        else:
            self.back.insert(0, val)

    def pushBack(self, val):
        self.back.append(val)

    def popFront(self):
        if self.front:
            return self.front.pop()
        elif self.back:
            self.front.append(self.back.pop(0))
            return self.front.pop()
        else:
            return 1

    def popMiddle(self):
        if len(self.front) == len(self.back):
            return self.front.pop()
        else:
            return self.back.pop(0)

    def popBack(self):
        if self.back:
            return self.back.pop()
        elif self.front:
            self.back.append(self.front.pop())
            return self.back.pop(0)
        else:
            return 1


#Q8.For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are **equal** to `value`.
#Implement the **DataStream** class:
#- `DataStream(int value, int k)` Initializes the object with an empty integer stream and the two integers `value` and `k`.
#- `boolean consec(int num)` Adds `num` to the stream of integers. Returns `true` if the last `k` integers are equal to `value`, and `false` otherwise.
# If there are less than `k` integers, the condition does not hold true, so returns `false`.

from collections import deque

class DataStream:
    def __init__(self, value, k):
        self.stream = deque()
        self.value = value
        self.k = k

    def consec(self, num):
        self.stream.append(num)

        if len(self.stream) > self.k:
            self.stream.popleft()

        if len(self.stream) == self.k and all(x == self.value for x in self.stream):
            return True

        return False
