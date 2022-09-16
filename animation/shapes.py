from manim import * 
from polycubes_coords import shapes_ls
import json
# class PointMovingOnShapes(Scene):
#     def construct(self):
#         square = Square(color=BLUE) # Create a square
#         square.rotate(-3 * TAU / 8) # Rotate the square -3/8 * 2*PI 

#          # Play the animation of a square growing from the center
#         self.play(GrowFromCenter(square))

class PolycubeAssemble(ThreeDScene):
    def construct(self):

        loop_num = 3
        offset_gain = 5
        gr = VGroup()
        for idx, (shape, shape_name) in enumerate(shapes_ls[:]):
            x_offset = offset_gain * (idx % loop_num)
            y_offset = offset_gain * int(idx / loop_num)
            for coords, color in shape:
                
                new_cube = Cube()

                if color == 'r':
                    new_cube.set_color(RED)
                elif color == 'g':
                    new_cube.set_color(GREEN)
                elif color == 'y':
                    new_cube.set_color(YELLOW)
                
                print(coords)
                new_cube.set_x(coords[0] - x_offset).set_y(coords[1] - y_offset).set_z(coords[2])
                new_cube.set_height(1)
                gr.add(new_cube)

        self.play(GrowFromCenter(gr))
        self.wait()
        self.move_camera(zoom=0.4, frame_center=(-5,-8,0), phi=45 * DEGREES)
        self.wait()
        self.wait()
        self.wait()
        self.move_camera(theta=-45 * DEGREES)
        self.wait()
        self.wait()




class MoveToTest3(Scene):
    def construct(self):


        loop_num = 3
        offset_gain = 5
        gr = VGroup()
        gr2 = VGroup()
        for idx, (shape, shape_name) in enumerate(shapes_ls[:1]):
            for coords, color in shape:
                
                new_cube = Cube()
                new_cube2 = Cube()

                if color == 'r':
                    new_cube.set_color(RED)
                    new_cube2.set_color(RED)
                elif color == 'g':
                    new_cube.set_color(GREEN)
                    new_cube2.set_color(GREEN)
                elif color == 'y':
                    new_cube.set_color(YELLOW)
                    new_cube2.set_color(YELLOW)
                
                print(coords)
                new_cube.set_x(coords[0]).set_y(coords[1]).set_z(coords[2])
                new_cube2.set_x(coords[0]+5).set_y(coords[1]+5).set_z(coords[2])
                new_cube.set_height(1)
                new_cube2.set_height(1)
                gr.add(new_cube)
                gr2.add(new_cube2)

        self.play(GrowFromCenter(gr))
        self.move_camera(zoom=0.4)
        self.wait()
        self.play(Transform(gr, gr2))
        self.wait()
        self.play(Transform(gr2, gr))
        self.wait()
        # self.wait()
        # self.wait()
        # self.wait()
        # self.move_camera(theta=-45 * DEGREES)
        # self.wait()
        # self.wait()


class AssembleCubes(ThreeDScene):

    def construct(self):
        num_blocks = 12

        loop_num = 3
        offset_gain = 5
        shapes_gr = VGroup()
        for idx, (shape, shape_name) in enumerate(shapes_ls[:num_blocks]):
            shape_gr = VGroup()
            for coords, color in shape:
                
                new_cube = Cube()

                if color == 'r':
                    new_cube.set_color(RED)
                elif color == 'g':
                    new_cube.set_color(GREEN)
                elif color == 'y':
                    new_cube.set_color(YELLOW)
                
                print(coords)
                new_cube.set_x(coords[0]).set_y(coords[1]).set_z(coords[2])
                new_cube.set_height(1)
                shape_gr.add(new_cube)
            shapes_gr.add(shape_gr)



        self.move_camera(zoom=0.3)
        self.move_camera(phi=45 * DEGREES,theta=-45 * DEGREES)
        # self.play(GrowFromCenter(shapes_gr))

        start_animations = [
            FadeIn(shapes_gr),
            shapes_gr.animate.arrange_in_grid(),
        ]
        self.play(AnimationGroup(*start_animations))

        # self.play(shapes_gr.animate.arrange_in_grid())

        with open('origins.json', 'r') as f:
            origins = json.load(f)


        for sol_num, solution in enumerate(origins[:8], 2):
            shapes_gr2 = VGroup()
            for idx, (shape, shape_name)  in enumerate(shapes_ls[:num_blocks]):
                shape_gr = VGroup()
                color = solution[shape_name][1]
                for coords in solution[shape_name][0]:
                    
                    new_cube = Cube()

                    if color == 'r':
                        new_cube.set_color(RED)
                    elif color == 'g':
                        new_cube.set_color(GREEN)
                    elif color == 'y':
                        new_cube.set_color(YELLOW)
                    
                    # import pdb
                    # pdb.set_trace()
                    # print(coords)

                    new_cube.set_x(coords[0]).set_y(coords[1]).set_z(coords[2])
                    new_cube.set_height(1)
                    shape_gr.add(new_cube)
                shapes_gr2.add(shape_gr)

            self.remove(shapes_gr)
            
            text3d=Text("Solution: " + str(sol_num - 1))
            self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
            text3d.to_corner(UL)

            self.play(TransformFromCopy(shapes_gr, shapes_gr2))
            # self.play(Write(text3d))
            self.move_camera(theta=-45 * DEGREES * (sol_num * 2 - 1))
            # self.wait()
            self.remove(shapes_gr2)
            self.play(TransformFromCopy(shapes_gr2, shapes_gr))
            self.move_camera(theta=-45 * DEGREES * (sol_num * 2))
            self.remove(text3d)
            # self.wait()


