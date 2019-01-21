def flip_invert_image(iarr):
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
    
    for x in iarr:
        for y range(len(y // 2)):
            opposite_index = y - (y + 1)
            current_opposite = x[opposite_index]
            y = int(not(x))
    return iarr


def test_flip_image():
    assert flip_invert_image([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]


def test_flip_image2():
    assert flip_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
