from src.widget import *
import pytest


@pytest.mark.parametrize(
    "words, result",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        ([" ", "madam", "racecar", "noon", "level", " "], [" ", "madam", "racecar", "noon", "level", " "]),
        ([], []),
    ],
)
def test_get_similar(words, result):
    assert get_similar(words) == result


@pytest.mark.parametrize("nums, result", [([2, 3, 5, 7, 11], 77),
                                          ([-5, -7, -9, -13], 117),
                                          ([1, 2], 2),
                                          ([4], 0)])
def test_get_max_multiply(nums, result):
    assert get_max_multiply(nums) == result
