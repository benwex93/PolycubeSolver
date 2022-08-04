from shape_drawer import draw_shape


from common import FixedEndCondition, FitnessDoneEndCondition, TopNReporter, PlotFitness, \
	RouletteWheelSelector, RandomSelector
from genetic_algorithm import GeneticAlgorithm

class CubeCoordsUsedCalculator:
	def __init__(self):
		self.shapes_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
		# 6 possible 45 degree rotations for x,y,z with 4 90 degree rotations = 24 isometries
		# a cube can be placed on any of its 6 faces and rotated so that 1 of the 4 faces, faces forward
		# x,y,z -x,y,z, x,-y,z x,y,-z
		# x,z,y ...
		# y,x,z ...
		# y,z,x ...
		# z,y,x ...
		# z,x,y ...

		self.swaps = ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1))
		self.negations = ((1,1,1),(-1,1,1),(1,-1,1),(1,1,-1))

	def calculate_fitness_of_individuals(self, pop):
		pop_fitness = []
		for individual in pop.get_pop_list():
			#x,y,z used in cube with only one cube per coordinate
			cube_open_vertices = [[[False for x in range(4)] for y in range(4)] for z in range(4)]

			shape_origin_coords = individual.get_chromosome()
			for origin_coords, shape in zip(shape_origin_coords, self.shapes_list):
				(Ox, Oy, Oz), (swap_axes, negate_axes) = origin_coords
				add_shape_coords = []
				valid_place = True
				for (coords, color) in shape:

					swap = self.swaps[swap_axes]
					negate = self.negations[negate_axes]

					x = coords[swap[0]]
					y = coords[swap[1]]
					z = coords[swap[2]]

					x *= negate[0]
					y *= negate[1]
					z *= negate[2]

					x += Ox
					y += Oy
					z += Oz

					if x >= 0 and x < 4 and y >= 0 and y < 4 and z >= 0 and z < 4 and not cube_open_vertices[x][y][z]:
						add_shape_coords.append((x,y,z))
					else:
						valid_place = False
						break
				if valid_place:
					for (x,y,z) in add_shape_coords:
						cube_open_vertices[x][y][z] = True
			spots_taken = 0
			for coords_list_list in cube_open_vertices:
				for coords_list in coords_list_list:
					spots_taken += coords_list.count(True)
			pop_fitness.append(spots_taken)
		return pop_fitness

import random
class CubeCoordsHalfCrossover:
	def __init__(self, prob_crossover, chromosome_type):
		self.prob_crossover = prob_crossover
		self.chromosome_type = chromosome_type
	def cross(self, parent1, parent2):
		chromosome1 = parent1.get_chromosome()
		chromosome2 = parent2.get_chromosome()











		######COPY???













		if random.uniform(0, 1) < self.prob_crossover:
			return self.chromosome_type(chromosome1[:6] + chromosome2[6:]), \
						self.chromosome_type(chromosome2[:6] + chromosome1[6:])
		return self.chromosome_type(chromosome1), self.chromosome_type(chromosome2)

# import random
# class CubeCoordsRandomUniformMutator:
# 	def __init__(self, prob_mutation):
# 		self.prob_mutation = prob_mutation
# 	def mutate(self, offspring):
# 		offspring_chromosome = offspring.get_chromosome()
# 		new_chromosome = []
# 		for i in offspring_chromosome:
# 			if random.uniform(0, 1) < self.prob_mutation:
# 				index = random.randrange(5)
# 				if index == 0:
# 					rand_chrom = random.randrange(4)
# 					i = ((rand_chrom, i[0][1], i[0][2]),i[1])
# 				elif index == 1:
# 					rand_chrom = random.randrange(4)
# 					i = ((i[0][0], rand_chrom, i[0][2]),i[1])
# 				elif index == 2:
# 					rand_chrom = random.randrange(4)
# 					i = ((i[0][0], i[0][1], rand_chrom),i[1])
# 				elif index == 3:
# 					rand_chrom = random.randrange(6)
# 					i = (i[0],(rand_chrom, i[1][1]))
# 				elif index == 4:
# 					rand_chrom = random.randrange(4)
# 					i = (i[0],(i[1][0], rand_chrom))
# 			new_chromosome.append(i)
# 		offspring.set_chromosome(new_chromosome)
# 		return offspring

class CubeCoordsRandomUniformMutator:
	def __init__(self, prob_mutation):
		self.prob_mutation = prob_mutation
	def mutate(self, offspring):
		offspring_chromosome = offspring.get_chromosome()
		
		offspring.set_chromosome([((random.randrange(4), random.randrange(4), random.randrange(4)), \
									(random.randrange(6), random.randrange(4))) \
										if random.uniform(0, 1) < self.prob_mutation \
										else i for i in offspring_chromosome])
		return offspring
