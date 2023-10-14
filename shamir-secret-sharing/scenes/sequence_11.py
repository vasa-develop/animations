from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence11(Scene):
    
    def construct(self):
        """
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
        
        self.play(Create(table))

        """
        TODO: Add animation for the following:

        In the first case, where we wanted 2 shares to be able to recover the secret,
        we used a line, which is a polynomial of degree 1. The degree of a polynomial
        is represented by the highest power of x in the equation of the curve. For
        example in case of a line, the highest power of x is 1, hence it’s a polynomial
        of degree 1.

        In the second case, where we wanted 3 shares to be able to recover the secret,
        we used a quadratic curve, which is a polynomial of degree 2.

        Similarly, if we want 4 shares to be able to recover the secret, we will use
        a cubic curve, which is a polynomial of degree 3. Similar to other cases,
        if you have less than 4 shares, say for example 3, you will be able to find
        infinite cubic curves which pass through 3 given points.

        This pattern follows as we increase the number of shares needed to recover
        the secret.

        To generalize this system you can imagine if you have a secret that you
        want to distribute among your "k" friends in such a way that any "n" friends
        can come together to recover the secret, all we need to do is to represent
        the secret as a point on the graph and choose n-1 points to introduce
        randomness, which will form the secret curve. Then you can choose any
        "k" points/shares from this curve and distribute them among your "k" friends.
        Then any "n" or more friends can come together and recover the secret curve,
        which we can use to recover the original secret value.
        """


        self.wait(2)