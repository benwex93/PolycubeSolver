from numpy import rot90, array
import numpy as np
from shape_drawer import draw_shape
def rotations24(polycube):
    shape_rotations = []
    rotations4(polycube, (1,2), shape_rotations)
    rotations4(rot90(polycube, 2, axes=(0,2)), (1,2), shape_rotations)
    rotations4(rot90(polycube, axes=(0,2)), (0,1), shape_rotations)
    rotations4(rot90(polycube, -1, axes=(0,2)), (0,1), shape_rotations)
    rotations4(rot90(polycube, axes=(0,1)), (0,2), shape_rotations)
    rotations4(rot90(polycube, -1, axes=(0,1)), (0,2), shape_rotations)
    return shape_rotations
def rotations4(polycube, axes, shape_rotations):
    """List all 24 rotations of the given 3d array"""
    """List the four rotations of the given 3d array in the plane spanned by the given axes."""
    for i in range(4):
        shape = rot90(polycube, i, axes)
        shape_rotations.append(shape)
        # shape = matrix2coordinates(shape)
        # draw_shape([shape])

    # imagine shape is pointing in axis 0 (up)

    # 4 rotations about axis 0
    # yield from rotations4(polycube, (1,2))

    # # rotate 180 about axis 1, now shape is pointing down in axis 0
    # # 4 rotations about axis 0
    # yield from rotations4(rot90(polycube, 2, axes=(0,2)), (1,2))

    # # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
    # # 8 rotations about axis 2
    # yield from rotations4(rot90(polycube, axes=(0,2)), (0,1))
    # yield from rotations4(rot90(polycube, -1, axes=(0,2)), (0,1))

    # # rotate about axis 2, now shape is pointing in axis 1
    # # 8 rotations about axis 1
    # yield from rotations4(rot90(polycube, axes=(0,1)), (0,2))
    # yield from rotations4(rot90(polycube, -1, axes=(0,1)), (0,2))

polycube = array(
      [[[0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]],

       [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]])
def matrix2coordinates(matrix):
    coordinates = []

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            for z in range(len(matrix[x][y])):
                if matrix[x][y][z]:
                    coordinates.append(((x,y,z),'r'))
    return coordinates

# shape = matrix2coordinates(polycube)
# draw_shape([shape])

# polycube = rotations4(polycube, (1,2))
# polycube = rotations4(polycube, (1,2))

# draw_shape([shape])
sh = np.unique(rotations24(polycube),axis=0)
import pdb
pdb.set_trace()
# filter(lambda x: numpy.linalg.det(x) > 0, sh)
# numpy.linalg.det(sh)

# assert np.unique(rotations24(polycube),axis=1).shape[0] == 24
print(np.unique(rotations24(polycube),axis=0).shape[0])
# rotations24(polycube)