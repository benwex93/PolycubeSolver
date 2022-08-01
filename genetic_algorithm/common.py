
class FixedEndCondition:
	def __init__(self, iterations):
		self.iterations = iterations
	def should_end(self, pop, pop_fitness):
		if self.iterations == 0:
			return True
		self.iterations -= 1
		return False

class FitnessDoneEndCondition:
	def __init__(self, fitness_desired):
		self.fitness_desired = fitness_desired
	def should_end(self, pop, pop_fitness):
		if max(pop_fitness) == self.fitness_desired:
			return True
		return False
import time
class TopNReporter:
	def __init__(self, top_n_to_report):
		self.top_n_to_report = top_n_to_report
		self.start = time.time()

	def report(self, pop, pop_fitness, iteration):
		print('iteration: ', iteration)
		# for individual, fitness in zip(pop.get_pop_list(), pop_fitness):
		# 	individual.print_chromosome()
		max_val = max(pop_fitness)
		print('best fitness: ', max_val)
		pop.get_pop_list()[pop_fitness.index(max_val)].print_chromosome()
		print('avg fitness: ', sum(pop_fitness) / float(len(pop_fitness)))
		print('time since start', time.time() - self.start)
import matplotlib.pyplot as plt
import numpy as np
import time
class PlotFitness:
	def __init__(self):
		plt.ion()
		self.best_fitness = []
		self.avg_fitness = []
		self.iterations = []
		self.start = time.time()
	def report(self, pop, pop_fitness, iteration):
	
		self.best_fitness.append(max(pop_fitness))
		self.avg_fitness.append(sum(pop_fitness) / float(len(pop_fitness)))
		# self.iterations.append(iteration)
		self.iterations.append(time.time() - self.start)


		plt.plot(self.iterations, self.best_fitness, 'r', label='Best Population Fitness')
		plt.plot(self.iterations, self.avg_fitness, 'b', label='Average Population Fitness')

		plt.title('Moving Avg of Fitness Over Time Until Convergence')
		# plt.xlabel('Iterations')
		plt.xlabel('Time (s)')
		plt.ylabel('Fitness')

		plt.legend()
		plt.draw()
		plt.pause(0.0001)
		plt.clf()

		print('iteration: ', iteration)
		# for individual, fitness in zip(pop.get_pop_list(), pop_fitness):
		# 	individual.print_chromosome()
		max_val = max(pop_fitness)
		print('best fitness: ', max_val)
		pop.get_pop_list()[pop_fitness.index(max_val)].print_chromosome()
		print('avg fitness: ', sum(pop_fitness) / float(len(pop_fitness)))
		
import random
class RouletteWheelSelector:
	def __init__(self, elitism=False, rank_based=False):
		self.elitism = elitism
		self.rank_based = rank_based

	def select(self, pop, pop_fitness, first=False):

		if first:
			if self.rank_based:
				pop.set_pop_list( \
					[x for _, x in sorted(zip(pop_fitness,pop.get_pop_list()), key=lambda pair: pair[0])])
				#store new pop_fitness
				self.ranked_pop_fitness = [i for i in range(0, len(pop_fitness))]

			if self.elitism:
				max_fitness_idx = pop_fitness.index(max(pop_fitness))
				best1 = pop.get_pop_list().pop(max_fitness_idx)
				best1_fitness = pop_fitness.pop(max_fitness_idx)

				best2 = pop.get_pop_list()[pop_fitness.index(max(pop_fitness))]
				#add best1 back in
				pop.get_pop_list().append(best1)
				pop_fitness.append(best1_fitness)

				return best1, best2

		if self.rank_based:
			pop_fitness = self.ranked_pop_fitness

		total_fitness = sum(pop_fitness)
		wheel_location = random.uniform(0, 1) * total_fitness

		index = 0
		current_sum = pop_fitness[index]

		while current_sum < wheel_location and index < (pop.size() - 1):
			index += 1
			current_sum = current_sum + pop_fitness[index]

		parent1 = pop.get_pop_list().pop(index)
		parent1_fitness = pop_fitness.pop(index)

		total_fitness = total_fitness - parent1_fitness
		wheel_location = random.uniform(0, 1) * total_fitness

		index = 0
		current_sum = pop_fitness[index]

		while current_sum < wheel_location and index < (pop.size() - 1):
			index += 1
			current_sum = current_sum + pop_fitness[index]

		parent2 = pop.get_pop_list()[index]

		#add parent1 back in
		pop.get_pop_list().append(parent1)
		pop_fitness.append(parent1_fitness)

		return parent1, parent2

import random
class RandomSelector:
	def select(self, pop, pop_fitness, first=False):
		return pop.get_pop_list()[random.randrange(pop.size())], pop.get_pop_list()[random.randrange(pop.size())]

