import gym
from gym import spaces
from common.coverage_transformer import CoverageTransformer
from gym.spaces import MultiDiscrete, MultiBinary
import numpy as np

class PolyCubeEnv(gym.Env):

	def __init__(self, cube_open_vertices, problem_matrices, shapes_names):
		self.cube_spaces = cube_open_vertices.shape[0] * cube_open_vertices.shape[1] * cube_open_vertices.shape[2]
		self.shapes_names = shapes_names
		self.problem_matrices = problem_matrices

		self.action_space = gym.spaces.MultiDiscrete([3 for _ in range(len(self.shapes_names))])
		self.action_space.sample()



		self.action_dims = [problem_matrices[shape_name].shape[0] for shape_name in self.shapes_names]
		self.observation_space = MultiDiscrete(self.action_dims)


		#state is (num objects, x*y*z)
		# self.observation_space = MultiBinary([len(self.shapes_names), problem_matrices[self.shapes_names[0]].shape[1]])

	def step(self, action_list):
		for i, action in enumerate(action_list):
			self.state_idxs[i] += (action-1)
			self.state_idxs[i] %= self.action_dims[i]

		#get reward finding used spaces
		state = [self.problem_matrices[shape_name][idx] for shape_name, idx in zip(self.shapes_names, self.state_idxs)]

		taken_shapes = []
		for shape, idx in zip(self.shapes_names, self.state_idxs):
			taken_shapes.append(self.problem_matrices[shape][idx])
		reward = np.sum(np.sum(np.array(taken_shapes), axis=0) == 1)

		done = 0
		if reward == self.cube_spaces:
			done = 1
		info = None

		return state, reward, done, info 

	def reset(self):
		self.state_idxs = self.observation_space.sample()
		state = [self.problem_matrices[shape_name][idx] for shape_name, idx in zip(self.shapes_names, self.state_idxs)]
		return state
	# def render(self, mode='human', close=False):
	# 	pass
	# 	# Render the environment to the screen