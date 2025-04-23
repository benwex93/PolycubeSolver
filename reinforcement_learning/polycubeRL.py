import numpy as np
from common.coverage_transformer import CoverageTransformer

from reinforcement_learning.polycube_env import PolyCubeEnv
class PolycubeRL:

    def __init__(self, same_shapes):
        self.ct = CoverageTransformer(same_shapes)
        self.same_shapes = same_shapes
        self.env = None

    def run(self, cube_open_vertices, shapes_names, transformed_shapes):
        
        problem_matrices = self.ct.generate_problem_matrices(cube_open_vertices, shapes_names, transformed_shapes)
        env = PolyCubeEnv(cube_open_vertices, problem_matrices, shapes_names)


        # Number of steps you run the agent for 
        num_steps = 1500

        obs = env.reset()

        for step in range(num_steps):
            # take random action, but you can also do something more intelligent
            # action = my_intelligent_agent_fn(obs) 
            action = env.action_space.sample()
            
            # apply the action
            obs, reward, done, info = env.step(action)
            
            print(reward)
            # Render the env
            # env.render()

            # If the epsiode is up, then start another one
            if done:
                env.reset()

        # Close the env
        env.close()