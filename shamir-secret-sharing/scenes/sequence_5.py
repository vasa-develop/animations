from manim import *

class Sequence5(Scene):
    def construct(self):
        randomness_problem_text = MathTex(r"\textbf{What are the benefits of adding randomness?}", color=BLUE).scale(1).to_edge(LEFT).shift(UP)
        modular_arithmetic_problem_text = MathTex(r"\textbf{What are the benefits of using modular arithmetic?}", color=BLUE).scale(1).next_to(randomness_problem_text, DOWN, buff=1.5).to_edge(LEFT)

        self.play(
            DrawBorderThenFill(randomness_problem_text)
        )
        self.add(randomness_problem_text)
        self.wait(1)

        self.play(
            DrawBorderThenFill(modular_arithmetic_problem_text)
        )
        self.add(modular_arithmetic_problem_text)
        self.wait(1)

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

        self.play(
            FadeOut(randomness_problem_text),
            FadeOut(modular_arithmetic_problem_text),
            DrawBorderThenFill(secret_number_group),
            DrawBorderThenFill(random_number_group),
            Create(line),
            DrawBorderThenFill(random_secret_group)
        )
        self.remove(randomness_problem_text, modular_arithmetic_problem_text)
        self.wait(1)

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
        self.wait(1)

        self.play(
            Indicate(random_secret_group, scale_factor=1.01, color=RED)
        )
        self.wait(1)
        
        self.play(
            Indicate(unknown_secret_number_group, scale_factor=1.01, color=RED)
        )
        self.wait(1)

        complete_group = VGroup(unknown_secret_number_group, unknown_random_number_group, random_secret_group, line, plus_sign)

        """ zero_secret_text = MathTex(r"\textbf{00000000}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
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
        self.remove(zero_secret_number_group, max_random_number_group) """







        axes = Axes(
            x_range=[0, 150_000_000, 10_000_000],
            y_range=[0, 150_000_000, 10_000_000],
            # axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(
            MathTex(r"\textbf{secret number}").scale(0.7).set_color(GREEN), 
            MathTex(r"\textbf{random number}").scale(0.7).set_color(BLUE)
        )
        
        dot_axes = Dot(axes.coords_to_point(100_000_000, 100_000_000), color=GREEN)

        # Create an initial label for the dot
        dot_label = MathTex(
            f"({100_000_000}, {100_000_000})"
        ).next_to(dot_axes, UR, buff=SMALL_BUFF)

        # Define an updater function to update the label
        def update_label(label):
            x, y = axes.point_to_coords(dot_axes.get_center())
            label.become(
                MathTex(
                    f"({x:,.0f}, {y:,.0f})"
                ).next_to(dot_axes, UL, buff=SMALL_BUFF)
            )

        # Add the updater to the label
        dot_label.add_updater(update_label)

        lines = axes.get_lines_to_point(axes.c2p(100_000_000, 100_000_000))

        group = VGroup(axes, labels, dot_axes, dot_label, lines)

        self.play(
            TransformMatchingShapes(complete_group, group),
            # Create(axes),
            # Create(labels),
            # Create(dot_axes),
            # Create(lines),
            # Write(dot_label)
        )
        self.wait(1)

        self.play(
            dot_axes.animate.move_to(axes.coords_to_point(93_630_212, 0)),
            lines.animate.become(axes.get_lines_to_point(axes.c2p(93_630_212, 0))),
            run_time=3
        )

        # Remove the updater to prevent it from continuing to run in the background
        dot_label.remove_updater(update_label)
        









        start_point = axes.coords_to_point(93_630_212, 0)
        end_point = axes.coords_to_point(0, 93_630_212)
        trace_line = VMobject(color=GREEN)
        trace_line.set_points_as_corners([start_point, start_point])
        
        self.play(
            dot_label.animate.next_to(dot_axes, UP, buff=SMALL_BUFF),
        )
        self.wait(1)

        def update_label(label):
            x, y = axes.point_to_coords(dot_axes.get_center())
            label.become(
                MathTex(
                    f"({x:,.0f}, {y:,.0f})"
                ).next_to(dot_axes, UP, buff=SMALL_BUFF)
                .shift(2*RIGHT*y/100_000_000)
            )
        
        def update_trace_line(line):
            line.add_line_to(dot_axes.get_center())
        
        dot_label.add_updater(update_label)
        trace_line.add_updater(update_trace_line)
        
        self.play(
            Create(trace_line),
        )
        self.wait(1)
        
        self.play(
            dot_axes.animate.move_to(end_point),
            run_time=3
        )
        self.wait(1)
        
        dot_label.remove_updater(update_label)
        trace_line.remove_updater(update_trace_line)

        random_secret_number_text = MathTex(r"\textbf{Random secret number: \;}", r"\textbf{93,630,212}").scale(0.8).set_color(BLUE).shift(2*UP + 3*RIGHT)
        combinations_text = MathTex(r"\textbf{Possible secret values: \;}", r"\textbf{93,630,212}").scale(0.8).set_color(BLUE).shift(1.5*UP + 3*RIGHT)
        
        self.play(
            Write(random_secret_number_text),
            Write(combinations_text)
        )
        self.wait(1)












        target_point = axes.coords_to_point(0, 50_000_000)
        target_line = VMobject(color=GREEN)
        target_line.set_points_as_corners([axes.coords_to_point(50_000_000, 0), axes.coords_to_point(0, 50_000_000)])

        # Update function to update the label text as the dot moves
        def update_label(label):
            x, y = axes.point_to_coords(dot_axes.get_center())
            label.become(
                MathTex(
                    f"({x:,.0f}, {y:,.0f})"
                )
                .next_to(dot_axes, UR, buff=SMALL_BUFF)
                #.shift(2*LEFT*y/100_000_000)
            )
            random_secret_number_text.become(
                MathTex(
                    rf"\textbf{{Random secret number: \;}} {y:,.0f}"
                ).scale(0.8).set_color(BLUE).shift(2*UP + 3*RIGHT)
            )
            combinations_text.become(
                MathTex(
                    rf"\textbf{{Possible secret values: \;}} {y:,.0f}"
                ).scale(0.8).set_color(BLUE).shift(1.5*UP + 3*RIGHT)
            )
            

        # Add the updaters
        dot_label.add_updater(update_label)
        #combinations_text.add_updater(update_combinations_text)

        self.play(
            dot_axes.animate.move_to(target_point),
            trace_line.animate.become(target_line),
            run_time=3
        )

        # Remove the updaters to prevent them from continuing to run in the background
        dot_label.remove_updater(update_label)
        # combinations_text.remove_updater(update_combinations_text)

        self.wait(2)