from manim import *

class VectorScene(Scene):
    def construct(self):
        plane = NumberPlane()
        v = Vector([3,4], color=BLUE)

        self.play(Create(plane))
        self.play(GrowArrow(v))
        self.wait()

class RotationScene(Scene):
    def construct(self):
        plane = NumberPlane()
        v = Vector([2,1], color=BLUE)

        self.play(Create(plane))
        self.play(GrowArrow(v))
        self.play(Rotate(v, angle=PI/2))
        self.wait()