from manimlib.imports import *

c = 2
a = 0.7
class CreateTorous(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # create a threeD axis
        torus = ParametricSurface(
            lambda u, v: np.array([
                (c + a * np.cos(TAU * v)) * np.cos(TAU*u) ,
                (c + a * np.cos(TAU * v)) * np.sin(TAU*u) ,
                a * np.sin(TAU*v)
            ]),
            resolution=(32, 32)).fade(0.5)
        self.set_camera_orientation(phi= 55 * DEGREES)
        self.play(ShowCreation(torus), run_time=5)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)
        
