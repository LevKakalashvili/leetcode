# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Сложность O(n)
# Сложность по памяти O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    # {nums_value: nums_index}
    dict_nums = {}
    for index in range(len(nums)):
        if (target - nums[index]) in dict_nums:
            return [dict_nums[target - nums[index]], index]
        else:
            dict_nums[nums[index]] = index
