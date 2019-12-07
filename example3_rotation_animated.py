from manimlib.imports import *

class SquareRotations(Scene):
    def construct(self):
        sq = Square()
        self.play(ApplyMethod(sq.rotate, np.pi/4))
        self.wait(2)
