from numpy import rot90, array
from shape_drawer import draw_shape
def rotations24(polycube):
    """List all 24 rotations of the given 3d array"""
    def rotations4(polycube, axes):
        """List the four rotations of the given 3d array in the plane spanned by the given axes."""
        for i in range(4):
             yield rot90(polycube, i, axes)

    # imagine shape is pointing in axis 0 (up)
    # 4 rotations about axis 0
    yield from rotations4(polycube, (1,2))

    # rotate 180 about axis 1, now shape is pointing down in axis 0
    # 4 rotations about axis 0
    yield from rotations4(rot90(polycube, 2, axes=(0,2)), (1,2))

    # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
    # 8 rotations about axis 2
    yield from rotations4(rot90(polycube, axes=(0,2)), (0,1))
    yield from rotations4(rot90(polycube, -1, axes=(0,2)), (0,1))

    # rotate about axis 2, now shape is pointing in axis 1
    # 8 rotations about axis 1
    yield from rotations4(rot90(polycube, axes=(0,1)), (0,2))
    yield from rotations4(rot90(polycube, -1, axes=(0,1)), (0,2))

polycube = array([[[1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [1, 0, 0],
        [1, 0, 0]],

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

assert len(set(str(x) for x in rotations24(polycube))) == 24