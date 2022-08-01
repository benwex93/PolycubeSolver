#ADD TO GITHUB
#Each shape is defined by vertices

#		__
#	   /\_\
#	  / / /
#	 / / /
#	 \ \ \
#     \ \_\
#	   \/_/

s1 = [((0,0,0),'r'), ((1,0,0),'r'), ((2,0,0),'r'), ((0,1,0),'r'), ((0,2,0),'r')]

#      _ __
#   __/\/\_\
#  /\__  / /
#  \/__\/_/

s2 = [((0,0,0),'b'), ((0,0,1),'b'), ((0,1,0),'b'), ((1,1,0),'b'), ((1,2,0),'b')]

#     __
#    /\ \__
#    \ \/\ \
#     \   \_\
#      \/\/_/

s3 = [((0,0,0),'b'), ((1,0,0),'b'), ((2,0,0),'b'), ((2,1,0),'b'), ((3,1,0),'b')]

#        __
#   ____/\_\
#  /\__/ / /
#  \/_   \_\
#     \/\/_/

s4 = [((0,0,0),'r'), ((0,0,1),'r'), ((1,0,0),'r'), ((1,1,0),'r'), ((2,1,0),'r'), ((1,2,0),'r')]

#    __  __
#   /\ \/\_\
#   \ \_ / /
#    \/_ \_\
#     \/\/_/

s5 = [((0,0,0),'y'), ((1,0,0),'y'), ((0,1,0),'y'), ((0,-1,0),'y'), ((0,0,1),'y'), ((-1,0,1),'y')]

#     __
#    /\_\
#   / / /__
#  / / /__ \
#  \/____ \_\
#        \/_/

s6 = [((0,0,0),'b'), ((1,0,0),'b'), ((0,0,1),'b'), ((0,0,2),'b'), ((0,1,2),'b'), ((0,2,2),'b')]

#     __
#    /\ \_
#   / / / \
#   \ \____\
#    \_____/

s7 = [((0,0,0),'r'), ((0,1,0),'r'), ((1,0,0),'r'), ((0,0,-1),'r'), ((1,0,-1),'r')]

#      __
#     /\_\
#    / / /__
#   / / / __\
#   \/_ \_\_/
#      \/_/

s8 = [((0,0,0),'b'), ((0,1,0),'b'), ((0,2,0),'b'), ((0,0,-1),'b'), ((1,0,-1),'b'), ((0,0,-2),'b')]

#      __
#     /\_\
#    / / /
#   / / /\
#   \/_ \_\
#      \/_/

s9 = [((0,0,0),'y'), ((0,1,0),'y'), ((0,2,0),'y'), ((0,0,-1),'y'), ((1,0,-1),'y')]

#      __
#     /\_\
#    / / /__
#    \ \____\
#     \/____/  
#       \/_/

s10 = [((0,0,0),'y'), ((0,1,0),'y'), ((1,0,0),'y'), ((1,0,-1),'y'), ((1,-1,-1),'y')]

#      __
#     /\_\
#    / / /\
#   / /  \_\
#   \/_/\/_/
#     

s11 = [((0,0,0),'y'), ((0,1,0),'y'), ((0,-1,0),'y'), ((0,0,-1),'y'), ((1,0,-1),'y')]

#      __
#     /\_\_
#    / / /_\
#   / / ___/
#  / / /
#  \/_/   

s12 = [((0,0,0),'r'), ((0,1,0),'r'), ((0,0,-1),'r'), ((0,-1,0),'r'), ((0,-2,0),'r')]


from shape_drawer import draw_shape

# new_shape.append(((x,y,z), color))
# cubes.append(new_shape)

# swaps = ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1))
swaps = ((0,1,2),(0,2,1),(1,2,0),(2,0,1))
negations = ((1,1,1),(-1,1,1),(1,-1,1),(1,1,-1))

cube_open_vertices = [[[True for x in range(4)] for y in range(4)] for z in range(4)]

def add(shape, swap, negation, (Ox,Oy,Oz)):
	used_coords = []

	for (coords, color) in shape:

		x = coords[swap[0]]
		y = coords[swap[1]]
		z = coords[swap[2]]

		x *= negation[0]
		y *= negation[1]
		z *= negation[2]

		x += Ox
		y += Oy
		z += Oz

		used_coords.append(((x,y,z),color))
	return used_coords

shapes = [s4]
for shape in shapes:
	for swap in swaps:
		# for negation in negations:
		negation = (1, 1, 1)
		t_shape = add(shape,swap,negation,(0,0,0))
		print(swap)
		print(negation)
		draw_shape([t_shape])

		

tried = {}
def make_cube(origins, cube_open_vertices, unused_shapes):
	if unused_shapes is None:
		print('yay')
		print(origins)
		exit()

	# if len(unused_shapes) >= 6:
	for x in range(len(cube_open_vertices)):

		for y in range(len(cube_open_vertices[x])):
			for z in range(len(cube_open_vertices[y])):
				for shape_obj in unused_shapes:
					(shape_name, shape) = shape_obj
					for swap in swaps:
						for negation in negations:
							used_coords = add(shape, swap, negation, (x,y,z))
							valid_placement = True
							for (X,Y,Z) in used_coords:
								if X >= 4 or Y >= 4 or Z >= 4 or X < 0 or Y < 0 or Z < 0 or \
														not cube_open_vertices[X][Y][Z]:
									valid_placement = False
									break
							if valid_placement:
								origins[shape_name] = ((x,y,z), used_coords)

								if str(origins) in tried:
									origins.pop(shape_name)
									break
								tried[str(origins)] = True

								for (X,Y,Z) in used_coords:
									 cube_open_vertices[X][Y][Z] = False

								new_unused_shapes = [s for s in unused_shapes if s is not shape_obj]

								make_cube(origins, cube_open_vertices, new_unused_shapes)
								

								#FIX BACK TO WHAT WAS BEFORE
								for (X,Y,Z) in used_coords:
									 cube_open_vertices[X][Y][Z] = True
								origins.pop(shape_name)

make_cube({}, cube_open_vertices, [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12])