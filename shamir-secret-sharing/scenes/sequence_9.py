from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence9(Scene):
    
    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 5.5],
            axis_config={"color": WHITE},
        )
        labels = axes.get_axis_labels(
            MathTex(r"\textbf{x}").scale(0.7), 
            MathTex(r"\textbf{y}").scale(0.7)
        )

        # Create a green dot at (0, 9)
        dot = Dot().set_color(GREEN).move_to(axes.c2p(0, 5))

        # Create label for y-intercept value
        label = MathTex("secret = 5.00").next_to(dot, RIGHT, buff=0.1)

        # Add Axes and dot to the scene
        self.play(Create(axes), Create(labels), Create(dot), Write(label))
        self.add(axes, labels, dot, label)
        self.wait(0.5)

        # Move dot to (0, 0)
        def update_label(mob):
            x, y = axes.p2c(mob.get_center())
            label.become(MathTex(f"secret = {y:.2f}").next_to(mob, RIGHT , buff=0.1))

        self.play(
            dot.animate.move_to(axes.c2p(0, 0)),
            UpdateFromFunc(dot, update_label),
            run_time=5,
        )

        point_label_0_0 = MathTex("(0,", "0", ")").set_color(WHITE).move_to(axes.c2p(0, 0)).shift(0.5*(DOWN + RIGHT))
        point_label_0_0[1].set_color(GREEN)  # Set y-coordinate "0" to green

        self.play(Transform(label, point_label_0_0))
        self.add(point_label_0_0)
        self.remove(label)
        self.wait(0.5)

        randomness_text = MathTex(r"\textbf{Randomness}", color=WHITE).scale(1.2)
        self.play(DrawBorderThenFill(randomness_text))
        self.add(randomness_text)

        point_label_1_1 = MathTex("(1,1)").set_color(WHITE).move_to(axes.c2p(1, 1)).shift(0.5*(DOWN + RIGHT))
        dot_1_1 = Dot(point=axes.c2p(1, 1), color=GRAY)
        self.play(DrawBorderThenFill(dot_1_1), Transform(randomness_text, point_label_1_1))
        self.add(dot_1_1, point_label_1_1)
        self.remove(randomness_text)
        self.wait(0.5)

        line = Line(dot.get_center(), dot_1_1.get_center() + 2*(dot_1_1.get_center() - dot.get_center())).set_color(GREEN)
        line_label = MathTex(r"\textbf{Secret Line}").set_color(WHITE).scale(1.2)

        self.play(Create(line), DrawBorderThenFill(line_label))
        self.add(line, line_label)
        self.wait(0.5)

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

        dot_group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5, dot_6, dot_7, dot_8, dot_9, dot_10)
        self.play(Transform(line_label, dot_group))
        self.add(dot_group)
        self.remove(line_label)
        self.wait(0.5)


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
            FadeOut(dot),
            FadeOut(dot_1_1),
            FadeOut(line),
            FadeOut(point_label_0_0),
            FadeOut(point_label_1_1)
        )
        self.add(person_group)
        self.remove(dot_group)
        self.wait(0.5)

        dot_3 = Dot(point=axes.c2p(0.9, 0.9), color=GRAY)
        dot_7 = Dot(point=axes.c2p(2.1, 2.1), color=GRAY)
        dot_0 = Dot(point=axes.c2p(0, 0), color=GRAY)

        point_label_0_0 = MathTex("(0,", "0", ")").set_color(WHITE).move_to(axes.c2p(0, 0)).shift(0.5*(DOWN + RIGHT))
        point_label_0_0[1].set_color(GREEN)  # Set y-coordinate "0" to green

        self.play(
            Transform(person_3, dot_3),
            Transform(person_7, dot_7),
            FadeOut(person_1),
            FadeOut(person_2),
            FadeOut(person_4),
            FadeOut(person_5),
            FadeOut(person_6),
            FadeOut(person_8),
            FadeOut(person_9),
            FadeOut(person_10),
        )

        self.add(dot_3, dot_7)
        self.remove(person_3, person_7, person_1, person_2, person_4, person_5, person_6, person_8, person_9, person_10)
        self.wait(0.5)

        dot_1_1 = Dot(point=axes.c2p(1, 1), color=GRAY)
        dot = Dot().set_color(GREEN).move_to(axes.c2p(0, 0))
        line = Line(dot.get_center(), dot_1_1.get_center() + 2*(dot_1_1.get_center() - dot.get_center())).set_color(GREEN)
        
        self.play(Create(line))
        self.play(DrawBorderThenFill(dot_0), DrawBorderThenFill(point_label_0_0))
        self.add(line, dot_0, point_label_0_0)
        self.wait(0.5)

        self.play(
            FadeOut(dot_3),
            FadeOut(dot_0),
            FadeOut(line),
            FadeOut(point_label_0_0),
        )
        self.remove(dot_3, dot_0, line, point_label_0_0)
        self.wait(0.5)


        # Create a dot at (0, 5)
        end_dot = Dot().set_color(GREEN).move_to(axes.c2p(0, 5))

        # Create a line from (5, 5) to (0, 5)
        line = Line(axes.c2p(2.1, 2.1), axes.c2p(0, 5), color=RED)

        # Create label for line's end point
        end_dot_label = MathTex("secret = 5.00").set_color(GREEN).next_to(line.get_end(), DOWN + RIGHT, buff=0.1)

        # Add Axes, dot, and line to the scene
        self.play(
            Create(end_dot),
            Write(end_dot_label),
            Create(line)
        )
        self.add(end_dot, end_dot_label, line)
        self.wait(0.5)

        # Move point on x=0 from y=5 to y=0
        def update_dot_label(mob):
            x, y = axes.p2c(mob.get_end())
            end_dot_label.become(MathTex(f"secret = {y:.2f}").set_color(GREEN)).next_to(mob.get_end(), DOWN + RIGHT, buff=0.1)
            end_dot.move_to(mob.get_end())
            self.add(end_dot_label, end_dot)

        self.play(
            line.animate.put_start_and_end_on(axes.c2p(2.1, 2.1), axes.c2p(0, 0)),
            UpdateFromFunc(line, update_dot_label),
            run_time=5,
        )

        self.play(
            FadeOut(line),
            FadeOut(end_dot),
            FadeOut(end_dot_label),    
        )
        self.remove(line, end_dot, end_dot_label)
        self.wait(0.5)

        dot_3 = Dot(point=axes.c2p(0.9, 0.9), color=GRAY)
        dot_0 = Dot(point=axes.c2p(0, 0), color=GRAY)

        point_label_0_0 = MathTex("(0,", "0", ")").set_color(WHITE).move_to(axes.c2p(0, 0)).shift(0.5*(DOWN + RIGHT))
        point_label_0_0[1].set_color(GREEN)  # Set y-coordinate "0" to green

        dot_1_1 = Dot(point=axes.c2p(1, 1), color=GRAY)
        dot = Dot().set_color(GREEN).move_to(axes.c2p(0, 0))
        line = Line(dot.get_center(), dot_1_1.get_center() + 2*(dot_1_1.get_center() - dot.get_center())).set_color(GREEN)

        self.play(DrawBorderThenFill(dot_3))
        self.play(Create(line), DrawBorderThenFill(dot_0), DrawBorderThenFill(point_label_0_0))
        self.add(dot_3, dot_0, point_label_0_0, line)
        self.wait(0.5)
        
        self.play(FadeOut(line), FadeOut(point_label_0_0))
        self.remove(line, point_label_0_0)

        self.wait(2)