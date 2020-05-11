import numpy as np

#functions checking that the number in a particular cell (position i,j in the grid 9x9) is not in conflict with other number
#WARNING: 0 are counted as empty cells and not numbers

#returns "true" if the number currently in position i,j (=sol[i,j]) does not appear somewhere else in the sub-square 3x3
def check_square(i,j,sol):
    #line index of the square
    line=3 * (i // 3)
    #column index of the square
    col=3 * (j // 3)
    for k in range(3):
        for l in range(3):
            if (line+k)!=i or (col+l)!=j:
                if sol[i,j]==sol[(line+k),(col+l)]  and sol[i,j]!=0:
                    return False
    return True

#returns "true" if the number currently in position i,j (=sol[i,j]) does not appear somewhere else on the line i
def check_line(i,j,sol):
    for k in range(9):
        if k!=j and sol[i,j]==sol[i,k] and sol[i,j]!=0:
            return False
    return True

#returns "true" if the number currently in position i,j (=sol[i,j]) does not appear somewhere else on the column j
def check_column(i,j,sol):
    for k in range(9):
        if k!=i and sol[i,j]==sol[k,j]  and sol[i,j]!=0:
            return False
    return True       