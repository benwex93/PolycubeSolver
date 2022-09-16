import argparse
from brute_force.recursive_solver import run as recursive_run
from brute_force.recursive_solver2 import RecursiveSolver2
from brute_force.recursive_solver3 import RecursiveSolver3
from algoX.polycubeDLX import PolycubeDLX
from genetic_algorithm.polycube_solverGA import PolycubeGA
from common.shape_transformer import generate_transformations
import numpy as np
from common.shape_drawer import draw_shape, draw_shapes

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--cube", type=int, default="")
	parser.add_argument("--solver", default="")
	args = parser.parse_args()

	print("---------------------------------------")
	print(f"Cube: {args.cube}, Solver: {args.solver}")
	print("---------------------------------------")

	if int(args.cube) == 1:

		same_shapes = False
		from polycubes_array_1 import shapes234, shapes244, shapes255, shapes555

		## 2x3x4 
		## 6x ----
		# shapes = shapes244
		# cube_open_vertices = np.full((2, 3, 4), True)
		# shapes_dict = {	's1':shapes[0], 's2':shapes[1], 's3':shapes[2] ,'s4':shapes[3],'s5':shapes[4], \
		# 				's6':shapes[5]}

		# shapes_names = ['s1', 's2', 's3','s4','s5','s6']
		# same_shapes = True

		## 2x4x4 
		## 4x ---__ 2x ----
		# shapes = shapes244
		# cube_open_vertices = np.full((2, 4, 4), True)
		# shapes_dict = {	's1':shapes[0], 's2':shapes[1], 's3':shapes[2] ,'s4':shapes[3],'s5':shapes[4], \
		# 				's6':shapes[5],'s7':shapes[6]}

		# shapes_names = ['s1', 's2', 's3','s4','s5','s6','s7']

		##2x5x5
		##10 x ---__
		# shapes = shapes255
		# cube_open_vertices = np.full((5, 5, 2), True)
		# shapes_dict = {	's1':shapes[0], 's2':shapes[1], 's3':shapes[2] ,'s4':shapes[3],'s5':shapes[4], \
		# 				's6':shapes[5],'s7':shapes[6], 's8':shapes[7],'s9':shapes[8], 's10':shapes[9]}

		# shapes_names = ['s1', 's2', 's3','s4','s5','s6','s7','s8','s9','s10']
		# same_shapes = True


		## 5x5x5
		# shapes = shapes555
		# cube_open_vertices = np.full((5, 5, 5), True)
		# shapes_dict = {	's1':shapes[0],'s2':shapes[1],'s3':shapes[2],'s4':shapes[3],'s5':shapes[4], \
		# 					's6':shapes[5],'s7':shapes[6],'s8':shapes[7],'s9':shapes[8],'s10':shapes[9],
		# 					's11':shapes[10],'s12':shapes[11],'s13':shapes[12],'s14':shapes[13],'s15':shapes[14], \
		# 					's16':shapes[15],'s17':shapes[16],'s18':shapes[17],'s19':shapes[18],'s20':shapes[19], \
		# 					's21':shapes[20],'s22':shapes[21],'s23':shapes[22],'s24':shapes[23],'s25':shapes[24]}
		# shapes_names = ['s1','s2','s3','s4','s5','s6','s7','s8','s9', 's10', \
		# 				's11','s12','s13','s14','s15','s16','s17','s18','s19', 's20', \
		# 				's21','s22','s23','s24','s25']
		# same_shapes = True


		# ## 4x4x4
		from polycubes_array_2 import shapes
		same_shapes = False
		cube_open_vertices = np.full((4, 4, 4), True)
		shapes_dict = {	's1':shapes[0],'s2':shapes[1],'s3':shapes[2],'s4':shapes[3],'s5':shapes[4], \
							's6':shapes[5],'s7':shapes[6],'s8':shapes[7],'s9':shapes[8],'s10':shapes[9],
							's11':shapes[10],'s12':shapes[11]}
		shapes_names = ['s1','s2','s3','s4','s5','s6','s7','s8','s9', 's10', \
						's11','s12']




		transformed_shapes = generate_transformations(shapes_dict)

		# for shape_name, (coords_ls, color) in transformed_shapes.items():
		# 	print(len(coords_ls))
		# 	for coords in coords_ls:
		# 		print(coords)
		# 		draw_shapes([(coords, color)])
				# break

	if str(args.solver) == 'brute_force':
		# recursive_run({}, cube_open_vertices, shapes_names, transformed_shapes)
		# recursive_solver = RecursiveSolver2(same_shapes)
		recursive_solver = RecursiveSolver3(same_shapes)
		recursive_solver.run(cube_open_vertices, shapes_names, transformed_shapes)

	elif str(args.solver) == 'algoX':
		polycubeDLX = PolycubeDLX(same_shapes)
		polycubeDLX.run(cube_open_vertices, shapes_names, transformed_shapes)

	elif str(args.solver) == 'genetic':
		polycubeGA = PolycubeGA(same_shapes)
		polycubeGA.run(cube_open_vertices, shapes_names, transformed_shapes)