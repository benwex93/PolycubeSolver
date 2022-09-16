from genetic_algorithm.common import FixedEndCondition, FitnessDoneEndCondition, TopNReporter, PlotFitness, \
	RouletteWheelSelector, RandomSelector
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

import numpy as np
from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread, draw_shapes_one_each
from common.coverage_transformer import CoverageTransformer

class PolycubeOnePerSpacesFitnessCalculator:
	def __init__(self, problem_matrices, shapes_names):
		self.problem_matrices = problem_matrices
		self.shapes_names = shapes_names
	def calculate_fitness_of_individuals(self, pop):
		pop_fitness = []
		for individual in pop.get_pop_list():
			idxs = individual.get_chromosome()
			taken_shapes = []
			for shape, idx in zip(self.shapes_names, idxs):
				taken_shapes.append(self.problem_matrices[shape][idx])
			pop_fitness.append(np.sum(np.sum(np.array(taken_shapes), axis=0) == 1))
		# print(pop_fitness)
		return pop_fitness

import random
class PolycubeHalfCrossover:
	def __init__(self, prob_crossover, chromosome_type, chromosome_length, chromosome_idxs):
		self.prob_crossover = prob_crossover  
		self.chromosome_type = chromosome_type
		self.chromosome_length = chromosome_length
		self.chromosome_half_length = int(chromosome_length / 2)
		self.chromosome_idxs = chromosome_idxs

	def cross(self, parent1, parent2):
		chromosome1 = parent1.get_chromosome()
		chromosome2 = parent2.get_chromosome()
		if random.uniform(0, 1) < self.prob_crossover:
			return self.chromosome_type(chromosome1[:self.chromosome_half_length] + chromosome2[self.chromosome_half_length:], self.chromosome_idxs), \
						self.chromosome_type(chromosome2[:self.chromosome_half_length] + chromosome1[self.chromosome_half_length:], self.chromosome_idxs)
		return self.chromosome_type(chromosome1, self.chromosome_idxs), self.chromosome_type(chromosome2, self.chromosome_idxs)

import random
class PolycubeRandomUniformMutator:
	def __init__(self, prob_mutation, chromosome_length, chromosome_idxs):
		self.prob_mutation = prob_mutation
		self.chromosome_length = chromosome_length
		self.chromosome_idxs = chromosome_idxs
	def mutate(self, offspring):
		offspring_chromosome = offspring.get_chromosome()
		offspring.set_chromosome([random.randrange(self.chromosome_idxs[i]) if random.uniform(0, 1) < self.prob_mutation 
										else chromosome for i, chromosome in enumerate(offspring_chromosome)])
		return offspring

import random
class PolycubeRowChromosome():
	def __init__(self, chromosome_length, chromosome_idxs, chromosome=None):
		if chromosome == None:
			self.chromosome = [random.randrange(chromosome_idx) for chromosome_idx in chromosome_idxs]
		else:
			self.chromosome = chromosome
	def print_chromosome(self):
		print(self.chromosome)
		print
	def get_chromosome(self):
		return self.chromosome
	def set_chromosome(self, chromosome):
		self.chromosome = chromosome
						
class PolycubePopulation:
	def __init__(self, pop_size, chromosome_type, chromosome_length, chromosome_idxs):
		self.pop_size = pop_size
		self.chromosome_type = chromosome_type
		self.pop_list = []
		self.chromosome_length = chromosome_length
		self.chromosome_idxs = chromosome_idxs
	def initialize_pop(self):
		self.pop_list = [self.chromosome_type(self.chromosome_length, self.chromosome_idxs) for _ in range(self.pop_size)]
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

import time
class PolycubeTopNReporter:
	def __init__(self, top_n_to_report, shapes_names, problem_matrices, ct):
		self.top_n_to_report = top_n_to_report
		self.start = time.time()
		self.best_global = 0
		self.shapes_names = shapes_names
		self.problem_matrices = problem_matrices
		self.ct = ct

	def report(self, pop, pop_fitness, iteration):
		print('iteration: ', iteration)
		# for individual, fitness in zip(pop.get_pop_list(), pop_fitness):
		# 	individual.print_chromosome()
		max_val = max(pop_fitness)
		print('best fitness: ', max_val)
		best_individual = pop.get_pop_list()[pop_fitness.index(max_val)]
		best_individual.print_chromosome()
		print('avg fitness: ', sum(pop_fitness) / float(len(pop_fitness)))
		if max_val > self.best_global:
			self.best_global = max_val
		print('best global fitness: ', self.best_global)
		print('time since start', time.time() - self.start)

		idxs = best_individual.get_chromosome()
		taken_shapes = []
		for shape, idx in zip(self.shapes_names, idxs):
			taken_shapes.append(self.problem_matrices[shape][idx])
		with np.printoptions(threshold=np.inf):
			print(np.array(taken_shapes))
		import pdb
		pdb.set_trace()
		origins = self.ct.rows_to_shapes(np.array(taken_shapes))
		draw_shapes(origins)
		# pop_fitness.append(np.sum(np.sum(np.array(taken_shapes), axis=0) == 1))

############################
#Genetic Algorithm
############################

