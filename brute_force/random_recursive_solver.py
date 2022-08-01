# from polycubes_array import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12

from common.shape_transformer import coordinates2matrix, matrix2coordinates, transform_shape

from common.shape_drawer import draw_shape, draw_shapes
import random
import copy
random.seed(10)

num_it = 0
def add(shape, cube_open_vertices, origins_list):

	(Ox,Oy,Oz) = origins_list
	used_coords = []
	for coords in shape:
		(x,y,z) = coords

		x += Ox
		y += Oy
		z += Oz

		# global num_it
		# if num_it > 7:
		# import pdb
		# pdb.set_trace()
		if x >= cube_open_vertices.shape[0] or y >= cube_open_vertices.shape[1] or z >= cube_open_vertices.shape[2] or \
				x < 0 or y < 0 or z < 0 or not cube_open_vertices[x][y][z]:
			#invalid placement
			return False, None

		# used_coords.append((x,y,z))
		used_coords.append((x,y,z))

	return True, used_coords

tried = set()
faces = [1,2,3,4,5,6]
rotations = [1,2,3,4]


trial = 0

def run(origins, cube_open_vertices, unused_shapes, transformed_shapes):
	global trial
	print('trial: ', trial)
	print(origins.keys())
	print('len:',len(origins.keys()))
	print(unused_shapes)
	print('len:',len(unused_shapes))
	trial+=1
	if unused_shapes == []:
		print('yay')
		draw_shapes(list(origins.values()))
		print(origins)
		exit()

	# removed = False
	# if trial % 100 == 0:
	# 	shape_to_remove = random.choice(list(origins.keys()))
	# 	(used_coords, color) = origins[shape_to_remove]
	# 	# cube_open_vertices = copy.deepcopy(cube_open_vertices)
	# 	for (X,Y,Z) in used_coords:
	# 		 cube_open_vertices[X][Y][Z] = True
	# 	# origins = copy.deepcopy(origins)
	# 	origins.pop(shape_to_remove)
	# 	unused_shapes.add(shape_to_remove)
	# 	removed = True

	for x in range(cube_open_vertices.shape[0]):
		for y in range(cube_open_vertices.shape[1]):
			for z in range(cube_open_vertices.shape[2]):
				for shape_name in unused_shapes:
					#get color by first transformation
					(transformed_shapes_list, color) = transformed_shapes[shape_name]
					random.shuffle(transformed_shapes_list)
					# for t in transformed_shapes_list:
					t = random.choice(transformed_shapes_list)
					# global num_it
					# print(num_it)
					# num_it+=1
					valid_placement, used_coords = add(t, cube_open_vertices, (x,y,z))

					if not valid_placement:
						continue
					# if trial >= 100:
					# 	import pdb
					# 	pdb.set_trace()
					origins[shape_name] = (used_coords, color)
					

					if str(origins) in tried:
						origins.pop(shape_name)
						continue
					#else add to used
					tried.add(str(origins))


					for (X,Y,Z) in used_coords:
						cube_open_vertices[X][Y][Z] = False

					# draw_shapes(list(origins.values()))

					new_unused_shapes = [s for s in unused_shapes if s is not shape_name]
					run(origins, cube_open_vertices, new_unused_shapes, transformed_shapes)

					# unused_shapes.remove(shape_name)
					# print(new_unused_shapes)
					# run(origins, cube_open_vertices, unused_shapes, transformed_shapes)

					# unused_shapes.add(shape_name)
					
					#if wasn't lost in random pop
					if shape_name in origins:

						#FIX BACK TO WHAT WAS BEFORE
						for (X,Y,Z) in used_coords:
							 cube_open_vertices[X][Y][Z] = True

						origins.pop(shape_name)
					else:
						print('not', shape_name)

