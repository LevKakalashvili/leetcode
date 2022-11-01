from python_.task_26_Remove_Duplicates_from_Sorted_Array import removeDuplicates
import pytest


@pytest.mark.parametrize("nums, expected_result",
                         [
                             ([-1,0,0,0,0,3,3], 3),
                             ([1,1,2], 2),
                             ([0,0,1,1,1,2,2,3,3,4], 5)
                         ]
                         )
def test_removeDuplicates(nums, expected_result):
    assert removeDuplicates(nums=nums) == expected_result