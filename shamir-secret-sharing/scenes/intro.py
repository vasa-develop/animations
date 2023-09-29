from manim import *

class Intro(Scene):
    def construct(self):
        eli5_text = MathTex(r"\text{ELI5}", color=BLUE).scale(3).shift(2*UP)
        topic_text = MathTex(r"\text{Shamir Secret Sharing and Lagrange Interpolation}", color=WHITE).shift(1*DOWN)
        self.play(DrawBorderThenFill(eli5_text), DrawBorderThenFill(topic_text), run_time=5)
        self.wait(2)

        #clear screen
        self.play(FadeOut(eli5_text), FadeOut(topic_text))