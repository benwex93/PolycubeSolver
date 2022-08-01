from common import FixedEndCondition, FitnessDoneEndCondition, TopNReporter, PlotFitness, \
	RouletteWheelSelector, RandomSelector
from genetic_algorithm import GeneticAlgorithm

class QueensNotAttackedFitnessCalculator:
	def calculate_fitness_of_individuals(self, pop):
		pop_fitness = []
		for individual in pop.get_pop_list():
			#rows with queens attacked
			queens_attacked = [False, False, False, False, False, False, False, False]

			board = individual.get_chromosome()
			#get column collisions first
			for col in range(8):
				if board.count(col) >= 2:
					for idx, rows_col in enumerate(board):
						if rows_col == col:
							queens_attacked[idx] = True

			#diagonal collisions
			for row, rows_col in enumerate(board):
				#if not already attacked
				if not queens_attacked[row]:
					#start at 1 to skip itself
					for i in range(1, 8):
						#diagonal down
						if row + i < 8:
							#backwards
							if board[row + i] == rows_col - i:
								queens_attacked[row] = True
								queens_attacked[row + i] = True
							#forwards
							if board[row + i] == rows_col + i:
								queens_attacked[row] = True
								queens_attacked[row + i] = True					
						#diagonal up
						if row - i >= 0:
							#backwards
							if board[row - i] == rows_col - i:
								queens_attacked[row] = True
								queens_attacked[row - i] = True
							#forwards
							if board[row - i] == rows_col - i:
								queens_attacked[row] = True
								queens_attacked[row - i] = True

			pop_fitness.append(queens_attacked.count(False))
		return pop_fitness

import random
class QueensHalfCrossover:
	def __init__(self, prob_crossover, chromosome_type):
		self.prob_crossover = prob_crossover
		self.chromosome_type = chromosome_type
	def cross(self, parent1, parent2):
		chromosome1 = parent1.get_chromosome()
		chromosome2 = parent2.get_chromosome()
		if random.uniform(0, 1) < self.prob_crossover:
			return self.chromosome_type(chromosome1[:4] + chromosome2[4:]), \
						self.chromosome_type(chromosome2[:4] + chromosome1[4:])
		return self.chromosome_type(chromosome1), self.chromosome_type(chromosome2)

import random
class QueensRandomUniformMutator:
	def __init__(self, prob_mutation):
		self.prob_mutation = prob_mutation
	def mutate(self, offspring):
		offspring_chromosome = offspring.get_chromosome()
		offspring.set_chromosome([random.randrange(8) if random.uniform(0, 1) < self.prob_mutation 
										else i for i in offspring_chromosome])
		return offspring

import random
class QueensRowChromosome():
	def __init__(self, chromosome=None):
		if chromosome == None:
			self.chromosome = [random.randrange(8) for _ in range(8)]
		else:
			self.chromosome = chromosome
	def print_chromosome(self):
		for i in self.chromosome:
			row = ['-','-','-','-','-','-','-','-']
			row[i] = 'Q'
			print(row)
		print
	def get_chromosome(self):
		return self.chromosome
	def set_chromosome(self, chromosome):
		self.chromosome = chromosome
						
class QueensPopulation:
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
end_condition = FitnessDoneEndCondition(fitness_desired=8)
reporter = TopNReporter(top_n_to_report=1)
# reporter = PlotFitness()
fitness_calculator = QueensNotAttackedFitnessCalculator()
selector = RouletteWheelSelector()
crossover = QueensHalfCrossover(prob_crossover=0.1, chromosome_type=QueensRowChromosome)
mutator = QueensRandomUniformMutator(prob_mutation=0.1)

queens_pop1 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
queens_next_pop1 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
assert (queens_pop1.size() == queens_next_pop1.size()), 'pop_sizes not equal'
assert (queens_pop1.size() % 2 == 0), 'pop_size not even number'
assert (queens_pop1.chromosome_type == queens_next_pop1.chromosome_type), 'chromosome_type not the same'

ga1 = GeneticAlgorithm(end_condition=end_condition, reporter=reporter, fitness_calculator=fitness_calculator, \
						selector=selector, crossover=crossover, mutator=mutator)
ga1.run_ga(queens_pop1, queens_next_pop1)

# ############################
# #Random Guessing
# ############################
# end_condition = FitnessDoneEndCondition(fitness_desired=8)
# reporter = TopNReporter(top_n_to_report=1)
# fitness_calculator = QueensNotAttackedFitnessCalculator()
# selector = RandomSelector()
# crossover = QueensHalfCrossover(prob_crossover=0, chromosome_type=QueensRowChromosome)
# mutator = QueensRandomUniformMutator(prob_mutation=1)

# queens_pop2 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
# queens_next_pop2 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
# assert (queens_pop2.size() == queens_next_pop2.size()), 'pop_sizes not equal'
# assert (queens_pop2.size() % 2 == 0), 'pop_size not even number'
# assert (queens_pop2.chromosome_type == queens_next_pop2.chromosome_type), 'chromosome_type not the same'

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
# 	queens_pop1 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
# 	queens_next_pop1 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)


# 	start = time.time()
# 	ga1.run_ga(queens_pop1, queens_next_pop1)
# 	time_taken = time.time() - start
	
# 	ga_iters.append(time_taken)
# 	# ga_iters.append(ga1.run_ga(queens_pop1, queens_next_pop1))

# 	queens_pop2 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)
# 	queens_next_pop2 = QueensPopulation(pop_size=20, chromosome_type=QueensRowChromosome)

# 	start = time.time()
# 	ga2.run_ga(queens_pop2, queens_next_pop2)
# 	time_taken = time.time() - start

# 	random_iters.append(time_taken)
# 	# random_iters.append(ga2.run_ga(queens_pop2, queens_next_pop2))

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