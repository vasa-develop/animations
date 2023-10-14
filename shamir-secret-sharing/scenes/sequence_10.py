from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence10(Scene):
    
    def construct(self):
        # TODO: Change the quadratic curve to use (1,4), (2,9), (3,16)

        # Create Axes
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 5],
            axis_config={"color": WHITE},
        )

        dot_1 = Dot(point=axes.c2p(0.3, 0.3), color=GRAY)
        dot_2 = Dot(point=axes.c2p(0.6, 0.6), color=GRAY)
        dot_3 = Dot(point=axes.c2p(0.9, 0.9), color=GRAY)
        dot_4 = Dot(point=axes.c2p(1.2, 1.2), color=GRAY)
        dot_5 = Dot(point=axes.c2p(1.5, 1.5), color=GRAY)
        dot_6 = Dot(point=axes.c2p(1.8, 1.8), color=GRAY)
        dot_7 = Dot(point=axes.c2p(2.1, 2.1), color=GRAY)
        dot_8 = Dot(point=axes.c2p(2.4, 2.4), color=GRAY)
        dot_9 = Dot(point=axes.c2p(2.7, 2.7), color=GRAY)
        dot_10 = Dot(point=axes.c2p(3, 3), color=GRAY)

        self.play(
            Create(axes),
            DrawBorderThenFill(dot_3),
            DrawBorderThenFill(dot_7)
        )
        self.add(axes, dot_3, dot_7)

        person_1 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(4.5*LEFT)
        person_2 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(3.5*LEFT)
        person_3 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.3).shift(3*UP).shift(2.5*LEFT).set_color(BLUE)
        person_4 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(1.5*LEFT)
        person_5 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*LEFT)
        person_6 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*RIGHT)
        person_7 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.3).shift(3*UP).shift(1.5*RIGHT).set_color(BLUE)
        person_8 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(2.5*RIGHT)
        person_9 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(3.5*RIGHT)
        person_10 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(4.5*RIGHT)

        self.play(
            Transform(dot_3, person_3),
            Transform(dot_7, person_7),
            DrawBorderThenFill(person_1),
            DrawBorderThenFill(person_2),
            DrawBorderThenFill(person_4),
            DrawBorderThenFill(person_5),
            DrawBorderThenFill(person_6),
            DrawBorderThenFill(person_8),
            DrawBorderThenFill(person_9),
            DrawBorderThenFill(person_10),
        )
        self.add(
            person_1,
            person_2,
            person_3,
            person_4,
            person_5,
            person_6,
            person_7,
            person_8,
            person_9,
            person_10
        )
        self.remove(dot_3, dot_7)

        self.play(
            person_10.animate.set_color(BLUE),
        )

        dot_0_1 = Dot(point=axes.c2p(0, 1), color=GREEN)
        dot_1_0 = Dot(point=axes.c2p(1, 0), color=GRAY)
        dot_2_1 = Dot(point=axes.c2p(2, 1), color=GRAY)

        dot_0_1_label = MathTex("(0,", "1", ")").set_color(WHITE).move_to(dot_0_1).shift(0.5*(UP + 1.2*RIGHT))
        dot_0_1_label[1].set_color(GREEN)
        dot_1_0_label = MathTex("(1,0)").set_color(WHITE).move_to(dot_1_0).shift(0.5*(DOWN + RIGHT))
        dot_2_1_label = MathTex("(2,1)").set_color(WHITE).move_to(dot_2_1).shift(0.5*(UP + LEFT))

        self.play(
            FadeOut(person_1),
            FadeOut(person_2),
            FadeOut(person_4),
            FadeOut(person_5),
            FadeOut(person_6),
            FadeOut(person_8),
            FadeOut(person_9),
            Transform(person_3, dot_0_1),
            Transform(person_7, dot_1_0),
            Transform(person_10, dot_2_1),
            Write(dot_0_1_label),
            Write(dot_1_0_label),
            Write(dot_2_1_label),
        )
        self.add(
            dot_0_1,
            dot_1_0,
            dot_2_1,
            dot_0_1_label,
            dot_1_0_label,
            dot_2_1_label,
        )
        self.remove(person_1, person_2, person_3, person_4, person_5, person_6, person_7, person_8, person_9, person_10)

        # Step 4: Draw a smooth curve through the points (0,1), (1,0), and (2,1)
        curve_points = [
            axes.c2p(0, 1),
            axes.c2p(0.3, 0.49),
            axes.c2p(0.6, 0.16),
            axes.c2p(0.9, 0.01),
            axes.c2p(1.2, 0.04),
            axes.c2p(1.5, 0.25),
            axes.c2p(1.8, 0.64),
            axes.c2p(2.1, 1.21),
            axes.c2p(2.4, 1.96),
            axes.c2p(2.7, 2.89),
            axes.c2p(3, 4),
        ]
        curve = VMobject()
        curve.set_points_as_corners([*curve_points])
        curve.make_smooth()
        curve.set_color(GREEN)
        
        self.play(Create(curve))
        self.add(curve)

        line_label = MathTex(r"\textbf{Secret Quadratic Curve}").set_color(WHITE).scale(0.7)
        self.play(Write(line_label))
        self.add(line_label)

        dot_1 = Dot(point=axes.c2p(0.3, 0.49), color=GRAY)
        dot_2 = Dot(point=axes.c2p(0.6, 0.16), color=GRAY)
        dot_3 = Dot(point=axes.c2p(0.9, 0.01), color=GRAY)
        dot_4 = Dot(point=axes.c2p(1.2, 0.04), color=GRAY)
        dot_5 = Dot(point=axes.c2p(1.5, 0.25), color=GRAY)
        dot_6 = Dot(point=axes.c2p(1.8, 0.64), color=GRAY)
        dot_7 = Dot(point=axes.c2p(2.1, 1.21), color=GRAY)
        dot_8 = Dot(point=axes.c2p(2.4, 1.96), color=GRAY)
        dot_9 = Dot(point=axes.c2p(2.7, 2.89), color=GRAY)
        dot_10 = Dot(point=axes.c2p(3, 4), color=GRAY)

        dot_group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5, dot_6, dot_7, dot_8, dot_9, dot_10)
        self.play(Transform(line_label, dot_group))
        self.add(dot_group)
        self.remove(line_label)

        person_1 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(4.5*LEFT)
        person_2 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(3.5*LEFT)
        person_3 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(2.5*LEFT)
        person_4 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(1.5*LEFT)
        person_5 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*LEFT)
        person_6 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*RIGHT)
        person_7 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(1.5*RIGHT)
        person_8 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(2.5*RIGHT)
        person_9 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(3.5*RIGHT)
        person_10 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(4.5*RIGHT)

        person_group = VGroup(person_1, person_2, person_3, person_4, person_5, person_6, person_7, person_8, person_9, person_10)

        self.play(
            Transform(dot_group, person_group),
            FadeOut(dot_0_1),
            FadeOut(dot_1_0),
            FadeOut(dot_2_1),
            FadeOut(dot_0_1_label),
            FadeOut(dot_1_0_label),
            FadeOut(dot_2_1_label),
            FadeOut(curve),
        )
        self.add(person_group)
        self.remove(dot_group)


        dot_3 = Dot(point=axes.c2p(1, 0), color=GRAY)
        dot_7 = Dot(point=axes.c2p(2, 1), color=GRAY)
        dot_10 = Dot(point=axes.c2p(3, 4), color=GRAY)
        dot_0 = Dot(point=axes.c2p(0, 1), color=GRAY)

        point_label_0_1 = MathTex("(0,", "1", ")").set_color(WHITE).move_to(axes.c2p(0, 1)).shift(0.5*(UP) + 0.7*(RIGHT))
        point_label_0_1[1].set_color(GREEN)  # Set y-coordinate "0" to green

        self.play(
            Transform(person_3, dot_3),
            Transform(person_7, dot_7),
            Transform(person_10, dot_10),
            FadeOut(person_1),
            FadeOut(person_2),
            FadeOut(person_4),
            FadeOut(person_5),
            FadeOut(person_6),
            FadeOut(person_8),
            FadeOut(person_9),
        )

        self.add(dot_3, dot_7, dot_10)
        self.remove(person_3, person_7, person_1, person_2, person_4, person_5, person_6, person_8, person_9, person_10)

        curve_points = [
            axes.c2p(0, 1),
            axes.c2p(0.3, 0.49),
            axes.c2p(0.6, 0.16),
            axes.c2p(0.9, 0.01),
            axes.c2p(1.2, 0.04),
            axes.c2p(1.5, 0.25),
            axes.c2p(1.8, 0.64),
            axes.c2p(2.1, 1.21),
            axes.c2p(2.4, 1.96),
            axes.c2p(2.7, 2.89),
            axes.c2p(3, 4),
        ]
        curve = VMobject()
        curve.set_points_as_corners([*curve_points])
        curve.make_smooth()
        curve.set_color(GREEN)
        self.play(Create(curve))
        self.add(curve)

        self.play(DrawBorderThenFill(dot_0), DrawBorderThenFill(point_label_0_1))
        self.add(dot_0, point_label_0_1)

        self.play(
            FadeOut(dot_10),
            FadeOut(dot_0),
            FadeOut(curve),
            FadeOut(point_label_0_1),
        )
        self.remove(dot_10, dot_0, curve, point_label_0_1)

        # Create initial points
        p1 = axes.c2p(0, 5)
        p2 = axes.c2p(1, 0)
        p3 = axes.c2p(2, 1)

        # Create dots for the points
        dot1 = Dot().set_color(GREEN).move_to(p1)
        dot2 = dot_3
        dot3 = dot_7

        # Create label for dot1
        dot1_label = MathTex("5").set_color(GREEN).next_to(dot1, UP, buff=0.1)

        # Create the curve
        curve = VMobject()
        curve.set_points_as_corners([p1, p2, p3])
        curve.make_smooth()

        # Add everything to the scene
        self.play(Create(dot1), Create(curve), Write(dot1_label))
        self.add(axes, dot1, curve, dot1_label)

        # Update function for the curve and label
        def update_curve_and_label(mob):
            new_p1 = mob.get_center()
            curve.set_points_as_corners([new_p1, p2, p3])
            curve.make_smooth()
            x, y = axes.p2c(new_p1)
            dot1_label.become(MathTex(f"{y:.2f}")).next_to(new_p1, UP, buff=0.1)

        # Animate the movement of dot1 to (0, 0)
        self.play(
            dot1.animate.move_to(axes.c2p(0, 0)),
            UpdateFromFunc(dot1, update_curve_and_label),
            run_time=5,
        )

        """
        TODO: Add animation for the following:

        To summarise, you need at least 3 secret shares to be able to
        recover the unique quadratic curve and hence the secret point.
        If you have less that 3 secret shares, you will not be able
        to recover the secret curve or the secret point.
        """

        self.wait(2)