from manim import *

class Sequence15(Scene):
    
    def construct(self):

        # Create Axes
        axes = Axes(
            x_range=[0, 4],
            y_range=[0, 10],
            axis_config={"color": WHITE},
        )

        dot_1 = Dot().set_color(GREEN).move_to(axes.c2p(0, 1))
        dot_2 = Dot().set_color(GREEN).move_to(axes.c2p(1, 3))
        dot_3 = Dot().set_color(GREEN).move_to(axes.c2p(3, 7))
        dot_4 = Dot().set_color(GREEN).move_to(axes.c2p(3.5, 8))

        # Create label for y-intercept value
        dot_1_label = MathTex(r"(0,1)").next_to(dot_1, DOWN, buff=0.1).shift(0.3*DOWN)
        dot_2_label = MathTex(r"(1,3)").next_to(dot_2, DOWN, buff=0.1).shift(0.3*DOWN)
        dot_3_label = MathTex(r"(3,7)").next_to(dot_3, DOWN, buff=0.1).shift(0.3*DOWN)

        line_1 = Line(dot_1.get_center(), dot_4.get_center()).set_color(GREEN)
        line_1_label = MathTex(r"s(x) = 1 + 2x").set_color(GREEN).scale(1.2).shift(DOWN+RIGHT)

        self.play(Create(axes))
        self.add(axes)
        self.wait(0.5)
        
        self.play(Create(line_1), Write(line_1_label))
        self.add(axes, line_1)
        self.wait(0.5)

        self.play(
            DrawBorderThenFill(dot_3),
            Write(dot_3_label),
        )
        self.add(dot_3, dot_3_label)
        self.wait(0.5)

        self.play(
            DrawBorderThenFill(dot_2),
            Write(dot_2_label),
        )
        self.add(dot_2, dot_2_label)
        self.wait(0.5)


        self.play(
            FadeOut(dot_2),
            FadeOut(dot_2_label),
        )
        self.remove(dot_2, dot_2_label)
        self.wait(0.5)


        def g_x(x):
            return (5/3)*x + 2

        _dot_1 = Dot().set_color(RED).move_to(axes.c2p(0, g_x(0)))
        _dot_2 = Dot().set_color(RED).move_to(axes.c2p(3.5, g_x(3.5)))
        _dot_3 = Dot().set_color(RED).move_to(axes.c2p(1, g_x(1)))

        # Create label for y-intercept value
        _dot_1_label = MathTex(r"(0,2)").next_to(dot_1, UP, buff=0.1).set_color(RED).shift(UP+RIGHT)
        _dot_3_label = MathTex(r"(1,2+\frac{5}{3})").next_to(_dot_3, UP, buff=0.1).set_color(RED).shift(0.3*UP)

        line_2 = Line(_dot_1.get_center(), _dot_2.get_center()).set_color(RED)
        line_2_label = MathTex(r"s(x) = 2 + \frac{5}{3}x").set_color(RED).scale(1.2).shift(1.5*(UP))

        self.play(
            DrawBorderThenFill(_dot_1),
            Write(_dot_1_label),
        )
        self.wait(0.5)

        self.play(Create(line_2))
        self.wait(0.5)
        self.play(Write(line_2_label))
        self.wait(0.5)
        
        self.add(_dot_1, _dot_1_label, line_2, line_2_label)

        self.play(
            DrawBorderThenFill(_dot_3),
            Write(_dot_3_label),
        )
        self.add(_dot_3, _dot_3_label)
        self.wait(0.5)


        self.play(
            Indicate(_dot_3_label, scale_factor=1.1)
        )
        self.wait(0.5)

        self.play(
            Indicate(_dot_1_label, scale_factor=1.1)
        )

        self.play(
            Indicate(dot_3_label, scale_factor=1.1)
        )


        self.wait(2)