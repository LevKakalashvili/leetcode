from python_.task_1_Two_Sum import twoSum
import pytest


@pytest.mark.parametrize("nums, target, expected_result",
                         [
                             ([3, 2, 3], 6, [0, 2]),
                             ([2,7,11,15], 9, [0, 1]),
                             ([3,2,4], 6, [1, 2]),
                             ([3,3], 6, [0, 1])
                         ]
                         )
def test_twoSum(nums, target, expected_result):
    assert twoSum(nums=nums, target=target) == expected_result
