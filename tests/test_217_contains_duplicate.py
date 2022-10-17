from python_.task_217_contains_duplicate import solution_217_1
import pytest


@pytest.mark.parametrize("nums, expected_result",
                         [
                             ([1,2,3,1], True),
                             ([1,2,3,4], False),
                             ([1,1,1,3,3,4,3,2,4,2], True)
                         ]
                         )
def test_solution_217_1(nums, expected_result):
    assert solution_217_1(nums=nums) == expected_result
