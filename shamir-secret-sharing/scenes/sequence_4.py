from manim import *

class Sequence4(Scene):
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
            #randomness_problem_text.animate.scale(1.1).shift(RIGHT*0.5).set_color(RED)
            Indicate(randomness_problem_text, scale_factor=1.02, color=RED)
        )

        secret_text = MathTex(r"\textbf{????????}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(secret_text, RIGHT)
        secret_number_group = VGroup(secret_text, secret_caption_text)

        random_number_text = MathTex(r"\textbf{????????}", color=BLUE).scale(2.5).next_to(secret_text, DOWN)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(random_number_text, RIGHT)
        plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(random_number_text, LEFT)
        random_number_group = VGroup(random_number_text, random_number_caption_text, plus_sign)

        # a line below the randomness text
        line = Line(start=3*LEFT, end=3*RIGHT).next_to(random_number_text, DOWN)

        # sum representing the random secret
        random_secret_text = MathTex(r"\textbf{93529102}").scale(2.5).next_to(line, DOWN)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, RIGHT)
        random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_group = VGroup(random_secret_text, random_secret_caption_text)


        random_secret_text_template = MathTex(r"\textbf{93529102}").scale(2.5).shift(0.5*UP)
        random_secret_text_template.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_template_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text_template, DOWN)
        random_secret_caption_template_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_template_group = VGroup(random_secret_text_template, random_secret_caption_template_text)


        self.play(
            FadeOut(modular_arithmetic_problem_text),
            Transform(randomness_problem_text, random_secret_template_group)
        )
        self.add(random_secret_template_group)
        self.remove(modular_arithmetic_problem_text, randomness_problem_text)

        self.play(
            Transform(random_secret_template_group, random_secret_group),
            DrawBorderThenFill(secret_number_group),
            DrawBorderThenFill(random_number_group),
            Create(line)
        )
        self.add(random_secret_group, secret_number_group, random_number_group, line)
        self.remove(random_secret_template_group)

        rect_height = secret_text.get_height() + random_number_text.get_height() + random_secret_text.get_height() + 1
        combined_rect = Rectangle(height=rect_height, width=0.8, color=YELLOW).next_to(secret_text[-1], UP, buff=0).align_to(random_number_text[-1], DOWN).shift(2.5*RIGHT + 1.4*DOWN)

        self.play(Create(combined_rect))
        self.add(combined_rect)


        single_digit_table = Table(
            [
                ["2"],
                ["0+2"],
                ["1+1"],
                ["2+0"],
                ["3+9"],
                ["4+8"],
                ["5+7"],
                ["6+6"],
                ["7+5"],
                ["8+4"],
                ["9+3"]
            ],
            include_outer_lines=True).scale(0.5)

        single_digit_table.add_highlighted_cell((1,1), color=RED)

        # Get the coordinates of the top-right and bottom-right corners of the relevant cells
        start_point = single_digit_table.get_entries()[1].get_corner(UP + RIGHT)
        end_point = single_digit_table.get_entries()[10].get_corner(DOWN + RIGHT)

        # Create a Brace between these points
        brace = BraceBetweenPoints(start_point, end_point, direction=RIGHT).shift(0.3*RIGHT)
        brace_label = BraceLabel(brace, r"\textbf{10 combinations}", brace_direction=RIGHT)

        single_digit_table_group = VGroup(single_digit_table, brace_label)

        self.play(
            FadeOut(random_number_group),
            FadeOut(line),
            FadeOut(random_secret_group),
            FadeOut(secret_number_group),
            Transform(combined_rect, single_digit_table_group),
        )
        self.add(single_digit_table_group)
        self.remove(random_number_group, line, random_secret_group, secret_number_group, combined_rect)

        complete_table = Table(
            [
                ["9", "3", "5", "2", "9", "1", "0", "2"],
                ["0+9", "0+3", "0+5", "0+2", "0+9", "0+1", "0+0", "0+2"],
                ["1+8", "1+2", "1+4", "1+1", "1+8", "1+0", "1+9", "1+1"],
                ["2+7", "2+1", "2+3", "2+0", "2+7", "2+9", "2+8", "2+0"],
                ["3+6", "3+0", "3+2", "3+9", "3+6", "3+8", "3+7", "3+9"],
                ["4+5", "4+9", "4+1", "4+8", "4+5", "4+7", "4+6", "4+8"],
                ["5+4", "5+8", "5+0", "5+7", "5+4", "5+6", "5+5", "5+7"],
                ["6+3", "6+7", "6+9", "6+6", "6+3", "6+5", "6+4", "6+6"],
                ["7+2", "7+6", "7+8", "7+5", "7+2", "7+4", "7+3", "7+5"],
                ["8+1", "8+5", "8+7", "8+4", "8+1", "8+3", "8+2", "8+4"],
                ["9+0", "9+4", "9+6", "9+3", "9+0", "9+2", "9+1", "9+3"]
            ],
            include_outer_lines=True).scale(0.4)

        complete_table.add_highlighted_cell((1,1), color=RED)
        complete_table.add_highlighted_cell((1,2), color=RED)
        complete_table.add_highlighted_cell((1,3), color=RED)
        complete_table.add_highlighted_cell((1,4), color=RED)
        complete_table.add_highlighted_cell((1,5), color=RED)
        complete_table.add_highlighted_cell((1,6), color=RED)
        complete_table.add_highlighted_cell((1,7), color=RED)
        complete_table.add_highlighted_cell((1,8), color=RED)

        complete_table.shift(UP)

        # Number of columns in the table
        num_columns = 8  # Adjust this based on your table

        # Calculate the indices for the 2nd and last cells in the last column
        start_index = 1 * num_columns + 7  # 2nd cell in the last column
        end_index = 10 * num_columns + 7  # Last cell in the last column

        # Get the coordinates of the top-right and bottom-right corners of the relevant cells
        start_point = complete_table.get_entries()[start_index].get_corner(UP + RIGHT)
        end_point = complete_table.get_entries()[end_index].get_corner(DOWN + RIGHT)

        # Create a Brace between these points
        brace_1 = BraceBetweenPoints(start_point, end_point, direction=RIGHT).shift(0.3*RIGHT)
        brace_2 = Brace(complete_table, direction=DOWN)
        
        brace_label_1 = BraceLabel(brace_1, r"\textbf{10}", brace_direction=RIGHT)
        brace_label_2 = BraceLabel(brace_2, r"\textbf{8 digits}", brace_direction=DOWN)

        complete_table_group = VGroup(complete_table, brace_label_1, brace_label_2)

        self.play(Transform(single_digit_table_group, complete_table_group))
        self.add(complete_table_group)
        self.remove(single_digit_table_group)

        text_1 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).shift(5.3*LEFT)
        text_2 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_1, RIGHT, buff=0.1)
        text_3 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_2, RIGHT, buff=0.1)
        text_4 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_3, RIGHT, buff=0.1)
        text_5 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_4, RIGHT, buff=0.1)
        text_6 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_5, RIGHT, buff=0.1)
        text_7 = MathTex(r"\textbf{10}", "\\times", color=GREEN).scale(1.8).next_to(text_6, RIGHT, buff=0.1)
        text_8 = MathTex(r"\textbf{10}", color=GREEN).scale(1.5).next_to(text_7, RIGHT, buff=0.1)

        full_permutation_calculation_group = VGroup(text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8)

        self.play(Transform(complete_table_group, full_permutation_calculation_group))
        self.add(full_permutation_calculation_group)
        self.remove(complete_table_group)

        hundred_million_text = MathTex(r"\textbf{100,000,000 possible combinations}", color=RED).scale(1.5)

        self.play(
            Transform(full_permutation_calculation_group, hundred_million_text)
        )
        self.add(hundred_million_text)
        self.remove(full_permutation_calculation_group)

        """
        TODO: Add animation for the following

        As we saw earlier, this is the same number of combinations that you will
        have to try if you have no secret share at all.

        So, this shows that adding randomness to our secret number mitigates the
        information leakage issue, thus a person with a share of the secret is as
        clueless as a person with no secret share at all, hence achieving perfect
        secrecy.
        -------

        No changes

        Maybe show the 3 users -> perfect secrecy thing.


        """
        
        self.wait(2)

