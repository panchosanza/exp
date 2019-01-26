def robot_moves(ms):
    """
    There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.


    The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

    Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
    """
    moves = list(ms)
    position = [0, 0]
    for x in moves:
        if x == "U":
            position[1] += 1
        elif x == "D":
            position[1] -= 1
        elif x == "R":
            position[0] += 1
        elif x == "L":
            position[0] -= 1
    return position == [0, 0]


def test_one():
    assert robot_moves("LL") == False


def test_two():
    assert robot_moves("UD") == True
