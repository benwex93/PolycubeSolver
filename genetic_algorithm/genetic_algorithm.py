

class GeneticAlgorithm:

	def __init__(self, end_condition, reporter, fitness_calculator, selector, \
					crossover, mutator):
		
		self.end_condition = end_condition
		self.reporter = reporter
		self.fitness_calculator = fitness_calculator
		self.selector = selector
		self.crossover = crossover
		self.mutator = mutator

	def run_ga(self, pop, next_pop):

		pop.initialize_pop()
		pop_fitness = self.fitness_calculator.calculate_fitness_of_individuals(pop)

		iteration = 0
		while not self.end_condition.should_end(pop=pop, pop_fitness=pop_fitness):

			self.reporter.report(pop=pop, pop_fitness=pop_fitness, iteration=iteration)
			next_pop = self.next_generation(pop=pop, pop_fitness=pop_fitness, next_pop=next_pop)
			pop.set_pop_list(next_pop.get_pop_list())
			pop_fitness = self.fitness_calculator.calculate_fitness_of_individuals(pop)
			iteration += 1

		self.reporter.report(pop=pop, pop_fitness=pop_fitness, iteration=iteration)
		return iteration 

	def next_generation(self, pop, pop_fitness, next_pop):

		next_pop.clear_pop()

		parent1, parent2 = self.selector.select(pop=pop, pop_fitness=pop_fitness, first=True)
		next_pop.insert(parent1)
		next_pop.insert(parent2)
 		offspring1, offspring2 = self.crossover.cross(parent1=parent1, parent2=parent2)
 		offspring1 = self.mutator.mutate(offspring1)
 		offspring2 = self.mutator.mutate(offspring2)
 		
		while not next_pop.is_full():
			parent1, parent2 = self.selector.select(pop=pop, pop_fitness=pop_fitness)
	 		offspring1, offspring2 = self.crossover.cross(parent1=parent1, parent2=parent2)
	 		offspring1 = self.mutator.mutate(offspring1)
	 		offspring2 = self.mutator.mutate(offspring2)
			next_pop.insert(offspring1)
			next_pop.insert(offspring2)
		return next_pop