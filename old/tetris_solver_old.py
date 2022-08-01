# from polycubes_coords import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
from polycubes_array import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
from numpy import rot90, array
import numpy as np
from shape_drawer import draw_shape

def transform_shape(polycube, face, rotation):

	if face == 1:
		# 4 rotations about axis 0
		return rotate_face(polycube, (1,2), rotation)
	elif face == 2:
		# # rotate 180 about axis 1, now shape is pointing down in axis 0
		# 4 rotations about axis 0
		return rotate_face(np.rot90(polycube, 2, axes=(0,2)), (1,2), rotation)
	elif face == 3:
		# # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
		# # 8 rotations about axis 2
		return rotate_face(np.rot90(polycube, axes=(0,2)), (0,1), rotation)
	elif face == 4:
		return rotate_face(np.rot90(polycube, -1, axes=(0,2)), (0,1), rotation)
	elif face == 5:
		# # rotate about axis 2, now shape is pointing in axis 1
		# # 8 rotations about axis 1
		return rotate_face(np.rot90(polycube, axes=(0,1)), (0,2), rotation)
	elif face == 6:
		return rotate_face(np.rot90(polycube, -1, axes=(0,1)), (0,2), rotation)

def rotate_face(polycube, axes, rotation):
	"""List the four rotations of the given 3d array in the plane spanned by the given axes."""
	for i in range(rotation):
		polycube = np.rot90(polycube, i, axes)
	return polycube

def matrix2coordinates(matrix):
    (m,color) = matrix
    coordinates = []

    for x in range(len(m)):
        for y in range(len(m[x])):
            for z in range(len(m[x][y])):
                if m[x][y][z]:
                    coordinates.append(((x,y,z),color))

    return coordinates

def coordinates2matrix(coordinates):
    polycube = np.zeros((5,5,3))

    for c in coordinates:
		((x,y,z),color) = c
		polycube[x][y][z] = 1

    return (polycube, color)

shapes = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]

faces = [1,2,3,4,5,6]
rotations = [1,2,3,4]
for shape in shapes:
	for f in faces:
		for r in rotations:
			(coordinates, color) = shape
			coordinates = transform_shape(coordinates, f, r)
			polycube = matrix2coordinates((coordinates, color))
			print(polycube)
			draw_shape([polycube])
