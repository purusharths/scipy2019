from manimlib.imports import *

def pendulum_vector_field_func(point, a1=-0.5, a2 = 2, b0=0.000088889, kd=3, kp=3):
    theta, omega = point[:2]
    a_1 = a1 - b0*kd
    a_2 = a2 - b0*kp
    return np.array([
        omega,
        (a_1 * omega) + (a_2 *  np.sin(theta)),
        0,
    ])


class InvertedPendulumEquation(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels(x_label_tex=r"\theta", y_label_tex=r"\dot{\theta}"))
        self.add(plane)
        vector_field = VectorField( pendulum_vector_field_func )
        self.add(vector_field)
        self.create_stream_lines(pendulum_vector_field_func)
        self.wait(2)

    def create_stream_lines(self, func, time=5):
        lines = StreamLines(
            func,
            virtual_time=3,
            min_magnitude=0,
            max_magnitude=2,
            dt=0.1,
            color_by_magnitude=True,
        )
        self.add(AnimatedStreamLines(
               lines,
               line_anim_class=ShowPassingFlash,
               flow_time = 5,
        ))
