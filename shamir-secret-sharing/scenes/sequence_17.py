from manim import *

class Sequence17(Scene):

    circle = None
    ticks = None
    yellow_box = None
    numbers = None

    def create_clock(self, modulo_value):
        # Create a circle
        self.circle = Circle(radius=1.5)
        
        # Create clock ticks and numbers
        self.ticks = VGroup()
        self.numbers = VGroup()
        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)  # Initialize variable to store the yellow box
        
        for i in range(modulo_value):
            # Calculate the angle for each tick
            angle = (((i+1) % modulo_value) * TAU / modulo_value)
            start_point = self.circle.point_at_angle(angle)
            end_point = self.circle.point_at_angle(angle) * 0.9
            tick = Line(start_point, end_point, color=WHITE)
            self.ticks.add(tick)
            
            # Add numbers
            number_value = (modulo_value-1)-i
            number = Text(str(number_value)).scale(0.7).next_to(tick, end_point - start_point, buff=0.2)
            self.numbers.add(number)

        self.circle.shift(4*RIGHT)
        self.ticks.shift(4*RIGHT)
        self.numbers.shift(4*RIGHT)
        self.yellow_box.shift(4*RIGHT)
    
    def construct(self):
        question_1_a_text = MathTex(r"\textbf{1. Does this new form of arithmetic work for any}", color=RED).scale(1).to_edge(LEFT).shift(1.5*UP)
        question_1_b_text = MathTex(r"\textbf{modulo value?}", color=RED).scale(1).next_to(question_1_a_text, DOWN).to_edge(LEFT)
        question_1_group = VGroup(question_1_a_text, question_1_b_text)
        self.play(
            Write(question_1_group)
        )
        self.wait(0.5)

        question_2_a_text = MathTex(r"\textbf{2. What are finite fields and how modular arithmetic}", color=RED).scale(1).to_edge(LEFT).shift(DOWN)
        question_2_b_text = MathTex(r"\textbf{is related to it?}", color=RED).scale(1).next_to(question_2_a_text, DOWN).to_edge(LEFT)
        question_2_group = VGroup(question_2_a_text, question_2_b_text)
        self.play(
            Write(question_2_group)
        )
        self.wait(0.5)

        self.play(
            Indicate(question_1_group, scale_factor=1.01)
        )
        self.wait(0.5)

        question_group = VGroup(question_1_group, question_2_group)


        modular_arithmetic_problem_text_6 = MathTex(r"\textbf{Modular Arithmetic with modulo 6}", color=BLUE).scale(1.5).shift(3*UP)

        addition_text = MathTex(r"\textbf{Addition}", color=WHITE).scale(1).shift(1.5*UP + LEFT)
        substraction_text = MathTex(r"\textbf{Subtraction}", color=WHITE).scale(1).next_to(addition_text, direction=DOWN, buff=1)
        multiplication_text = MathTex(r"\textbf{Multiplication}", color=WHITE).scale(1).next_to(substraction_text, direction=DOWN, buff=1)
        division_text = MathTex(r"\textbf{Division}", color=WHITE).scale(1).next_to(multiplication_text, direction=DOWN, buff=1)
        operation_group = VGroup(addition_text, substraction_text, multiplication_text, division_text)

        heading_and_operations_group = VGroup(modular_arithmetic_problem_text_6, operation_group)

        self.play(
            TransformMatchingShapes(question_group, heading_and_operations_group),
        )
        self.add(heading_and_operations_group)
        self.remove(question_group)
        self.wait(0.5)

        self.create_clock(6)
        clock_6 = VGroup(self.circle, self.ticks, self.numbers)
        self.play(
            Create(self.circle),
            Create(self.ticks),
            Write(self.numbers)
        )
        self.add(self.circle, self.ticks, self.numbers)
        self.wait(0.5)

        new_addition_text = MathTex(r"\checkmark \textbf{Addition}", color=GREEN).scale(1).shift(1.5*UP + LEFT)
        self.play(Transform(addition_text, new_addition_text))
        self.add(new_addition_text)
        self.remove(addition_text)
        self.wait(0.5)

        new_substraction_text = MathTex(r"\checkmark \textbf{Subtraction}", color=GREEN).scale(1).next_to(addition_text, direction=DOWN, buff=1)
        self.play(Transform(substraction_text, new_substraction_text))
        self.add(new_substraction_text)
        self.remove(substraction_text)
        self.wait(0.5)

        new_multiplication_text = MathTex(r"\checkmark \textbf{Multiplication}", color=GREEN).scale(1).next_to(substraction_text, direction=DOWN, buff=1)
        self.play(Transform(multiplication_text, new_multiplication_text))
        self.add(new_multiplication_text)
        self.remove(multiplication_text)
        self.wait(0.5)

        modular_division_question_1 = MathTex(r"1 \div 2 \equiv \; ? \mod 6", color=WHITE).scale(1).next_to(multiplication_text, direction=DOWN, buff=1)
        self.play(Transform(division_text, modular_division_question_1))
        self.add(modular_division_question_1)
        self.remove(division_text)
        self.wait(0.5)

        modular_division_question_2 = MathTex(r"1 \times 2^{-1} \equiv \; ? \mod 6", color=WHITE).scale(1).next_to(multiplication_text, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_1, modular_division_question_2))
        self.add(modular_division_question_2)
        self.remove(modular_division_question_1)
        self.wait(0.5)

        modular_division_question_3 = MathTex(r"(multiplicative \; inverse \; of \; 2)", r"\times 2 \equiv \; 1 \mod 6", color=WHITE).scale(1).next_to(multiplication_text, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_2, modular_division_question_3))
        self.add(modular_division_question_3)
        self.remove(modular_division_question_2)
        self.wait(0.5)


        new_operation_group = VGroup(new_addition_text, new_substraction_text, new_multiplication_text, modular_division_question_3) 

        single_digit_mod_mul_table = Table(
            [
                ["0"],
                ["2"],
                ["4"],
                ["0"],
                ["2"],
                ["4"],
            ],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}")],
            col_labels=[MathTex(r"\textbf{2}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        single_digit_mod_mul_table.add_highlighted_cell((1,2), color=PURPLE)
        
        single_digit_mod_mul_table.add_highlighted_cell((2,1), color=PURPLE)
        single_digit_mod_mul_table.add_highlighted_cell((3,1), color=PURPLE)
        single_digit_mod_mul_table.add_highlighted_cell((4,1), color=PURPLE)
        single_digit_mod_mul_table.add_highlighted_cell((5,1), color=PURPLE)
        single_digit_mod_mul_table.add_highlighted_cell((6,1), color=PURPLE)
        single_digit_mod_mul_table.add_highlighted_cell((7,1), color=PURPLE)

        single_digit_mod_mul_table.shift(0.5*DOWN+LEFT)

        self.play(Transform(new_operation_group, single_digit_mod_mul_table))
        self.add(single_digit_mod_mul_table)
        self.remove(new_operation_group)
        self.wait(0.5)



        def mul_mod_6(x, y):
            return str((x * y) % 6)


        table = Table(
            [[mul_mod_6(i, j) for j in range(6)] for i in range(6)],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}")],
            col_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        table.add_highlighted_cell((1,2), color=PURPLE)
        table.add_highlighted_cell((1,3), color=PURPLE)
        table.add_highlighted_cell((1,4), color=PURPLE)
        table.add_highlighted_cell((1,5), color=PURPLE)
        table.add_highlighted_cell((1,6), color=PURPLE)
        table.add_highlighted_cell((1,7), color=PURPLE)

        
        table.add_highlighted_cell((2,1), color=PURPLE)
        table.add_highlighted_cell((3,1), color=PURPLE)
        table.add_highlighted_cell((4,1), color=PURPLE)
        table.add_highlighted_cell((5,1), color=PURPLE)
        table.add_highlighted_cell((6,1), color=PURPLE)
        table.add_highlighted_cell((7,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(8):
            for j in range(8):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_6(i-2, j-2) == "1":
                        if i != 1 and j != 1:
                            table.add_highlighted_cell((i,j), color=GREEN)


        table.shift(0.5*DOWN+2*LEFT)

        self.play(Transform(single_digit_mod_mul_table, table))
        self.add(table)
        self.remove(single_digit_mod_mul_table)
        self.wait(0.5)

        one_div_two_text = MathTex(r"1 \div 2 \equiv \; ? \mod 6", color=RED).scale(0.7).next_to(self.circle, direction=DOWN, buff=0.5)
        one_div_three_text = MathTex(r"1 \div 3 \equiv \; ? \mod 6", color=RED).scale(0.7).next_to(one_div_two_text, direction=DOWN)
        one_div_four_text = MathTex(r"1 \div 4 \equiv \; ? \mod 6", color=RED).scale(0.7).next_to(one_div_three_text, direction=DOWN)
        group = VGroup(one_div_two_text, one_div_three_text, one_div_four_text)
        
        self.play(Write(group))
        self.add(group)
        self.wait(0.5)

        self.play(FadeOut(group))
        self.remove(group)
        self.wait(0.5)

        """
        TODO: Add animation for

        So, it seems like our new form of arithmetic only works for a certain modulo values. There is a specific class of modulo numbers for which our new form of arithmetic always works. This specific class is prime numbers. It can get a bit boring to go through the proof of why this always works for the prime numbers, so we will skip that for now, but you can find link to the proof in the description of this video.

        """






        modular_arithmetic_problem_text_5 = MathTex(r"\textbf{Modular Arithmetic with modulo 5}", color=BLUE).scale(1.5).shift(3*UP)

        def mul_mod_5(x, y):
            return str((x * y) % 5)


        table_5 = Table(
            [[mul_mod_5(i, j) for j in range(5)] for i in range(5)],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}")],
            col_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        table_5.add_highlighted_cell((1,2), color=PURPLE)
        table_5.add_highlighted_cell((1,3), color=PURPLE)
        table_5.add_highlighted_cell((1,4), color=PURPLE)
        table_5.add_highlighted_cell((1,5), color=PURPLE)
        table_5.add_highlighted_cell((1,6), color=PURPLE)

        
        table_5.add_highlighted_cell((2,1), color=PURPLE)
        table_5.add_highlighted_cell((3,1), color=PURPLE)
        table_5.add_highlighted_cell((4,1), color=PURPLE)
        table_5.add_highlighted_cell((5,1), color=PURPLE)
        table_5.add_highlighted_cell((6,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(7):
            for j in range(7):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_5(i-2, j-2) == "1":
                        if i != 1 and j != 1:
                            table_5.add_highlighted_cell((i,j), color=GREEN)


        table_5.shift(0.5*DOWN+2*LEFT)

        self.remove(self.circle, self.ticks, self.numbers)
        self.create_clock(5)
        clock_5 = VGroup(self.circle, self.ticks, self.numbers)
        self.play(
            Transform(modular_arithmetic_problem_text_6, modular_arithmetic_problem_text_5),
            Transform(table, table_5),
            Transform(clock_6, clock_5),
        )
        self.add(table_5, clock_5, modular_arithmetic_problem_text_5)
        self.remove(table, clock_6, modular_arithmetic_problem_text_6)
        self.wait(0.5)




        modular_arithmetic_problem_text_7 = MathTex(r"\textbf{Modular Arithmetic with modulo 7}", color=BLUE).scale(1.5).shift(3*UP)

        def mul_mod_7(x, y):
            return str((x * y) % 7)


        table_7 = Table(
            [[mul_mod_7(i, j) for j in range(7)] for i in range(7)],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}"), MathTex(r"\textbf{6}")],
            col_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}"), MathTex(r"\textbf{6}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        table_7.add_highlighted_cell((1,2), color=PURPLE)
        table_7.add_highlighted_cell((1,3), color=PURPLE)
        table_7.add_highlighted_cell((1,4), color=PURPLE)
        table_7.add_highlighted_cell((1,5), color=PURPLE)
        table_7.add_highlighted_cell((1,6), color=PURPLE)
        table_7.add_highlighted_cell((1,7), color=PURPLE)
        table_7.add_highlighted_cell((1,8), color=PURPLE)

        
        table_7.add_highlighted_cell((2,1), color=PURPLE)
        table_7.add_highlighted_cell((3,1), color=PURPLE)
        table_7.add_highlighted_cell((4,1), color=PURPLE)
        table_7.add_highlighted_cell((5,1), color=PURPLE)
        table_7.add_highlighted_cell((6,1), color=PURPLE)
        table_7.add_highlighted_cell((7,1), color=PURPLE)
        table_7.add_highlighted_cell((8,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(9):
            for j in range(9):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_7(i-2, j-2) == "1":
                        if i != 1 and j != 1:
                            table_7.add_highlighted_cell((i,j), color=GREEN)


        table_7.shift(0.5*DOWN+2*LEFT)


        self.remove(self.circle, self.ticks, self.numbers)
        self.create_clock(7)
        clock_7 = VGroup(self.circle, self.ticks, self.numbers)
        self.play(
            Transform(modular_arithmetic_problem_text_5, modular_arithmetic_problem_text_7),
            Transform(table_5, table_7),
            Transform(clock_5, clock_7),
        )
        self.add(table_7, clock_7, modular_arithmetic_problem_text_7)
        self.remove(table_5, clock_5, modular_arithmetic_problem_text_5)



        self.wait(2)
