from manimlib.imports import *

class ButterFly(Scene):
    def construct(self):
            butterfly = ParametricFunction(
            lambda t: np.array([
                (np.sin(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                (np.cos(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                0
            ]),
             t_min = 0, t_max = 40, step_size = 0.04, color = YELLOW
            )
            self.play(ShowCreation(butterfly),run_time=5)