class PolycubeGA():

	def __init__(self, same_shapes):

		self.ct = CoverageTransformer(same_shapes)
		self.cube_open_vertices = None
		self.shapes_names = None
		self.transformed_shapes = None
		self.problem_matrix = None
		self.trial = 0

	def find_coverage(self, idxs_used, idxs_unused):
		print('idxs_used', idxs_used)
		print('trial', self.trial)
		print(time.time() - start_time, "seconds")
		self.trial += 1
		if len(idxs_used) == len(self.shapes_names):
			origins = self.ct.rows_to_shapes(idxs_used)
			draw_shapes(origins)
			return

		for idx in idxs_unused:
			if np.all(np.sum(np.take(self.problem_matrix, idxs_used + [idx],axis=0), axis=0) < 2):
				self.find_coverage(idxs_used + [idx], [n for n in idxs_unused if n != idx])

	def run(self, cube_open_vertices, shapes_names, transformed_shapes):

		self.cube_open_vertices = cube_open_vertices
		self.shapes_names = shapes_names
		self.transformed_shapes = transformed_shapes

		problem_matrices = self.ct.generate_problem_matrices(cube_open_vertices, shapes_names, transformed_shapes)
		chromosome_length = len(self.shapes_names)
		chromosome_idxs = [problem_matrices[shape_name].shape[0] for shape_name in self.shapes_names]

		total_size = cube_open_vertices.shape[0] * cube_open_vertices.shape[0] * cube_open_vertices.shape[0]
		end_condition = FitnessDoneEndCondition(fitness_desired=total_size)
		reporter = PolycubeTopNReporter(top_n_to_report=1, shapes_names=shapes_names, problem_matrices=problem_matrices, ct=self.ct)
		# reporter = TopNReporter(top_n_to_report=1)
		# reporter = PlotFitness()
		fitness_calculator = PolycubeOnePerSpacesFitnessCalculator(problem_matrices, shapes_names)
		selector = RouletteWheelSelector()
		crossover = PolycubeHalfCrossover(prob_crossover=0.1, chromosome_type=PolycubeRowChromosome, chromosome_length=chromosome_length, chromosome_idxs=chromosome_idxs)
		mutator = PolycubeRandomUniformMutator(prob_mutation=0.01, chromosome_length=chromosome_length, chromosome_idxs=chromosome_idxs)

		Polycube_pop1 = PolycubePopulation(pop_size=400, chromosome_type=PolycubeRowChromosome, chromosome_length=chromosome_length, chromosome_idxs=chromosome_idxs)
		Polycube_next_pop1 = PolycubePopulation(pop_size=400, chromosome_type=PolycubeRowChromosome, chromosome_length=chromosome_length, chromosome_idxs=chromosome_idxs)
		assert (Polycube_pop1.size() == Polycube_next_pop1.size()), 'pop_sizes not equal'
		assert (Polycube_pop1.size() % 2 == 0), 'pop_size not even number'
		assert (Polycube_pop1.chromosome_type == Polycube_next_pop1.chromosome_type), 'chromosome_type not the same'

		ga1 = GeneticAlgorithm(end_condition=end_condition, reporter=reporter, fitness_calculator=fitness_calculator, \
								selector=selector, crossover=crossover, mutator=mutator)
		ga1.run_ga(Polycube_pop1, Polycube_next_pop1)



# ############################
# #Random Guessing
# ############################
# end_condition = FitnessDoneEndCondition(fitness_desired=8)
# reporter = TopNReporter(top_n_to_report=1)
# fitness_calculator = PolycubeNotAttackedFitnessCalculator()
# selector = RandomSelector()
# crossover = PolycubeHalfCrossover(prob_crossover=0, chromosome_type=PolycubeRowChromosome)
# mutator = PolycubeRandomUniformMutator(prob_mutation=1)

# Polycube_pop2 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)
# Polycube_next_pop2 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)
# assert (Polycube_pop2.size() == Polycube_next_pop2.size()), 'pop_sizes not equal'
# assert (Polycube_pop2.size() % 2 == 0), 'pop_size not even number'
# assert (Polycube_pop2.chromosome_type == Polycube_next_pop2.chromosome_type), 'chromosome_type not the same'

# ga2 = GeneticAlgorithm(end_condition=end_condition, reporter=reporter, fitness_calculator=fitness_calculator, \
# 						selector=selector, crossover=crossover, mutator=mutator)


# import matplotlib.pyplot as plt
# import numpy as np
# import time

# plt.ion()
# ga_iters, random_iters = [], []
# ga_avg, random_avg = [], []
# iterations = []
# for i in range(1000):

# 	#get num of iterations
# 	Polycube_pop1 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)
# 	Polycube_next_pop1 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)


# 	start = time.time()
# 	ga1.run_ga(Polycube_pop1, Polycube_next_pop1)
# 	time_taken = time.time() - start
	
# 	ga_iters.append(time_taken)
# 	# ga_iters.append(ga1.run_ga(Polycube_pop1, Polycube_next_pop1))

# 	Polycube_pop2 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)
# 	Polycube_next_pop2 = PolycubePopulation(pop_size=20, chromosome_type=PolycubeRowChromosome)

# 	start = time.time()
# 	ga2.run_ga(Polycube_pop2, Polycube_next_pop2)
# 	time_taken = time.time() - start

# 	random_iters.append(time_taken)
# 	# random_iters.append(ga2.run_ga(Polycube_pop2, Polycube_next_pop2))

# 	#plot average
# 	iterations.append(i)

# 	ga_avg.append(sum(ga_iters) / float(len(ga_iters)))
# 	random_avg.append(sum(random_iters) / float(len(random_iters)))

# 	plt.plot(iterations, ga_avg, 'r', label='Roulette Wheel Average')
# 	plt.plot(iterations, random_avg, 'b', label='Random Guess Average')

# 	plt.title('Moving Avg of Secs Until Convergence')
# 	plt.xlabel('Runs')
# 	plt.ylabel('Time (s)')

# 	plt.legend()
# 	plt.draw()
# 	plt.pause(0.0001)
# 	plt.clf()