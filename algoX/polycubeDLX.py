from algoX.dlx import DLX
import numpy as np
from common.shape_drawer import draw_shape, draw_shapes, draw_shapes_spread, animate_shapes_spread, draw_shapes_one_each
from solution2x5x5 import sol_shapes

class PolycubeDLX:

    def __init__(self, same_shapes):
        self.problem_matrix = None
        self.coords_dict = {}
        self.shapes_dict = {}
        self.shapes_colors_dict = {}
        self.same_shapes = same_shapes

    def add(self, shape, cube_open_vertices, origins_list):

        (Ox,Oy,Oz) = origins_list
        used_coords = []
        for coords in shape:
            (x,y,z) = coords

            x += Ox
            y += Oy
            z += Oz

            # global num_it
            # if num_it > 7:
            # import pdb
            # pdb.set_trace()
            if x >= cube_open_vertices.shape[0] or y >= cube_open_vertices.shape[1] or z >= cube_open_vertices.shape[2] or \
                    x < 0 or y < 0 or z < 0 or not cube_open_vertices[x][y][z]:
                #invalid placement
                return False, None

            # used_coords.append((x,y,z))
            used_coords.append((x,y,z))

        return True, used_coords

    def generate_problem_matrix(self, cube_open_vertices, shapes_names, transformed_shapes):
        

        cntr = 0

        if not self.same_shapes:
            #Number all polycubes with unique ID
            for shape_name in shapes_names:
                self.shapes_dict[shape_name] = cntr
                cntr += 1

        #Number all 3d box coords with unique ID in dict
        for x in range(cube_open_vertices.shape[0]):
            for y in range(cube_open_vertices.shape[1]):
                for z in range(cube_open_vertices.shape[2]):
                    self.coords_dict[(x,y,z)] = cntr
                    cntr += 1

        placements = []
        for x in range(cube_open_vertices.shape[0]):
            for y in range(cube_open_vertices.shape[1]):
                for z in range(cube_open_vertices.shape[2]):
                    for num, shape_name in enumerate(shapes_names):
                        print(shape_name, num)
                        #get color by first transformation
                        (transformed_shapes_list, color) = transformed_shapes[shape_name]
                        for t in transformed_shapes_list:
                            valid_placement, used_coords = self.add(t, cube_open_vertices, (x,y,z))
                            if not valid_placement:
                                continue
                            placements.append((shape_name, used_coords))


        self.problem_matrix = np.zeros((len(placements), len(self.shapes_dict) + \
                                                        cube_open_vertices.shape[0] * \
                                                        cube_open_vertices.shape[1] * \
                                                        cube_open_vertices.shape[2]))
        for row, placement in enumerate(placements):
            if not self.same_shapes:
                self.problem_matrix[row][self.shapes_dict[placement[0]]] = 1
            for coords in placement[1]:
                col = self.coords_dict[coords]

                self.problem_matrix[row][col] = 1




        #remove duplicate entries
        # import pdb
        # pdb.set_trace()
        self.problem_matrix = np.unique(self.problem_matrix, axis=0)
        print('after unique:', self.problem_matrix)

        with np.printoptions(threshold=np.inf):
            print(np.array2string(self.problem_matrix, max_line_width=np.inf))
            print('self.problem_matrix',self.problem_matrix.shape)

        zeros_check = np.zeros((1,len(self.shapes_dict) + \
                                                        cube_open_vertices.shape[0] * \
                                                        cube_open_vertices.shape[1] * \
                                                        cube_open_vertices.shape[2]))

        for i in range(0, self.problem_matrix.shape[0]):
            for j in range(0, self.problem_matrix.shape[1]):
                zeros_check[0][j] += self.problem_matrix[i][j]
        print('zeros_check',zeros_check)

        return self.problem_matrix


    def validate(self, solutions, s):
        result = []
        for k in s:
            result.append(k.ID)
        print(result)

        origins = []
        shapes_dict_swap = {v: k for k, v in self.shapes_dict.items()}
        coords_dict_swap = {v: k for k, v in self.coords_dict.items()}
        for color_i, res in enumerate(result):
            shape_coords = []
            row = self.problem_matrix[res]

            if not self.same_shapes:
                #get shape
                for i in range(len(self.shapes_dict)):
                    if row[i] != 0:
                        shape_name = shapes_dict_swap[i]

            #get coords
            for i in range(len(self.shapes_dict), self.problem_matrix.shape[1]):
                if row[i] != 0:
                    shape_coords.append(coords_dict_swap[i])

            if not self.same_shapes:
                origins.append((shape_coords, self.shapes_colors_dict[shape_name]))
            else:
                colors = ('r','b','y')
                origins.append((shape_coords, colors[color_i % len(colors)]))
        # draw_shapes(origins)
        # animate_shapes_spread(origins)
        draw_shapes_one_each(origins)

    def callback(self, solutions, s):
        self.validate(solutions, s)

    def fake_matrix(self):
        self.problem_matrix = np.zeros((760,60))
        for i in range(0, self.problem_matrix.shape[0]):
            for j in range(0, self.problem_matrix.shape[1]):
                if i == j:
                    self.problem_matrix[i][j] = 1
        print(self.problem_matrix)
        return self.problem_matrix

    def load_shapes_colors_dict(self, transformed_shapes):
        for shape_name, (coords, color) in transformed_shapes.items():
            self.shapes_colors_dict[shape_name] = color

    def run(self, cube_open_vertices, shapes_names, transformed_shapes):
        
        self.load_shapes_colors_dict(transformed_shapes)

        self.problem_matrix = self.generate_problem_matrix(cube_open_vertices, shapes_names, transformed_shapes)




        # ones_rows = []
        # for sol_shape in sol_shapes:
        #     ones_row = []
        #     for (x,y,z) in sol_shape:
        #         ones_row.append(self.coords_dict[(x,y,z)])
        #     ones_rows.append(ones_row)
        # if self.problem_matrix


        from solution2x5x5 import sol_shapes
        # problem_matrix2 = self.generate_problem_matrix(cube_open_vertices, shapes_names, sol_shapes_dict)

        # problem_matrix2 = np.zeros((len(sol_shapes),    cube_open_vertices.shape[0] * \
        #                                                 cube_open_vertices.shape[1] * \
        #                                                 cube_open_vertices.shape[2]))
        # for row, placement in enumerate(sol_shapes):
        #     for coords in placement:
        #         col = self.coords_dict[coords]
        #         problem_matrix2[row][col] = 1
        # with np.printoptions(threshold=np.inf):
        #     print(np.array2string(problem_matrix2, max_line_width=np.inf))
        

        # zeros_check = np.zeros((1,              cube_open_vertices.shape[0] * \
        #                                         cube_open_vertices.shape[1] * \
        #                                         cube_open_vertices.shape[2]))

        # for i in range(0, problem_matrix2.shape[0]):
        #     for j in range(0, problem_matrix2.shape[1]):
        #         zeros_check[0][j] += problem_matrix2[i][j]

        # print(zeros_check)


        # for row1 in problem_matrix2:
        #     found = False
        #     for row2 in self.problem_matrix:
        #         if np.sum(np.all(row1 == row2, axis=0)):
        #             print('found')
        #             found = True
        #     if not found:
        #         print('not found')

        # dlx = DLX.from_matrix(problem_matrix2, self.callback)
        # ret = dlx.run(True)


        # self.problem_matrix = fake_matrix()
        dlx = DLX.from_matrix(self.problem_matrix, self.callback)
        ret = dlx.run(True)

