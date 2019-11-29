from manimlib.imports import *
import numpy as np
class FancyCurve(Scene):
    def construct(self):
        a = 1
        b = -2
        curve = ParametricFunction(
                    lambda t: np.array([
                    (a+b)*np.cos(TAU*t) + b*np.cos(TAU*(a + b)/b*t),
                    (a + b)*np.sin(TAU*t) + b*np.sin(TAU*(a + b)/b*t),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        curve1 = ParametricFunction(
                    lambda t: np.array([
                    ((a+b)*np.cos(-TAU*t) + b*np.cos(-TAU*(a + b)/b*t)),
                    ((a + b)*np.sin(-TAU*t) + b*np.sin(-TAU*(a + b)/b*t)),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        self.play(ShowCreation(curve))
        self.play(ShowCreation(curve1))
        self.wait(2)
