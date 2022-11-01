# https://leetcode.com/problems/remove-element/

def remove_element(nums: list[int], val) -> int:
    k = 0
    for index in range(len(nums)):
        if nums[index] == val:
            nums[index] = 999
        else:
            k += 1
    nums.sort()
    return k


def remove_element_2(nums: list[int], val) -> int:
    k = len(nums)
    for cnt in range(nums.count(val)):
        nums.remove(val)
        k -= 1
    return k
