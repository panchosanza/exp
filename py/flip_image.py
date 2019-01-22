class Solution:

    def flipAndInvertImage(self, A):
        """
        Flip and invert the items in the matrix, as if it were an image.

        First, you must invert the array in place, then flip the bits and such.
        normal:
        1 1 0
        1 0 1
        0 0 0

        inverted:
        0 1 1
        1 0 1
        0 0 0

        return:
        1 0 0
        0 1 0
        1 1 1
        """

        for x in A:
            for y in range(len(x) // 2):
                index_offset = -(y + 1)
                current = int(not(x[y]))
                current_opposite = int(not(x[index_offset]))
                x[y] = current_opposite
                x[index_offset] = current
            if not (len(x) % 2 == 0):
                middle_index = (len(x) // 2)
                x[middle_index] = int(not(x[middle_index]))
        return A


def test_flip_image():
    assert Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]


def test_flip_image2():
    assert Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
