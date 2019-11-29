from manimlib.imports import *

def add_plane(self):
    plane = NumberPlane(color=RED)
    self.add(plane)
    return plane

def initialize_vector_field(self, diff_func, passive=False):
    self.vector_field = VectorField(
        diff_func,  
    )
    self.vector_field.sort(get_norm)
    #self.play(ShowCreation(self.vector_field), run_time=2)
    if not passive:
        self.add(self.vector_field)
    return self.vector_field

def create_stream_lines(self, func, time=5, ret=False):
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

def show_trajectory(self, time=60):
    start_points = [1*LEFT, 
                    1*LEFT+0.1*UP, #5*RIGHT+3*DOWN,
                    2*RIGHT+0.5*DOWN,
                    0.01*UP+0.01*RIGHT]
    dot1 = Dot(color=PINK)
    dot2 = Dot(color=RED)
    dot3 = Dot(color=PURPLE_A)
    dot4 = Dot(color=ORANGE)
    traj1 = get_trajectory(self, start_points[0], duration=time)
    traj2 = get_trajectory(self, start_points[1], duration=time)
    traj3 = get_trajectory(self, start_points[2], duration=time)
    traj4 = get_trajectory(self, start_points[3], duration=time)
    anims = [[ShowCreation(traj1, rate_func=linear),  UpdateFromFunc(dot1, lambda d: d.move_to(traj1.points[-1]))],
                [ShowCreation(traj2, rate_func=linear),  UpdateFromFunc(dot2, lambda d: d.move_to(traj2.points[-1]))],
                [ShowCreation(traj3, rate_func=linear),  UpdateFromFunc(dot3, lambda d: d.move_to(traj3.points[-1]))],
                [ShowCreation(traj4, rate_func=linear),  UpdateFromFunc(dot4, lambda d: d.move_to(traj4.points[-1]))],
    ]
    self.add(traj1, dot1); self.add(traj2, dot2); self.add(traj3, dot3); self.add(traj4, dot4)
    self.play(*anims[0], *anims[1], *anims[2], *anims[3], run_time=20)
    self.wait(2)

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

def show_titles(self, t, l1, l2):
    title = TextMobject(t).move_to(3.5*UP).scale(1.2)
    title.add_background_rectangle()
    lambdas = r"$\lambda_1 = {}$ \\ $\lambda_2 = {}$".format(l1, l2)
    eigenvals = TextMobject(lambdas, color=YELLOW).move_to(5*LEFT+3*UP).scale(0.74)
    eigenvals.add_background_rectangle()
    self.play(ShowCreation(title), ShowCreation(eigenvals))
    self.wait(2)
    

######## params #########

def stable_node(point):
    x, y = point[:2]
    return np.array([
        -1*x+3*y,
        -1*x-5*y,
        0,
    ])

class StableNode(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, stable_node)
        self.add(self.vector_field)
        create_stream_lines(self, stable_node)
        show_titles(self, "Stable Node", "-0.44948974,", "4.44948974")
        #show_dots_movement(self, node_convergent, 6)
        show_trajectory(self, time=30)
        self.wait(10)
## ------------------------
def saddle_point(point):
    return np.array([
        1*point[0]-2*point[1],
        0*point[0]-1*point[1],
        0,
    ])

class SaddlePoint(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, saddle_point)
        self.add(self.vector_field)
        create_stream_lines(self, saddle_point)
        show_titles(self, "Saddle Point", "1,", "-2")
        show_trajectory(self)
        self.wait(8)
## ------------------------
def unstable_point(point):
    return np.array([
        1*point[0]+1*point[1],
        0*point[0]+2*point[1],
        0,
    ])

class UnstablePoint(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, unstable_point)
        self.add(self.vector_field)
        create_stream_lines(self, unstable_point)
        show_titles(self, "Unstable Point", "1,", "2")
        show_trajectory(self, time=4)
        self.wait(5)
## ------------------------
def pure_imag_eig(point):
    return np.array([
        2*point[0]+5*point[1],
        -8*point[0]-2*point[1],
        0,
    ])

class PureImagComplexEige(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, pure_imag_eig)
        self.add(self.vector_field)
        create_stream_lines(self, pure_imag_eig)
        show_titles(self, "Purely Imaginary Eigenvalues", "0.+5.196i,", "0.-5.196i")
        show_trajectory(self, time=4)
        self.wait(10)
## -------------------------------
def complex_eig_unstable(point):
    return np.array([
        3*point[0]-13*point[1],
        5*point[0]+1*point[1],
        0,
    ])
    
class UnStableComplexEigs(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, complex_eig_unstable)
        self.add(self.vector_field)
        create_stream_lines(self, complex_eig_unstable)
        show_titles(self, "Complex Eigenvalues - Unstable", "2+8i,", "2-8i")
        show_trajectory(self)
        self.wait(10)
## -------------------------------
def complex_eig_stable(point):
    return np.array([
        -3*point[0]-13*point[1],
        5*point[0]-1*point[1],
        0,
    ])
    
class StableComplexEigs(Scene):
    def construct(self):
        add_plane(self)
        self.vector_field = initialize_vector_field(self, complex_eig_stable)
        self.add(self.vector_field)
        create_stream_lines(self, complex_eig_stable)
        show_titles(self, "Complex Eigenvalues - Stable", "-2+8i", "-2-8i")
        show_trajectory(self)
        self.wait(10)
## -------------------------------
