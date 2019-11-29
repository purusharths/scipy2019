from manimlib.imports import *

def confromal_transofrm(point):
    z = R3_to_complex(point)
    return complex_to_R3(np.power(z,2)/2)

class ConformTest(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Square(color=RED)
        self.add(grid)
        self.play(ShowCreation(circle))
        grid.prepare_for_nonlinear_transform()
        self.play(grid.apply_function, confromal_transofrm, circle.apply_function, confromal_transofrm, run_time=3)
        self.wait(2)
