from python_.task_27_Remove_Element import remove_element, remove_element_2
import pytest


@pytest.mark.parametrize("nums, val, expected_result",
                         [
                             ([3, 2, 2, 3], 3, 2),
                             ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
                         ]
                         )
def test_remove_element(nums, val, expected_result):
    assert remove_element(nums=nums, val=val) == expected_result


@pytest.mark.parametrize("nums, val, expected_result",
                         [
                             ([3, 2, 2, 3], 3, 2),
                             ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
                         ]
                         )
def test_remove_element_2(nums, val, expected_result):
    assert remove_element_2(nums=nums, val=val) == expected_result
