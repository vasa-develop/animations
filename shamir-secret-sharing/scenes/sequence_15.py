from manim import *

class Sequence15(Scene):
    
    def construct(self):
        """
        TODO: Add animation for 
        
        In order to solve this issue, we can try to update our polynomial
        such that it does not involve any fractional values.
        """

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
        # self.play(
        #     Create(dot_1),
        #     Create(dot_2),
        #     Write(dot_1_label),
        #     Write(dot_2_label),
        # )
        self.play(Create(line_1), Write(line_1_label))
        self.add(axes, line_1)

        self.play(
            DrawBorderThenFill(dot_3),
            Write(dot_3_label),
        )
        self.add(dot_3, dot_3_label)

        self.play(
            DrawBorderThenFill(dot_2),
            Write(dot_2_label),
        )
        self.add(dot_2, dot_2_label)


        self.play(
            FadeOut(dot_2),
            FadeOut(dot_2_label),
        )
        self.remove(dot_2, dot_2_label)


        def g_x(x):
            return (5/3)*x + 2

        _dot_1 = Dot().set_color(RED).move_to(axes.c2p(0, g_x(0)))
        _dot_2 = Dot().set_color(RED).move_to(axes.c2p(3.5, g_x(3.5)))
        _dot_3 = Dot().set_color(RED).move_to(axes.c2p(1, g_x(1)))

        # Create label for y-intercept value
        dot_1_label = MathTex(r"(0,2)").next_to(dot_1, UP, buff=0.1).set_color(RED).shift(UP+RIGHT)
        dot_3_label = MathTex(r"(1,2+\frac{5}{3})").next_to(_dot_3, UP, buff=0.1).set_color(RED).shift(0.3*UP)

        line_2 = Line(_dot_1.get_center(), _dot_2.get_center()).set_color(RED)
        line_2_label = MathTex(r"s(x) = 2 + \frac{5}{3}x").set_color(RED).scale(1.2).shift(1.5*(UP))

        self.play(
            DrawBorderThenFill(_dot_1),
            Write(dot_1_label),
        )

        self.play(Create(line_2))
        self.play(Write(line_2_label))
        
        self.add(_dot_1, dot_1_label, line_2, line_2_label)

        self.play(
            DrawBorderThenFill(_dot_3),
            Write(dot_3_label),
        )
        self.add(_dot_3, dot_3_label)



        """
        TODO: Add animation for

        The problem with this line is that at x = 1, the value is 2 + 5/3. Now, remember that we decided that we will be only working with polynomials that do not have a fractional value. But as we can see, if we assume that (0,2) is a secret share, it violates our rule of no fractional values. This means that (0,2) cannot be a valid secret.

        So, even with just the knowledge of a single secret share (3,7), we are able to rule out the possibility of (0,2) being a possible secret. This means that we no longer have perfect secrecy as we are able to deduce some information about the secret without having threshold number of shares.

        What we can observe here is that even if we try to avoid the fractional values in our secret sharing system, it can still affect the security guarantees of our secret sharing system.

        What would solve this issue for us is if we can figure out a new form of arithmetic where we can make sure that all operations such as addition, subtraction, multiplication, and division always lead to an integer?

        """



        self.wait(2)