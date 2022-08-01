# from polycubes_coords import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
# from polycubes_array_1 import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
from numpy import rot90, array
import numpy as np
from common.shape_drawer import draw_shape

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

def matrix2coordinates(m):
	coordinates = []
	for x in range(len(m)):
		for y in range(len(m[x])):
			for z in range(len(m[x][y])):
				if m[x][y][z]:
					coordinates.append((x,y,z))
	
	return coordinates

def coordinates2matrix(coordinates):
	polycube = np.zeros((5,5,3))

	for c in coordinates:
		((x,y,z),color) = c
		polycube[x][y][z] = 1

	return (polycube, color)

def shift_down(shapes):
	for shape_name, shape in shapes.items():
		(coords_ls, color) = shape
		new_coords_ls = []
		for coords in coords_ls:
			new_coords = coords
			for i in range(4):
				if np.any([(nc[0]-1) < 0 for nc in new_coords]):
					break
				new_coords = [(nc[0]-1,nc[1],nc[2]) for nc in new_coords]
			for i in range(4):
				if np.any([(nc[1]-1) < 0 for nc in new_coords]):
					break
				new_coords = [(nc[0],nc[1]-1,nc[2]) for nc in new_coords]
			for i in range(4):
				if np.any([(nc[2]-1) < 0 for nc in new_coords]):
					break
				new_coords = [(nc[0],nc[1],nc[2]-1) for nc in new_coords]

			new_coords_ls.append(new_coords)
		shapes[shape_name] = (new_coords_ls, color)
	return shapes

def generate_transformations(shapes):
	transformed_shapes = {}
	faces = [1,2,3,4,5,6]
	rotations = [1,2,3,4]
	for shape_name, shape in shapes.items():
		coords_list = []
		for f in faces:
			for r in rotations:
				(matrix, color) = shape
				matrix = transform_shape(matrix, f, r)
				print(matrix.shape, shape_name, f, r)
				coords = matrix2coordinates(matrix)
				coords_list.append(coords)

				# draw_shape([(coords, color)])

		transformed_shapes[shape_name] = (coords_list, color)
		#UNIQUIFY
		# transformed_matrices = np.array(transformed_matrices)
		# transformed_matrices = np.repeat(transformed_matrices, 2, axis=0)
		# np.unique(transformed_matrices)
	transformed_shapes = shift_down(transformed_shapes)

	return transformed_shapes
		


def test(shapes):
	#shapes = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]

	faces = [1,2,3,4,5,6]
	rotations = [1,2,3,4]
	for shape in shapes:
		for f in faces:
			for r in rotations:
				(matrix, color) = shape
				matrix = transform_shape(matrix, f, r)
				polycube = matrix2coordinates((matrix, color))
				print(polycube)
				draw_shape([polycube])
