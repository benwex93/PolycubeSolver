from algoX.dlx import DLX
import numpy as np
from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread, draw_shapes_one_each
from common.coverage_transformer import CoverageTransformer
from solution2x5x5 import sol_shapes

class PolycubeDLX:

    def __init__(self, same_shapes):
        self.ct = CoverageTransformer(same_shapes)

    def validate(self, solutions, s):
        result = []
        for k in s:
            result.append(k.ID)
        print(result)

        origins = self.ct.rows_to_shapes(result)
        # draw_shapes(origins)
        # animate_shapes_spread(origins)
        draw_shapes_one_each(origins)

    def callback(self, solutions, s):
        self.validate(solutions, s)

    def run(self, cube_open_vertices, shapes_names, transformed_shapes):
        
        problem_matrix = self.ct.generate_problem_matrix(cube_open_vertices, shapes_names, transformed_shapes)


        problem_matrix2 = np.zeros((len(sol_shapes),    cube_open_vertices.shape[0] * \
                                                        cube_open_vertices.shape[1] * \
                                                        cube_open_vertices.shape[2]))
        for row, placement in enumerate(sol_shapes):
            for coords in placement:
                col = self.ct.coords_dict[coords]
                problem_matrix2[row][col] = 1


        zeros_check = np.zeros((1,              cube_open_vertices.shape[0] * \
                                                cube_open_vertices.shape[1] * \
                                                cube_open_vertices.shape[2]))

        for i in range(0, problem_matrix2.shape[0]):
            for j in range(0, problem_matrix2.shape[1]):
                zeros_check[0][j] += problem_matrix2[i][j]

        for row1 in problem_matrix2:
            found = False
            for idx, row2 in enumerate(problem_matrix):
                if np.sum(np.all(row1 == row2, axis=0)):
                    print('found')
                    print(idx)

                    found = True
            if not found:
                print('not found')

        import pdb
        pdb.set_trace()
        dlx = DLX.from_matrix(problem_matrix, self.callback)
        ret = dlx.run(True)

