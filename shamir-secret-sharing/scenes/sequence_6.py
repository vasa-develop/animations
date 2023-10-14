from manim import *

class Sequence6(Scene):

    def create_clock(self, color, number_to_surround) -> VGroup:
        # Create a circle
        circle = Circle(radius=1.5, color=color)
        
        # Create clock ticks and numbers
        ticks = VGroup()
        numbers = VGroup()
        surrounding_box = Rectangle(height=0.5, width=0.3, color=WHITE, fill_opacity=0.3)  # Initialize variable to store the yellow box
        
        for i in range(10):
            # Calculate the angle for each tick
            angle = (((i+3) % 10) * TAU / 10)
            start_point = circle.point_at_angle(angle)
            end_point = circle.point_at_angle(angle) * 0.9
            tick = Line(start_point, end_point, color=WHITE)
            ticks.add(tick)
            
            # Add numbers
            number_value = 9-i
            number = Text(str(number_value)).scale(0.5).next_to(tick, end_point - start_point, buff=0.2)
            numbers.add(number)

            if number_value == number_to_surround:
                surrounding_box.surround(numbers[9-number_to_surround])

        return VGroup(circle, ticks, numbers, surrounding_box)
    
    
    def construct(self):
        """
        TODO: Animate the following:

        Now, let's try to visualize how using modular arithmetic makes it
        harder to brute force the secret.
        """

        secret_text = MathTex(r"\textbf{12345678}", color=WHITE).scale(2.5).shift(2*UP).shift(2*LEFT)
        secret_caption_text = MathTex(r"\textbf{(secret)}", color=WHITE).scale(1.5).next_to(secret_text, RIGHT)
        secret_number_group = VGroup(secret_text, secret_caption_text)

        random_number_text = MathTex(r"\textbf{81284534}", color=WHITE).scale(2.5).next_to(secret_text, DOWN)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=WHITE).scale(1.5).next_to(random_number_text, RIGHT)
        plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(random_number_text, LEFT)

        random_number_group = VGroup(random_number_text, random_number_caption_text, plus_sign)

        # a line below the randomness text
        line = Line(start=3*LEFT, end=3*RIGHT).next_to(random_number_text, DOWN)

        # sum representing the random secret
        random_secret_text = MathTex(r"\textbf{93529102}", color=WHITE).scale(2.5).next_to(line, DOWN)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}", color=WHITE).scale(1.5).next_to(random_secret_text, RIGHT)
        random_secret_group = VGroup(random_secret_text, random_secret_caption_text)

        self.play(
            DrawBorderThenFill(secret_number_group),
            DrawBorderThenFill(random_number_group),
            Create(line),
            DrawBorderThenFill(random_secret_group)
        )
        self.add(secret_number_group, random_number_group, random_secret_group, line)

        new_secret_text = MathTex(
            r"\textbf{1}",
            r"\textbf{2}",
            r"\textbf{3}",
            r"\textbf{4}",
            r"\textbf{5}",
            r"\textbf{6}",
            r"\textbf{7}",
            r"\textbf{8}",
        ).scale(2.5).shift(2*UP).shift(2*LEFT)
        new_secret_text[0].set_color(color=RED, family=True)
        new_secret_text[1].set_color(color=ORANGE, family=True)
        new_secret_text[2].set_color(color=YELLOW, family=True)
        new_secret_text[3].set_color(color=GREEN, family=True)
        new_secret_text[4].set_color(color=TEAL, family=True)
        new_secret_text[5].set_color(color=BLUE, family=True)
        new_secret_text[6].set_color(color=PURPLE, family=True)
        new_secret_text[7].set_color(color=PINK, family=True)
        new_secret_caption_text = MathTex(r"\textbf{(secret)}").scale(1.5).next_to(new_secret_text, RIGHT)
        new_secret_number_group = VGroup(new_secret_text, new_secret_caption_text)

        new_random_number_text = MathTex(
            r"\textbf{8}",
            r"\textbf{1}",
            r"\textbf{2}",
            r"\textbf{8}",
            r"\textbf{4}",
            r"\textbf{5}",
            r"\textbf{3}",
            r"\textbf{4}",
        ).scale(2.5).next_to(new_secret_text, DOWN)
        new_random_number_text[0].set_color(color=RED, family=True)
        new_random_number_text[1].set_color(color=ORANGE, family=True)
        new_random_number_text[2].set_color(color=YELLOW, family=True)
        new_random_number_text[3].set_color(color=GREEN, family=True)
        new_random_number_text[4].set_color(color=TEAL, family=True)
        new_random_number_text[5].set_color(color=BLUE, family=True)
        new_random_number_text[6].set_color(color=PURPLE, family=True)
        new_random_number_text[7].set_color(color=PINK, family=True)
        new_random_number_caption_text = MathTex(r"\textbf{(randomess)}").scale(1.5).next_to(new_random_number_text, RIGHT)
        new_plus_sign = MathTex(r"\textbf{+}").scale(2.5).next_to(new_random_number_text, LEFT)

        new_random_number_group = VGroup(new_random_number_text, new_random_number_caption_text, new_plus_sign)

        # a line below the randomness text
        new_line = Line(start=3*LEFT, end=3*RIGHT).next_to(new_random_number_text, DOWN)

        # sum representing the random secret
        new_random_secret_text = MathTex(
            r"\textbf{9}",
            r"\textbf{3}",
            r"\textbf{5}",
            r"\textbf{2}",
            r"\textbf{9}",
            r"\textbf{1}",
            r"\textbf{0}",
            r"\textbf{2}",
        ).scale(2.5).next_to(new_line, DOWN)
        new_random_secret_text[0].set_color(color=RED, family=True)
        new_random_secret_text[1].set_color(color=ORANGE, family=True)
        new_random_secret_text[2].set_color(color=YELLOW, family=True)
        new_random_secret_text[3].set_color(color=GREEN, family=True)
        new_random_secret_text[4].set_color(color=TEAL, family=True)
        new_random_secret_text[5].set_color(color=BLUE, family=True)
        new_random_secret_text[6].set_color(color=PURPLE, family=True)
        new_random_secret_text[7].set_color(color=PINK, family=True)
        new_random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(new_random_secret_text, RIGHT)
        new_random_secret_group = VGroup(new_random_secret_text, new_random_secret_caption_text)

        self.play(
            TransformMatchingTex(secret_number_group, new_secret_number_group),
            TransformMatchingTex(random_number_group, new_random_number_group),
            TransformMatchingTex(random_secret_group, new_random_secret_group),
        )
        self.add(
            new_secret_number_group,
            new_random_number_group,
            new_random_secret_group,
            new_line
        )
        self.remove(
            secret_number_group,
            random_number_group,
            random_secret_group,
            line
        )

        group = VGroup(new_secret_number_group, new_random_number_group, new_line, new_random_secret_group)
        self.add(group)
        self.remove(new_secret_number_group, new_random_number_group, new_random_secret_group)

        modular_sum_1 = MathTex(r"1 + 8 \equiv 9 \mod 10", color=RED).scale(1).shift(3*UP)
        modular_sum_2 = MathTex(r"2 + 1 \equiv 3 \mod 10", color=ORANGE).scale(1).next_to(modular_sum_1, DOWN, buff=0.4)
        modular_sum_3 = MathTex(r"3 + 2 \equiv 5 \mod 10", color=YELLOW).scale(1).next_to(modular_sum_2, DOWN, buff=0.4)
        modular_sum_4 = MathTex(r"4 + 8 \equiv 2 \mod 10", color=GREEN).scale(1).next_to(modular_sum_3, DOWN, buff=0.4)
        modular_sum_5 = MathTex(r"5 + 4 \equiv 9 \mod 10", color=TEAL).scale(1).next_to(modular_sum_4, DOWN, buff=0.4)
        modular_sum_6 = MathTex(r"6 + 5 \equiv 1 \mod 10", color=BLUE).scale(1).next_to(modular_sum_5, DOWN, buff=0.4)
        modular_sum_7 = MathTex(r"7 + 3 \equiv 0 \mod 10", color=PURPLE).scale(1).next_to(modular_sum_6, DOWN, buff=0.4)
        modular_sum_8 = MathTex(r"8 + 4 \equiv 2 \mod 10", color=PINK).scale(1).next_to(modular_sum_7, DOWN, buff=0.4)

        modular_sum_group = VGroup(
            modular_sum_1,
            modular_sum_2,
            modular_sum_3,
            modular_sum_4,
            modular_sum_5,
            modular_sum_6,
            modular_sum_7,
            modular_sum_8
        )

        self.play(
            Transform(group, modular_sum_group)
        )
        self.add(modular_sum_group)
        self.remove(group)

        clock_1 = self.create_clock(color=RED, number_to_surround=9).shift(5*LEFT).shift(2*UP)
        clock_2 = self.create_clock(color=ORANGE, number_to_surround=3).next_to(clock_1, RIGHT, buff=0.4)
        clock_3 = self.create_clock(color=YELLOW, number_to_surround=5).next_to(clock_2, RIGHT, buff=0.4)
        clock_4 = self.create_clock(color=GREEN, number_to_surround=2).next_to(clock_3, RIGHT, buff=0.4)
        clock_5 = self.create_clock(color=TEAL, number_to_surround=9).next_to(clock_1, DOWN, buff=0.6)
        clock_6 = self.create_clock(color=BLUE, number_to_surround=1).next_to(clock_2, DOWN, buff=0.6)
        clock_7 = self.create_clock(color=PURPLE, number_to_surround=0).next_to(clock_3, DOWN, buff=0.6)
        clock_8 = self.create_clock(color=PINK, number_to_surround=2).next_to(clock_4, DOWN, buff=0.6)

        clock_group = VGroup(
            clock_1,
            clock_2,
            clock_3,
            clock_4,
            clock_5,
            clock_6,
            clock_7,
            clock_8
        )

        self.play(
            Transform(modular_sum_group, clock_group)
        )
        self.add(clock_group)
        self.remove(modular_sum_group)

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
        complete_table.add_highlighted_cell((1,2), color=ORANGE)
        complete_table.add_highlighted_cell((1,3), color=YELLOW)
        complete_table.add_highlighted_cell((1,4), color=GREEN)
        complete_table.add_highlighted_cell((1,5), color=TEAL)
        complete_table.add_highlighted_cell((1,6), color=BLUE)
        complete_table.add_highlighted_cell((1,7), color=PURPLE)
        complete_table.add_highlighted_cell((1,8), color=PINK)

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

        self.play(Transform(clock_group, complete_table_group))
        self.add(complete_table_group)
        self.remove(clock_group)

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




        self.wait(2)