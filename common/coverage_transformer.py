#transforms the polycube problem into a coverage matrix

import numpy as np

class CoverageTransformer():

    def __init__(self, same_shapes):
        self.problem_matrix = None
        self.coords_dict = {}
        self.shapes_dict = {}
        self.cntr_shapes_dict = {}
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

            if x >= cube_open_vertices.shape[0] or y >= cube_open_vertices.shape[1] or z >= cube_open_vertices.shape[2] or \
                    x < 0 or y < 0 or z < 0 or not cube_open_vertices[x][y][z]:
                #invalid placement
                return False, None

            # used_coords.append((x,y,z))
            used_coords.append((x,y,z))

        return True, used_coords

    def generate_problem_matrix(self, cube_open_vertices, shapes_names, transformed_shapes, same_shapes=False):
        
        #load_shapes_colors_dict
        for shape_name, (coords, color) in transformed_shapes.items():
            self.shapes_colors_dict[shape_name] = color
            self.shapes_colors_dict[color] = shape_name

        cntr = 0

        if not self.same_shapes:
            #Number all polycubes with unique ID
            for shape_name in shapes_names:
                self.shapes_dict[shape_name] = cntr
                self.cntr_shapes_dict[cntr] = shape_name
                cntr += 1

        #Number all 3d box coords with unique ID in dict
        for x in range(cube_open_vertices.shape[0]):
            for y in range(cube_open_vertices.shape[1]):
                for z in range(cube_open_vertices.shape[2]):
                    self.coords_dict[(x,y,z)] = cntr
                    self.coords_dict[cntr] = (x,y,z)
                    cntr += 1

        placements = []
        for num, shape_name in enumerate(shapes_names):
            print(shape_name, num)
            for x in range(cube_open_vertices.shape[0]):
                for y in range(cube_open_vertices.shape[1]):
                    for z in range(cube_open_vertices.shape[2]):
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
        #assign unique matrix row for each entry
        for row, (shape_name, used_coords) in enumerate(placements):
            if not self.same_shapes:
                #assign unique shape entry
                self.problem_matrix[row][self.shapes_dict[shape_name]] = 1
            #assign unique coords entry
            for coords in used_coords:
                col = self.coords_dict[coords]

                self.problem_matrix[row][col] = 1

        #remove duplicate entries
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


    #convert solution to shapes list
    def rows_to_shapes(self, result, print_shape_name=False):

        if print_shape_name:
            origins = {}
        else:
            origins = []
        # shapes_dict_swap = {v: k for k, v in self.shapes_dict.items()}
        # coords_dict_swap = {v: k for k, v in self.coords_dict.items()}
        for color_i, res in enumerate(result):
            shape_coords = []
            row = self.problem_matrix[res]

            if not self.same_shapes:
                #get shape
                for i in range(len(self.shapes_dict)):
                    if row[i] != 0:
                        shape_name = self.cntr_shapes_dict[i]

            #get coords
            for i in range(len(self.shapes_dict), self.problem_matrix.shape[1]):
                if row[i] != 0:
                    shape_coords.append(self.coords_dict[i])

            if not self.same_shapes:
                if print_shape_name:
                    origins[shape_name] = (shape_coords, self.shapes_colors_dict[shape_name])
                else:
                    origins.append((shape_coords, self.shapes_colors_dict[shape_name]))
            else:
                colors = ('r','b','y')
                origins.append((shape_coords, colors[color_i % len(colors)]))

        return origins

    def generate_problem_matrices(self, cube_open_vertices, shapes_names, transformed_shapes, same_shapes=False):
        
        #load_shapes_colors_dict
        for shape_name, (coords, color) in transformed_shapes.items():
            self.shapes_colors_dict[shape_name] = color

        cntr = 0

        # if not self.same_shapes:
        #     #Number all polycubes with unique ID
        #     for shape_name in shapes_names:
        #         self.shapes_dict[shape_name] = cntr
        #         cntr += 1

        #Number all 3d box coords with unique ID in dict
        for x in range(cube_open_vertices.shape[0]):
            for y in range(cube_open_vertices.shape[1]):
                for z in range(cube_open_vertices.shape[2]):
                    self.coords_dict[(x,y,z)] = cntr
                    cntr += 1


        placements = {}
        for num, shape_name in enumerate(shapes_names):
            print(shape_name, num)
            placements[shape_name] = []
            for x in range(cube_open_vertices.shape[0]):
                for y in range(cube_open_vertices.shape[1]):
                    for z in range(cube_open_vertices.shape[2]):
                        #get color by first transformation
                        (transformed_shapes_list, color) = transformed_shapes[shape_name]
                        for t in transformed_shapes_list:
                            valid_placement, used_coords = self.add(t, cube_open_vertices, (x,y,z))
                            if not valid_placement:
                                continue
                            placements[shape_name].append(used_coords)
        

        problem_matrices = {}
        for shape_name in shapes_names:
            problem_matrix = np.zeros((len(placements[shape_name]), \
                                                            cube_open_vertices.shape[0] * \
                                                            cube_open_vertices.shape[1] * \
                                                            cube_open_vertices.shape[2]))
            for row, placement in enumerate(placements[shape_name]):
                for coords in placement:
                    col = self.coords_dict[coords]

                    problem_matrix[row][col] = 1


            problem_matrix = np.unique(problem_matrix, axis=0)
            problem_matrices[shape_name] = problem_matrix


        #remove duplicate entries

        # print('after unique:', self.problem_matrix)

        with np.printoptions(threshold=np.inf):
            for shape_name in shapes_names:
                print(np.array2string(problem_matrices[shape_name], max_line_width=np.inf))
                print('shape_name',shape_name)
                print('problem_matrix',problem_matrices[shape_name].shape)

        for shape_name in shapes_names:
            zeros_check = np.zeros((1, cube_open_vertices.shape[0] * \
                                        cube_open_vertices.shape[1] * \
                                        cube_open_vertices.shape[2]))
            matrix = problem_matrices[shape_name]
            for i in range(0, matrix.shape[0]):
                for j in range(0, matrix.shape[1]):
                    zeros_check[0][j] += matrix[i][j]
            print('zeros_check',zeros_check)

        return problem_matrices
