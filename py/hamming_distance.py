import pytest


class Solution:

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return 2


@pytest.fixture
def solution():
    return Solution()


def test_hamming(solution):
    assert solution.hammingDistance(1, 4) == 2
