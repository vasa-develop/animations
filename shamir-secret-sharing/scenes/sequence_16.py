from manim import *

class Sequence16(Scene):
    
    circle = None
    ticks = None
    yellow_box = None
    numbers = None

    def create_clock(self):
        # Create a circle
        self.circle = Circle(radius=1.5)
        
        # Create clock ticks and numbers
        self.ticks = VGroup()
        self.numbers = VGroup()
        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)  # Initialize variable to store the yellow box
        
        for i in range(5):
            # Calculate the angle for each tick
            angle = (((i+1) % 5) * TAU / 5)
            start_point = self.circle.point_at_angle(angle)
            end_point = self.circle.point_at_angle(angle) * 0.9
            tick = Line(start_point, end_point, color=WHITE)
            self.ticks.add(tick)
            
            # Add numbers
            number_value = 4-i
            number = Text(str(number_value)).scale(0.7).next_to(tick, end_point - start_point, buff=0.2)
            self.numbers.add(number)

        self.circle.shift(4*RIGHT)
        self.ticks.shift(4*RIGHT)
        self.numbers.shift(4*RIGHT)
        self.yellow_box.shift(4*RIGHT)
        
        # Display the circle, ticks, and numbers
        self.play(
            Create(self.circle),
            Create(self.ticks),
            Write(self.numbers)
        )

    def construct(self):
        """
        TODO: Add animation for 
        
        Let’s try to do this using our old friend, modular arithmetic.
        """

        modular_arithmetic_problem_text = MathTex(r"\textbf{Modular Arithmetic}", color=BLUE).scale(1.5).shift(3*UP)
        self.play(Write(modular_arithmetic_problem_text))

        self.create_clock()

        addition_text = MathTex(r"\textbf{Addition}", color=WHITE).scale(1).shift(1.5*UP + LEFT)
        substraction_text = MathTex(r"\textbf{Subtraction}", color=WHITE).scale(1).next_to(addition_text, direction=DOWN, buff=1)
        multiplication_text = MathTex(r"\textbf{Multiplication}", color=WHITE).scale(1).next_to(substraction_text, direction=DOWN, buff=1)
        division_text = MathTex(r"\textbf{Division}", color=WHITE).scale(1).next_to(multiplication_text, direction=DOWN, buff=1)

        self.play(
            Write(addition_text),
            Write(substraction_text),
            Write(multiplication_text),
            Write(division_text)
        )
        self.add(addition_text, substraction_text, multiplication_text, division_text)

        modular_addition_question = MathTex(r"4 + 2 \equiv \; ? \mod 5", color=WHITE).scale(1).shift(1.5*UP + LEFT)
        self.play(Transform(addition_text, modular_addition_question))
        self.add(modular_addition_question)
        self.remove(addition_text)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[4-4])
            self.play(Create(self.yellow_box))
            self.add(self.yellow_box)
        
        # Animate the yellow box moving from 8 to 2
        for i in [0, 1]:
            target_number = self.numbers[4-i]
            self.play(self.yellow_box.animate.surround(target_number))

        modular_addition = MathTex(r"4 + 2 \equiv 1 \mod 5", color=WHITE).scale(1).shift(1.5*UP + LEFT)
        self.play(
            Transform(self.yellow_box, modular_addition),
            FadeOut(modular_addition_question)
        )
        self.add(modular_addition)
        self.remove(modular_addition_question)







        modular_substraction_question = MathTex(r"4 - 2 \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_addition, direction=DOWN, buff=1)
        self.play(Transform(substraction_text, modular_substraction_question))
        self.add(modular_substraction_question)
        self.remove(substraction_text, self.yellow_box)

        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[4-4])
            self.play(Create(self.yellow_box))
            self.add(self.yellow_box)

        for i in [3, 2]:
            target_number = self.numbers[4-i]
            self.play(self.yellow_box.animate.surround(target_number))

        modular_substraction = MathTex(r"4 - 2 \equiv 2 \mod 5", color=WHITE).scale(1).next_to(modular_addition, direction=DOWN, buff=1)
        self.play(
            Transform(self.yellow_box, modular_substraction),
            FadeOut(modular_substraction_question)
        )
        self.add(modular_substraction)
        self.remove(self.yellow_box, modular_substraction_question)






        modular_multiplication_question = MathTex(r"2 \times 3 \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_substraction, direction=DOWN, buff=1)
        self.play(Transform(multiplication_text, modular_multiplication_question))
        self.add(modular_multiplication_question)
        self.remove(multiplication_text, self.yellow_box)

        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[4-0])
            self.play(Create(self.yellow_box))
            self.add(self.yellow_box)

        for i in [1, 2, 3, 4, 0, 1]:
            target_number = self.numbers[4-i]
            self.play(self.yellow_box.animate.surround(target_number))

        modular_multiplication = MathTex(r"2", r"\times 3 \equiv 1 \mod 5", color=WHITE).scale(1).next_to(modular_substraction, direction=DOWN, buff=1)
        self.play(
            Transform(self.yellow_box, modular_multiplication),
            FadeOut(modular_multiplication_question)
        )
        self.add(modular_multiplication)
        self.remove(self.yellow_box, modular_multiplication_question)






        modular_division_question_1 = MathTex(r"1 \div 3 \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(division_text, modular_division_question_1))
        self.add(modular_division_question_1)
        self.remove(division_text, self.yellow_box)

        modular_division_question_2 = MathTex(r"1 \times 3^{-1} \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_1, modular_division_question_2))
        self.add(modular_division_question_2)
        self.remove(modular_division_question_1, self.yellow_box)

        modular_division_question_3 = MathTex(r"1 \times (multiplicative \; inverse \; of \; 3) \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_2, modular_division_question_3))
        self.add(modular_division_question_3)
        self.remove(modular_division_question_2, self.yellow_box)

        modular_division_question_4 = MathTex(r"(multiplicative \; inverse \; of \; 3)", r"\times 3 \equiv \; 1 \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_3, modular_division_question_4))
        self.add(modular_division_question_4)
        self.remove(modular_division_question_3, self.yellow_box)

        self.play(
            Indicate(modular_multiplication, scale_factor=1.1, color=YELLOW),
            Indicate(modular_division_question_4, scale_factor=1.1, color=YELLOW),
        )

        self.play(
            Indicate(modular_multiplication[0], scale_factor=1.1, color=YELLOW),
            Indicate(modular_division_question_4[0], scale_factor=1.1, color=YELLOW),
        )

        modular_division_question_5 = MathTex(r"1 \times (multiplicative \; inverse \; of \; 3) \equiv \; ? \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_4, modular_division_question_5))
        self.add(modular_division_question_5)
        self.remove(modular_division_question_4, self.yellow_box)

        modular_division_question_6 = MathTex(r"1 \div 3 \equiv 2 \mod 5", color=WHITE).scale(1).next_to(modular_multiplication, direction=DOWN, buff=1)
        self.play(Transform(modular_division_question_5, modular_division_question_6))
        self.add(modular_division_question_6)
        self.remove(modular_division_question_5, self.yellow_box)

        self.wait(1)