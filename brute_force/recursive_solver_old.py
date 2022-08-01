# from polycubes_array import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12

from common.shape_transformer import coordinates2matrix, matrix2coordinates, transform_shape

from common.shape_drawer import draw_shape

def add(shape, cube_open_vertices, origins_list):

	(Ox,Oy,Oz) = origins_list
	used_coords = []

	for (coords, color) in shape:
		(x,y,z) = coords

		x += Ox
		y += Oy
		z += Oz

		if x >= len(cube_open_vertices[1]) or y >= len(cube_open_vertices[0]) or z >= len(cube_open_vertices) or \
				x < 0 or y < 0 or z < 0 or not cube_open_vertices[x][y][z]:
			#invalid placement
			return False, None

		# used_coords.append((x,y,z))
		used_coords.append(((x,y,z), color))

	return True, used_coords

tried = set()
faces = [1,2,3,4,5,6]
rotations = [1,2,3,4]


trial = 0
def run(origins, cube_open_vertices, unused_shapes, shapes_dict):
	global trial
	print('trial: ', trial)
	print(origins.keys())
	trial+=1
	if unused_shapes is None:
		print('yay')
		print(origins)
		exit()

	for x in range(-len(cube_open_vertices[1]) - 1, len(cube_open_vertices[1])):
		for y in range(-len(cube_open_vertices[0]) - 1, len(cube_open_vertices[0])):
			for z in range(-len(cube_open_vertices) - 1, len(cube_open_vertices)):
				for shape_name in unused_shapes:
					(matrix, color) = shapes_dict[shape_name]
					for f in faces:
						for r in rotations:
							transformed_matrix = transform_shape(matrix, f, r)
							polycube = matrix2coordinates((transformed_matrix, color))
							valid_placement, used_coords = add(polycube, cube_open_vertices, (x,y,z))

							if not valid_placement:
								continue

							origins[shape_name] = used_coords
							if str(origins) in tried:
								origins.pop(shape_name)
								continue

							#else add to used
							tried.add(str(origins))
							for ((X,Y,Z), color) in used_coords:
								cube_open_vertices[X][Y][Z] = False


							# draw_shape(origins.values())

							new_unused_shapes = [s for s in unused_shapes if s is not shape_name]

							run(origins, cube_open_vertices, new_unused_shapes, shapes_dict)
							

							#FIX BACK TO WHAT WAS BEFORE
							for ((X,Y,Z), color) in used_coords:
								 cube_open_vertices[X][Y][Z] = True
							origins.pop(shape_name)

