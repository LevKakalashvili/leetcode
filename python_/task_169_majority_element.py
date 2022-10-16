# 169. Majority Element
# Share
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
from collections import Counter


# Временная сложность O(n)
# Сложность поп памяти O(n)
def solution_169(nums: list) -> int:
    return Counter(nums).most_common(1)[0][0]


# Самое классное решение на мой взгляд
# Временная сложность O(n)
# Сложность поп памяти O(1)
def solution_169_1(nums):
    nums.sort()
    return nums[len(nums) // 2]
