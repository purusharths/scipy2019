from manimlib.imports import *

class TestCircle(Scene):
    def construct(self):
        circle = Circle(radius=3)
        square = Square()
        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        self.wait(2)
