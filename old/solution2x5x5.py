#______x
#|\
#| \
#|  \
#|   \z
#y


#     __
#    /\ \__
#    \ \/\ \
#     \   \_\
#      \/\/_/

from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread

s1 = [(0,0,0),(0,1,0),(0,1,1),(0,2,1),(0,3,1)]

s2 = [(0,0,1),(1,0,1),(1,0,0),(2,0,0),(3,0,0)]

s3 = [(1,1,1),(2,1,1),(2,0,1),(3,0,1),(4,0,1)]

s4 = [(1,2,1),(2,2,1),(3,2,1),(3,1,1),(4,1,1)]

s5 = [(1,3,1),(2,3,1),(3,3,1),(3,4,1),(4,4,1)]

s6 = [(0,4,1),(1,4,1),(2,4,1),(2,4,0),(3,4,0)]

s7 = [(4,0,0),(4,1,0),(4,2,0),(4,2,1),(4,3,1)]

s8 = [(1,1,0),(1,2,0),(0,2,0),(0,3,0),(0,4,0)]

s9 = [(2,1,0),(2,2,0),(2,3,0),(1,3,0),(1,4,0)]

s10 = [(3,1,0),(3,2,0),(3,3,0),(4,3,0),(4,4,0)]

sol_shapes = [s1,s2, s3, s4, s5, s6, s7, s8, s9, s10]

# sol_shapes_dict = {	's1': ([s1], 'r'), 's2': ([s2], 'b'), 's3': ([s3], 'y'), \
# 					's4': ([s4], 'r'), 's5': ([s5], 'b'), 's6': ([s6], 'y'), \
# 					's7': ([s7], 'r'), 's8': ([s8], 'b'), 's9': ([s9], 'y'), 's10': ([s10], 'r')}

def check_no_overlap():
	counter = 0
	for x in range(5):
		for y in range(5):
			for z in range(2):
				no_flag = True
				for shape in sol_shapes:
					for coords in shape:
						if (x,y,z) == coords:
							counter+=1
							print(counter)
							no_flag = False
				if no_flag:
					print('not here')

def draw_solution():
	colors = ('r','b','y')

	cube = []
	for i, shape in enumerate(sol_shapes):
		print(shape)
		cube.append((shape, colors[i % len(colors)]))
	print(cube)
	draw_shapes(cube)

# check_no_overlap()
# draw_solution()