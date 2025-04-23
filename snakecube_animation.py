from manim import *
import numpy as np

class SnakeCubeVisualization(ThreeDScene):
    def construct(self):
        self.unsolved_state = list("RUUURURURURURUURUUURURUUURRURURURRUURURURURURRURRURRURRRURUURRUU")
        self.solved_state = list("RBBBLURFLDFUFRRDBBBURDFFFUUBDBLULLFFURDRURBLDDLUULBBDRRRFULLBRRR")

        self.cubes = self.create_snake_cube(self.unsolved_state)
        for cube in self.cubes:
            self.add(cube)

        #need pause at beginning to set camera
        self.wait(1)
        # Initial camera setup (Zoomed Out)
        self.move_camera(zoom=0.25, frame_center=[9., 9., 0.])

        self.wait(2)
        self.move_camera(zoom=0.5, frame_center=[0., 0., 0.],
            phi=-115*DEGREES, theta=-45*DEGREES)
            # phi=135*DEGREES, theta=-45*DEGREES)
        # self.move_camera(phi=60*DEGREES,
        #                  theta=135*DEGREES)
        for step in range(len(self.solved_state)):
        # for step in range(6):
            if step == 5:
                self.move_camera(phi=-45*DEGREES, theta=-45*DEGREES)
                self.wait(0.25)
            if step == 16:
                self.move_camera(phi=-135*DEGREES, theta=-45*DEGREES)
                self.wait(0.25)
            #if any difference
            if self.update_snake(step):
                self.wait(0.25)

        self.wait(3)

    def create_snake_cube(self, state):
        position = np.array([0.0, 0.0, 0.0])
        cubes = []
        distance_between_cubes = 0.6

        for index, move in enumerate(state):
            cube = self.create_single_cube(position, index)
            cubes.append(cube)
            position += self.get_direction_vector(move) * distance_between_cubes

        return cubes

    def create_single_cube(self, position, index):
        cube_color = "#8B4513" if index % 2 == 0 else "#F5F5DC"
        cube = Cube(side_length=0.5)
        cube.set_fill(cube_color, opacity=1)
        cube.set_stroke(WHITE, width=0.5)
        cube.move_to(position)
        return cube

    def get_direction_vector(self, move):
        move_map = {
            'R': np.array([1, 0, 0]),
            'U': np.array([0, 1, 0]),
            'L': np.array([-1, 0, 0]),
            'D': np.array([0, -1, 0]),
            'B': np.array([0, 0, -1]),
            'F': np.array([0, 0, 1]),
        }
        return move_map.get(move, np.array([0, 0, 0]))

    def update_snake(self, step):
        current_move = self.solved_state[step]
        old_move = self.unsolved_state[step]
        if current_move == old_move:
            return False
        # Only replace occurrences of old_move AFTER the current step index
        self.unsolved_state = (
            self.unsolved_state[: step]
            + [
                current_move if move == old_move else move
                for move in self.unsolved_state[step:]
            ]
        )
        print('step:', step)
        print('current_move:', current_move)
        print('old_move:', old_move)
        print('solved_state:', self.solved_state)
        print('unsolved_state:', self.unsolved_state)
        new_cubes = self.create_snake_cube(self.unsolved_state)
        breakpoint()
        animations = [
            Transform(self.cubes[i], new_cubes[i]) for i in range(len(self.cubes))
        ]

        self.play(*animations)
        return True