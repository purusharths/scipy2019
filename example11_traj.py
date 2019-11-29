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

class InvertedPendulumSimulationWithPendulum(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels(x_label_tex=r"\theta", y_label_tex=r"\dot{\theta}"))
        self.add(plane)

        self.vector_field = VectorField( pendulum_vector_field_func )
        self.vector_field.sort(get_norm)
        self.add(self.vector_field)
        
        self.show_trajectory()

    def show_trajectory(self):
        dot1 = Dot(color=PINK)
        trajectories_list = [2*LEFT+3*UP]
        traj1 = self.get_trajectory(trajectories_list[0], duration=60)
        self.add(traj1, dot1)
        #anims = [[ShowCreation(traj1, rate_func=linear),  UpdateFromFunc(dot1, lambda d: d.move_to(traj1.points[-1]))]];self.play(*anims[0], run_time=63)
        self.play(ShowCreation(traj1, rate_func=linear),  UpdateFromFunc(dot1, lambda d: d.move_to(traj1.points[-1])))

    def get_trajectory(self, starting_position, duration, dt=0.1, added_steps=100):
        field = self.vector_field
        traj = VMobject()
        traj.start_new_path(starting_position)
        for x in range(int(duration / dt)): # duration = iterations for trajectory
            last_point = traj.points[-1] 
            for y in range(added_steps):
                dp_dt = field.func(last_point) # follow vector field
                last_point += dp_dt * dt / added_steps
            traj.add_smooth_curve_to(last_point)
        traj.make_smooth() # smoothning
        traj.set_stroke(WHITE, 2)
        return traj
