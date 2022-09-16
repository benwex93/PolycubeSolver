# from polycubes_array import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12

from common.shape_transformer import coordinates2matrix, matrix2coordinates, transform_shape
import numpy as np
from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread, draw_shapes_one_each
from common.coverage_transformer import CoverageTransformer

import itertools
import random

num_it = 0
trial = 0

import time
start_time = time.time()



class RecursiveSolver2():

    def __init__(self, same_shapes):

        self.ct = CoverageTransformer(same_shapes)

    def run(self, cube_open_vertices, shapes_names, transformed_shapes):
        
        problem_matrix = self.ct.generate_problem_matrix(cube_open_vertices, shapes_names, transformed_shapes)

        subset_k = itertools.combinations(range(0,problem_matrix.shape[0]), len(shapes_names))
        

        # for trial, idxs in enumerate(subset_k):
        #     # idxs = [207, 195, 99, 80, 64, 132, 6, 169, 77, 20]
        #     print(idxs)
        #     print(trial)
        #     if np.all(np.sum(np.take(problem_matrix, idxs,axis=0), axis=0)):
        #         origins = self.ct.rows_to_shapes(idxs)
        #         draw_shapes(origins)
        import pdb
        pdb.set_trace()
        ## try random idxs
        trial = 0
        while 1:
            (idxs) = random.sample(range(0,problem_matrix.shape[0]), len(shapes_names))
            # idxs = [207, 195, 99, 80, 64, 132, 6, 169, 77, 20]
            print(idxs)
            print(trial)
            trial+=1
            # origins = self.ct.rows_to_shapes(idxs)
            # draw_shapes(origins)
            if np.all(np.sum(np.take(problem_matrix, idxs,axis=0), axis=0)):
                origins = self.ct.rows_to_shapes(idxs)
                draw_shapes(origins)


