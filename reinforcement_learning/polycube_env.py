import gym
from gym import spaces

class PolyCubeEnv(gym.Env):
	"""Custom Environment that follows gym interface"""
	metadata = {'render.modes': ['human']}

	def __init__(self, arg1, arg2, ...):
		super(CustomEnv, self).__init__()
		# Define action and observation space
		# They must be gym.spaces objects
		# Example when using discrete actions:
		self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
		# Example for using image as input:
		self.observation_space = spaces.Box(low=0, high=255, shape=
		(HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)
		self.state = None
	def step(self, action):
		# Execute one time step within the environment
		# action is tuple of len(shapes_ls) with actions being -1, 0, 1 for go up, stay, or down shapes list which loops back on self
		for s in action:

	def reset(self):
		self.state = rand index in problem_matrices
		# Reset the state of the environment to an initial state
	def render(self, mode='human', close=False):
		# Render the environment to the screen