import random
class CubeCoordsUniformCrossover:
	def __init__(self, prob_crossover, chromosome_type):
		self.prob_crossover = prob_crossover
		self.chromosome_type = chromosome_type
	def cross(self, parent1, parent2):
		chromosome1 = parent1.get_chromosome()
		chromosome2 = parent2.get_chromosome()
		if random.uniform(0, 1) < self.prob_crossover:
			crossover = [(i, j) if random.randrange(2) else (j, i) for i, j in zip (chromosome1, chromosome2)] 
			chromosome1, chromosome2 = zip(*crossover)
		return self.chromosome_type(chromosome1), self.chromosome_type(chromosome2)

import random
# from shape_drawer import draw_shape
it = 0
class CubeCoordsChromosome():
	def __init__(self, chromosome=None):
		if chromosome == None:
			# 6 possible 45 degree rotations for x,y,z with 4 90 degree rotations = 24 isometries
			# a cube can be placed on any of its 6 faces and rotated so that 1 of the 4 faces, faces forward
			# x,y,z -x,y,z, x,-y,z x,y,-z
			# x,z,y
			# y,x,z
			# y,z,x
			# z,y,x
			# z,x,y
			#(x,y,z,6swap_axes,4negate_axes)
			self.chromosome = [((random.randrange(4), random.randrange(4), random.randrange(4)), \
									(random.randrange(6), random.randrange(4))) for _ in range(12)]
		else:
			self.chromosome = chromosome

		self.shapes_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
		self.swaps = ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1))
		self.negations = ((1,1,1),(-1,1,1),(1,-1,1),(1,1,-1))

	def print_chromosome(self):
		global it
		if it % 100000 == 0:
			shape_origin_coords = self.chromosome
			cubes = []
			for origin_coords, shape in zip(shape_origin_coords, self.shapes_list):
				(Ox, Oy, Oz), (swap_axes, negate_axes) = origin_coords
				new_shape = []
				for (coords, color) in shape:

					swap = self.swaps[swap_axes]
					negate = self.negations[negate_axes]

					x = coords[swap[0]]
					y = coords[swap[1]]
					z = coords[swap[2]]

					x *= negate[0]
					y *= negate[1]
					z *= negate[2]

					x += Ox
					y += Oy
					z += Oz

					new_shape.append(((x,y,z), color))
				cubes.append(new_shape)
			draw_shape(cubes)
		it += 1
		print self.chromosome
	def get_chromosome(self):
		return self.chromosome
	def set_chromosome(self, chromosome):
		self.chromosome = chromosome
						
class CubePopulation:
	def __init__(self, pop_size, chromosome_type):
		self.pop_size = pop_size
		self.chromosome_type = chromosome_type
		self.pop_list = []
	def initialize_pop(self):
		self.pop_list = [self.chromosome_type() for _ in range(self.pop_size)]
	def clear_pop(self):
		for individual in self.pop_list:
			del individual
		self.pop_list = []
	def is_full(self):
		if len(self.pop_list) == self.pop_size:
			return True
		return False
	def insert(self, offspring):
		self.pop_list.append(offspring)
	def size(self):
		return len(self.pop_list)
	def get_pop_list(self):
		return self.pop_list
	def set_pop_list(self, pop_list):
		self.pop_list = pop_list

############################
#Genetic Algorithm
############################
end_condition = FitnessDoneEndCondition(fitness_desired=64)
reporter = TopNReporter(top_n_to_report=1)
# reporter = PlotFitness()
fitness_calculator = CubeCoordsUsedCalculator()
selector = RouletteWheelSelector()
# crossover = CubeCoordsHalfCrossover(prob_crossover=0.2, chromosome_type=CubeCoordsChromosome)
crossover = CubeCoordsUniformCrossover(prob_crossover=0.5, chromosome_type=CubeCoordsChromosome)
mutator = CubeCoordsRandomUniformMutator(prob_mutation=0.01)

cube_pop = CubePopulation(pop_size=800, chromosome_type=CubeCoordsChromosome)
cube_next_pop = CubePopulation(pop_size=800, chromosome_type=CubeCoordsChromosome)
assert (cube_pop.size() == cube_next_pop.size()), 'pop_sizes not equal'
assert (cube_pop.size() % 2 == 0), 'pop_size not even number'
assert (cube_pop.chromosome_type == cube_next_pop.chromosome_type), 'chromosome_type not the same'

ga = GeneticAlgorithm(end_condition=end_condition, reporter=reporter, fitness_calculator=fitness_calculator, \
						selector=selector, crossover=crossover, mutator=mutator)
ga.run_ga(cube_pop, cube_next_pop)
