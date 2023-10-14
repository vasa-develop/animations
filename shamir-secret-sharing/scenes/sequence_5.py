from manim import *

class Sequence5(Scene):
    def construct(self):
        randomness_problem_text = MathTex(r"\textbf{What are the benefits of adding randomness?}", color=BLUE).scale(1).to_edge(LEFT).shift(UP)
        modular_arithmetic_problem_text = MathTex(r"\textbf{What are the benefits of using modular arithmetic?}", color=BLUE).scale(1).next_to(randomness_problem_text, DOWN, buff=1.5).to_edge(LEFT)

        self.play(
            DrawBorderThenFill(randomness_problem_text)
        )
        self.add(randomness_problem_text)

        self.play(
            DrawBorderThenFill(modular_arithmetic_problem_text)
        )
        self.add(modular_arithmetic_problem_text)

        self.play(
            # modular_arithmetic_problem_text.animate.set_color(RED)
            Indicate(modular_arithmetic_problem_text, scale_factor=1.01, color=RED)
        )

        # show secret text
        secret_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(secret_text, RIGHT)
        secret_number_group = VGroup(secret_text, secret_caption_text)

        random_number_text = MathTex(r"\textbf{81284534}", color=BLUE).scale(2.5).next_to(secret_text, DOWN)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(random_number_text, RIGHT)
        plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(random_number_text, LEFT)

        random_number_group = VGroup(random_number_text, random_number_caption_text, plus_sign)

        # a line below the randomness text
        line = Line(start=3*LEFT, end=3*RIGHT).next_to(random_number_text, DOWN)

        # sum representing the random secret
        random_secret_text = MathTex(r"\textbf{93630212}").scale(2.5).next_to(line, DOWN)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, RIGHT)
        random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_group = VGroup(random_secret_text, random_secret_caption_text)

        """
        TODO: Add animation for
        
        Let's use normal arithmetic instead of modular arithmetic to add randomness to our secret.
        """

        self.play(
            FadeOut(randomness_problem_text),
            FadeOut(modular_arithmetic_problem_text),
            DrawBorderThenFill(secret_number_group),
            DrawBorderThenFill(random_number_group),
            Create(line),
            DrawBorderThenFill(random_secret_group)
        )
        self.remove(randomness_problem_text, modular_arithmetic_problem_text)


        unknown_secret_text = MathTex(r"\textbf{????????}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        unknown_secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(unknown_secret_text, RIGHT)
        unknown_secret_number_group = VGroup(unknown_secret_text, unknown_secret_caption_text)

        unknown_random_number_text = MathTex(r"\textbf{????????}", color=BLUE).scale(2.5).next_to(unknown_secret_text, DOWN)
        unknown_random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(unknown_random_number_text, RIGHT)
        unknown_plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(unknown_random_number_text, LEFT)
        unknown_random_number_group = VGroup(unknown_random_number_text, unknown_random_number_caption_text, unknown_plus_sign)

        self.play(
            Transform(secret_number_group, unknown_secret_number_group),
            Transform(random_number_group, unknown_random_number_group)
        )
        self.add(unknown_secret_number_group, unknown_random_number_group)
        self.remove(secret_number_group, random_number_group)

        zero_secret_text = MathTex(r"\textbf{00000000}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        zero_secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(zero_secret_text, RIGHT)
        zero_secret_number_group = VGroup(zero_secret_text, zero_secret_caption_text)

        max_random_number_text = MathTex(r"\textbf{93630212}", color=BLUE).scale(2.5).next_to(zero_secret_text, DOWN)
        max_random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(max_random_number_text, RIGHT)
        max_plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(max_random_number_text, LEFT)
        max_random_number_group = VGroup(max_random_number_text, max_random_number_caption_text, max_plus_sign)

        self.play(
            Transform(unknown_secret_number_group, zero_secret_number_group),
            Transform(unknown_random_number_group, max_random_number_group)
        )
        self.add(zero_secret_number_group, max_random_number_group)
        self.remove(unknown_secret_number_group, unknown_random_number_group)


        max_secret_text = MathTex(r"\textbf{93630212}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        max_secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(max_secret_text, RIGHT)
        max_secret_number_group = VGroup(max_secret_text, max_secret_caption_text)

        zero_random_number_text = MathTex(r"\textbf{00000000}", color=BLUE).scale(2.5).next_to(zero_secret_text, DOWN)
        zero_random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(zero_random_number_text, RIGHT)
        zero_plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(zero_random_number_text, LEFT)
        zero_random_number_group = VGroup(zero_random_number_text, zero_random_number_caption_text, zero_plus_sign)

        self.play(
            Transform(zero_secret_number_group, max_secret_number_group),
            Transform(max_random_number_group, zero_random_number_group)
        )
        self.add(max_secret_number_group, zero_random_number_group)
        self.remove(zero_secret_number_group, max_random_number_group)

        """
        TODO: Add animation for

        Basically, if you increase one of these numbers, the other one will have
        to decrease and vice-versa.
        -------------
        One way to animate this would be to create 2 bars representing the secret
        and the randomness. Then, when one bar increases, the other bar decreases.
        """

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        labels = ax.get_axis_labels(
            Tex("secret number").scale(0.7), Text("random number").scale(0.45)
        )
        self.play(
            FadeOut(max_secret_number_group),
            FadeOut(zero_random_number_group),
            Create(ax),
            Create(labels)
        )

        """
        TODO: Animate the following:
        
        Each point on this graph represents a combination of the secret number and
        the random number. There are some points on this graph whose sum of the x
        and y coordinate values is equal to the random secret number that we know.
        If we plot all such points on this graph and join them, we will see that it
        is a line.

        Each point on this line represents a possible combination of values that
        you need to try to find the secret. If you count the number of points on
        this line, it's equal to the random secret number itself.

        So, the smaller the random secret number, the fewer combinations you will
        have to try. We can easily see that it will be easier to brute force the
        secret number if we use normal arithmetic compared to modular arithmetic.
        """

        self.wait(2)