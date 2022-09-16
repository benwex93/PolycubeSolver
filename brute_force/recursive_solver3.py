import numpy as np
from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread, draw_shapes_one_each
from common.coverage_transformer import CoverageTransformer

import time
start_time = time.time()



class RecursiveSolver3():

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

        self.problem_matrix = self.ct.generate_problem_matrix(cube_open_vertices, shapes_names, transformed_shapes)

        self.find_coverage([],list(range(0,self.problem_matrix.shape[0])))


