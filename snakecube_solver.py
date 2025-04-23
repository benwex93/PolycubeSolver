import numpy as np

def solve_snakecube(size, snakecube, current_block_idx, cube_open, prev_coords, prev_moves):

	if current_block_idx == len(snakecube) - 1:
		#ends with an s
		print(prev_moves + prev_moves[-1])
		# exit(1)
		return

	current_block = snakecube[current_block_idx]
	prev_i, prev_j, prev_k = prev_coords

	#give default prev move if first cube is 's'
	if prev_moves == '':
		prev_move = 'R'
	else:
		prev_move = prev_moves[-1]

	moves_case = {
			'R': (prev_i + 1, prev_j, prev_k, prev_i + 1 < size),
			'L': (prev_i - 1, prev_j, prev_k, prev_i - 1 > -1),
			'B': (prev_i, prev_j + 1, prev_k, prev_j + 1 < size),
			'F': (prev_i, prev_j - 1, prev_k, prev_j - 1 > -1),
			'U': (prev_i, prev_j, prev_k + 1, prev_k + 1 < size),
			'D': (prev_i, prev_j, prev_k - 1, prev_k - 1 > -1),
	}
	if current_block == 's':
		(next_i, next_j, next_k, valid_next_placement) = moves_case[prev_move]
		if valid_next_placement and cube_open[next_i, next_j, next_k]:
			cube_open[next_i, next_j, next_k] = False
			# if current_block_idx >= 24:
			# 	breakpoint()
			solve_snakecube(size, snakecube, current_block_idx + 1, cube_open, (next_i, next_j, next_k), prev_moves + prev_move)
	else:
		#it's a bend so remove all impossible cases along same axis
		if prev_move in ['R', 'L']: 
			del moves_case['R']
			del moves_case['L']
		if prev_move in ['B', 'F']: 
			del moves_case['B']
			del moves_case['F']
		if prev_move in ['U', 'D']: 
			del moves_case['U']
			del moves_case['D']
		for move in moves_case:
			(next_i, next_j, next_k, valid_next_placement) = moves_case[move]

			if valid_next_placement and cube_open[next_i, next_j, next_k]:
				# add prev block placement back in since exploration is possible
				cube_open[next_i, next_j, next_k] = False		

				if current_block == 'b':
					solve_snakecube(size, snakecube, current_block_idx + 1, cube_open, (next_i, next_j, next_k), prev_moves + move)
				else:
					print('Error, unrecognized blocktype, check input string')
					exit(0)

	#remove prev block placement since no further exploration possible
	prev_move = prev_move[:-1]
	cube_open[prev_coords] = True


snakecube = 'sbss bbbb bbbb bbsb bssb bbbs sbsb bbbb bsbs bbbb bbbb bsbb sbbs bbss bbbs bbss'.replace(" ", "")
size = 4
# snakecube = 'ssbbbsbsbbbbbbbbbbbbbsbsbbs'
# size = 3

full_cube = np.full((size, size, size), True)

print(len(snakecube))

for i in range(size):
	for j in range(size):
		for k in range(size):
			#place the first cube
			full_cube[(i, j, k)] = False
			solve_snakecube(size, snakecube, 0, full_cube, (i, j, k), '')
			#undo the first cube
			full_cube[(i, j, k)] = True
			