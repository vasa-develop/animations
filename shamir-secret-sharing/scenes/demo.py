from manim import *

class DataRecovery(Scene):
    def construct(self):
        cd = Circle(radius=2).set_fill(color=WHITE, opacity=0.5)
        cd_scratch = Line(cd.point_from_proportion(0.25), cd.point_from_proportion(0.75)).set_color(RED)
        qr_code = Square(side_length=2).set_fill(color=BLACK, opacity=0.85).shift(RIGHT*4)
        qr_damage = Cross(qr_code.get_center(), stroke_width=6).set_color(RED)
        
        self.play(Create(cd), Create(qr_code))
        self.play(Create(cd_scratch), Create(qr_damage))