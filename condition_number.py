from manimlib.imports import *

class CondNumb(LinearTransformationScene, ZoomedScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 3,
        "zoomed_camera_frame_starting_position": 0.1*UP+0.1*RIGHT,
        "zoom_factor": 0.01,
    }

    def setup(self):
        ZoomedScene.setup(self)
        LinearTransformationScene.setup(self)

    def construct(self):
        
        transform = [1, 1], [1,1.01]
        self.setup()
        self.wait(1)
        self.activate_zooming(animate=True)
        self.apply_matrix(transform)
        self.wait(2)