from manimlib.imports import *

class SquareRotations(Scene):
    def construct(self):
        sq = Square()
        sq.rotate(np.pi/4)
        self.play(GrowFromCenter(sq))
        self.wait(2)
