from python_.task_169_majority_element import solution_169_1
import pytest


@pytest.mark.parametrize("nums, expected_result",
                         [
                             ([3, 2, 3], 3),
                             ([2, 2, 1, 1, 1, 2, 2], 2),
                             ([2, 1, 1, 1, 4, 4, 4, 4, 4], 4)
                         ]
                         )
def test_solution_169_1(nums, expected_result):
    assert solution_169_1(nums=nums) == expected_result
