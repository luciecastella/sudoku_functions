import numpy as np
from functions import check_square
from functions import check_line
from functions import check_column

# WARNING: 0 are counted as empty cells and not numbers


def test_check_square():
    # wrong: first (top-left) 3x3 square has two "6" the other squares have no problems
    grid1 = np.array([
        [5, 3, 6, 0, 7, 0, 0,0,0],
        [6, 0, 0, 1, 9, 5, 0,0,0],
        [0, 9, 8, 0, 0, 0, 0,6,0],
        [8, 0, 0, 0, 6, 0, 0,0,3],
        [4, 0, 0, 8, 0, 3, 0,0,1],
        [7, 0, 0, 0, 2, 0, 0,0,6],
        [0, 6, 0, 0, 0, 0, 2,8,0],
        [0, 0, 0, 4, 1, 9, 0,0,5],
        [0, 0, 0, 0, 8, 0, 0,7,9]])

    assert check_square(1, 0, grid1) == False
    assert check_square(8, 8, grid1) == True


def test_check_line():
    # wrong: last line (line 8) has two "8". The other lines have no problems
    grid2 = np.array([
        [5, 3, 0, 0, 7, 0, 0,0,0],
        [6, 0, 0, 1, 9, 5, 0,0,0],
        [0, 9, 8, 0, 0, 0, 0,6,0],
        [8, 0, 0, 0, 6, 0, 0,0,3],
        [4, 0, 0, 8, 0, 3, 0,0,1],
        [7, 0, 0, 0, 2, 0, 0,0,6],
        [0, 6, 0, 0, 0, 0, 2,8,0],
        [0, 0, 0, 4, 1, 9, 0,0,5],
        [0, 8, 0, 0, 8, 0, 0,7,9]])

    # last line: the number in position 8,1 is "8" and is also somewhere else in the line:
    assert check_line(8, 1, grid2) == False

    # on the same line, "9" (value at 8,8) is nowhere else:
    assert check_line(8, 8, grid2) == True

    # no problem with 5 on the first line = line 0
    assert check_line(0, 0, grid2) == True


def test_check_column():
    # wrong: last column (column 8) has two "3". The other columns have no problems
    grid3 = np.array([
        [5, 3, 0, 0, 7, 0, 0,0,0],
        [6, 0, 0, 1, 9, 5, 0,0,3],
        [0, 9, 8, 0, 0, 0, 0,6,0],
        [8, 0, 0, 0, 6, 0, 0,0,3],
        [4, 0, 0, 8, 0, 3, 0,0,1],
        [7, 0, 0, 0, 2, 0, 0,0,6],
        [0, 6, 0, 0, 0, 0, 2,8,0],
        [0, 0, 0, 4, 1, 9, 0,0,5],
        [0, 0, 0, 0, 8, 0, 0,7,9]])

    assert check_column(1, 8, grid3) == False

    assert check_line(0, 4, grid3) == False
