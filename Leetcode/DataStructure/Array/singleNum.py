# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        xor = 0
        for n in nums:
            print('xor ^ n =', bin(xor), '^', bin(n), '=', xor, '^', n)
            xor = xor ^ n
            print('xor:', xor)
        return xor

    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n's unique element) -> not constant extra space.
        """
        n_cnt = Counter(nums)
        for n in n_cnt:
            if n_cnt[n]==1:
                return n

class Xor:
    def xor_example(a, b):
        print(f"{a} ^ {b} = {a^b} (Binary: {bin(a)} ^ {bin(b)} = {bin(a^b)})")

    def xor_swap(a, b):
        print(f"초기값: a = {a}, b = {b}")
        a = a ^ b
        print('1st change a:', a)
        b = a ^ b
        print('2nd change b:', b)
        a = a ^ b
        print(f"교환후: a = {a}, b = {b}")

    def toggle_bit(number, position):
        """Toggle a specific of bit."""
        mask = 1 << position
        result = number ^ mask
        print(f"Input: {bin(number)}")
        print(f"Mask: {bin(mask)}")
        print(f"Toggle Result: {bin(result)}")
        return result

# Xor.xor_example(1, 2)
# Xor.xor_example(5, 3)
# Xor.xor_example(7, 8)

# Xor.xor_swap(1, 2)
# Xor.xor_swap(5, 3)
# Xor.xor_swap(10, 20)

Xor.toggle_bit(0b1010, 1)