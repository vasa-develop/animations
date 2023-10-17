from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence11(Scene):
    
    def construct(self):
        """
        NOTE: We can skip this part.
        TODO: Add animation for the following:

        This system works for cases where you want any 3 people out
        of a group to recover a secret. What if we want to create a
        system where we want any 4 people out of a group to recover
        a secret?
        """

        person_1 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(4.5*LEFT)
        person_2 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(3.5*LEFT)
        person_3 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(2.5*LEFT)
        person_4 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(1.5*LEFT)
        person_5 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*LEFT)
        person_6 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(0.5*RIGHT)
        person_7 = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.3).shift(3*UP).shift(1.5*RIGHT)
        three_dots = BootstrapSVGMobject('three-dots', color=GRAY).scale(0.1).shift(3*UP).shift(0.5*RIGHT)

        # Create 3 rows with the following values:
        # 1. 1
        # 2. f(x) = secret + ax
        # 3. 2
        line_degree = MathTex("1")
        line_polynomial = MathTex(
            r"f(x) &= secret + ax",
            substrings_to_isolate="x"
        )
        line_polynomial.set_color_by_tex("x", RED)
        line_threshold = VGroup(person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy(), person_4.copy(), person_5.copy(), person_6.copy(), person_7.copy())

        # Create 3 rows with the following values:
        # 1. 2
        # 2. g(x) = ax^2
        # 3. 3
        quadratic_degree = MathTex("2")
        quadratic_polynomial = MathTex(
            r"f(x) &= secret + ax + bx^2",
            substrings_to_isolate="x"
        )
        quadratic_polynomial.set_color_by_tex("x", RED)
        quadratic_threshold = VGroup(person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy().set_color(BLUE), person_4.copy(), person_5.copy(), person_6.copy(), person_7.copy())

        # Create 3 rows with the following values:
        # 1. 3
        # 2. h(x) = ax^3
        # 3. 4
        cubic_degree = MathTex("3")
        cubic_polynomial = MathTex(
            r"f(x) &= secret + ax + bx^2 + cx^3",
            substrings_to_isolate="x"
        )
        cubic_polynomial.set_color_by_tex("x", RED)
        cubic_threshold = VGroup(person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy().set_color(BLUE), person_4.copy().set_color(BLUE), person_5.copy(), person_6.copy(), person_7.copy())

        # Create 3 rows with the following values:
        # 1. 4
        # 2. i(x) = ax^4
        # 3. 5
        quartic_degree = MathTex("4")
        quartic_polynomial = MathTex(
            r"f(x) &= secret + ax + bx^2 + cx^3 + dx^4",
            substrings_to_isolate="x"
        )
        quartic_polynomial.set_color_by_tex("x", RED)
        quartic_threshold = VGroup(person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy().set_color(BLUE), person_4.copy().set_color(BLUE), person_5.copy().set_color(BLUE), person_6.copy(), person_7.copy())


        # Create  3 rows with the following values:
        # 1. n
        # 2. f(x) = secret + ax + bx^2 + cx^3 + ... + nx^n
        # 3. n+1
        n_degree = MathTex("n")
        n_polynomial = MathTex(
            r"f(x) &= secret + ax + bx^2 + cx^3 + ... + nx^n",
            substrings_to_isolate="x"
        )
        n_polynomial.set_color_by_tex("x", RED)
        n_threshold = VGroup(person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy().set_color(BLUE), person_4.copy().set_color(BLUE), person_5.copy().set_color(BLUE), three_dots.copy().set_color(BLUE), person_7.copy())
        
        table = MobjectTable(
            [
                [MathTex(r"\textbf{Polynomial Degree}"), MathTex(r"\textbf{Polynomial}"), MathTex(r"\textbf{Threshold number of shares}")],
                [line_degree.copy(), line_polynomial.copy(), line_threshold.copy()],
                [quadratic_degree.copy(), quadratic_polynomial.copy(), quadratic_threshold.copy()],
                [cubic_degree.copy(), cubic_polynomial.copy(), cubic_threshold.copy()],
                [quartic_degree.copy(), quartic_polynomial.copy(), quartic_threshold.copy()],
                [n_degree.copy(), n_polynomial.copy(), n_threshold.copy()],
            ]
        ).scale(0.6)
        
        self.play(
            Create(table)
        )
        self.wait(0.5)

        self.play(
            Indicate(table.get_rows()[1][2][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[1][2][1], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)

        self.play(
            Indicate(table.get_rows()[1][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[1][1], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)




        self.play(
            Indicate(table.get_rows()[2][2][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[2][2][1], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[2][2][2], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)

        self.play(
            Indicate(table.get_rows()[2][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[2][1], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)


        self.play(
            Indicate(table.get_rows()[3][2][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[3][2][1], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[3][2][2], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[3][2][3], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)
        
        self.play(
            Indicate(table.get_rows()[3][0], scale_factor=1.1, color=RED),
            Indicate(table.get_rows()[3][1], scale_factor=1.1, color=RED),
        )
        self.wait(0.5)

        lagrange_interpolation_text = MathTex(r"\textbf{Lagrange Interpolation}", color=BLUE).scale(2).to_edge(UP).shift(DOWN)

        quadratic_threshold = VGroup(
            person_1.copy().set_color(BLUE), person_2.copy().set_color(BLUE), person_3.copy().set_color(BLUE), person_4.copy(), person_5.copy(), person_6.copy(), person_7.copy()
        ).next_to(lagrange_interpolation_text, DOWN, buff=1.5)

        quadratic_polynomial = MathTex(
            r"f(x) &= secret + ax + bx^2",
            substrings_to_isolate="x"
        ).next_to(quadratic_threshold, DOWN, buff=1.5)
        quadratic_polynomial.set_color_by_tex("x", RED)

        arrow = Arrow(start=quadratic_threshold.get_bottom(), end=quadratic_polynomial.get_top(), color=WHITE)

        new_group = VGroup(quadratic_threshold, quadratic_polynomial, arrow)

        self.play(
            TransformMatchingShapes(table, new_group)
        )
        self.wait(0.5)

        self.play(
            DrawBorderThenFill(lagrange_interpolation_text)
        )
        self.wait(0.5)


        self.wait(2)