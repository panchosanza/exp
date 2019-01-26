class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        max_num = len(S)
        nums = []
        for x in range(max_num + 1):
            if S[x] == "I":
                pass
            elif S[x] == "D":
                pass
        return S


def test_string_match_one():
    assert Solution().diStringMatch("IDID") == [0, 4, 1, 3, 2]


def test_string_match_two():
    assert Solution().diStringMatch("III") == [0, 1, 2, 3]


def test_string_match_three():
    assert Solution().diStringMatch("DDI") == [3, 2, 0, 1]
