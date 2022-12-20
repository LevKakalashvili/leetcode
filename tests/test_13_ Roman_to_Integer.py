from python_.task_13_Roman_to_Integer import Solution
import pytest


@pytest.mark.parametrize("s, expected_result",
                         [
                             ("III", 3),
                             ("LVIII", 58),
                             ("MCMXCIV", 1994),
                         ]
                         )
def test_solution(s, expected_result):
    a = Solution()
    assert a.romanToInt(s=s) == expected_result

