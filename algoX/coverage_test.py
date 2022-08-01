
from dlx import DLX

from numpy import array

def validate(correct, solutions, s):
    result = []
    for k in s:
        result.append(k.ID + 1)
    print(result)

def callback(solutions, s):
    validate([2, 4, 6], solutions, s)

problem = array([[1, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 1, 0, 1, 1, 0],
                 [0, 1, 1, 0, 0, 1, 1],
                 [0, 1, 0, 0, 0, 0, 1]])

dlx = DLX.from_matrix(problem, callback)
dlx.run(True)
