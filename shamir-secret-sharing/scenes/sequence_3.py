from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence3(Scene):

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
        
        for i in range(10):
            # Calculate the angle for each tick
            angle = (((i+3) % 10) * TAU / 10)
            start_point = self.circle.point_at_angle(angle)
            end_point = self.circle.point_at_angle(angle) * 0.9
            tick = Line(start_point, end_point, color=WHITE)
            self.ticks.add(tick)
            
            # Add numbers
            number_value = 9-i
            number = Text(str(number_value)).scale(0.5).next_to(tick, end_point - start_point, buff=0.2)
            self.numbers.add(number)

        self.circle.shift(5*RIGHT + 2*DOWN)
        self.ticks.shift(5*RIGHT + 2*DOWN)
        self.numbers.shift(5*RIGHT + 2*DOWN)
        self.yellow_box.shift(5*RIGHT + 2*DOWN)
        
        # Display the circle, ticks, and numbers
        self.play(
            Create(self.circle),
            Create(self.ticks),
            Write(self.numbers)
        )
        self.wait(1)

    
    def construct(self, *args) -> []:

        line = None
        secret_number_group = None
        random_number_group = None
        random_secret_group = None

        if len(args) == 0:
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
            random_secret_text = MathTex(r"\textbf{93529102}").scale(2.5).next_to(line, DOWN)
            random_secret_text.set_color(color=[GREEN, BLUE], family=True)
            random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, RIGHT)
            random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)
            random_secret_group = VGroup(random_secret_text, random_secret_caption_text)

            self.play(
                Create(secret_number_group),
                Create(random_number_group),
                Create(line),
                Create(random_secret_group)
            )
            self.add(
                secret_number_group,
                random_number_group,
                line,
                random_secret_group
            )
            self.wait(1)

        else:
            line = args[0]
            secret_number_group = args[1]
            random_number_group = args[2]
            random_secret_group = args[3]

        left_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(8*(LEFT))
        right_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(8*(RIGHT))

        random_number_text = MathTex(r"\textbf{81284534}", color=BLUE).scale(2.5).next_to(left_friend, DOWN, buff=0.5)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(random_number_text, DOWN)

        random_secret_text = MathTex(r"\textbf{93529102}").scale(2.5).next_to(right_friend, DOWN, buff=0.5)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, DOWN)
        random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)

        scaled_down_random_number_group = VGroup(random_number_text, random_number_caption_text).shift(RIGHT * 4.5 + UP)
        scaled_down_random_secret_group = VGroup(random_secret_text, random_secret_caption_text).shift(LEFT * 4.5 + UP)

        self.play(
            left_friend.animate.shift(RIGHT * 4.5 + UP),
            right_friend.animate.shift(LEFT * 4.5 + UP),
            FadeOut(secret_number_group),
            FadeOut(line),
            Transform(random_number_group, scaled_down_random_number_group),
            Transform(random_secret_group, scaled_down_random_secret_group),
        )

        self.add(
            left_friend,
            right_friend,
            scaled_down_random_number_group,
            scaled_down_random_secret_group
        )
        self.remove(
            secret_number_group,
            line,
            random_number_group,
            random_secret_group
        )
        self.wait(1)

        random_secret_text = MathTex(r"\textbf{93529102}").scale(2.5).shift(2*UP).shift(2*LEFT)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, RIGHT)
        random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)
        
        random_secret_group = VGroup(random_secret_text, random_secret_caption_text)
        
        random_number_text = MathTex(r"\textbf{81284534}", color=BLUE).scale(2.5).next_to(random_secret_text, DOWN)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(random_number_text, RIGHT)
        minus_sign = MathTex(r"\textbf{-}", color=WHITE).scale(2.5).next_to(random_number_text, LEFT)

        random_number_group = VGroup(minus_sign, random_number_text, random_number_caption_text)

        # show secret text
        secret_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2.5).next_to(line, DOWN)
        secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(secret_text, RIGHT)
        secret_number_group = VGroup(secret_text, secret_caption_text)


        # a line below the randomness text
        line = Line(start=3*LEFT, end=3*RIGHT).next_to(random_number_text, DOWN)


        self.play(
            FadeOut(left_friend),
            FadeOut(right_friend),
            Transform(scaled_down_random_number_group, random_number_group),
            Transform(scaled_down_random_secret_group, random_secret_group),
            Create(line)
        )

        self.add(
            random_number_group,
            random_secret_group,
            line
        )

        self.remove(
            left_friend,
            right_friend,
            scaled_down_random_number_group,
            scaled_down_random_secret_group
        )
        self.wait(1)

        rect_height = random_secret_text.get_height() + random_number_text.get_height() + 0.7
        combined_rect_1 = Rectangle(height=rect_height, width=0.8, color=YELLOW).next_to(random_secret_text[-1], UP, buff=0).align_to(random_number_text[-1], DOWN).shift(2.5*RIGHT + 0.2*DOWN)
        combined_rect_2 = Rectangle(height=rect_height, width=0.8, color=YELLOW).next_to(random_secret_text[-1], UP, buff=0).align_to(random_number_text[-1], DOWN).shift(1.8*RIGHT + 0.2*DOWN)

        random_secret_modular_diff_text_1 = MathTex(r"\textbf{8}").scale(2.5).next_to(line, DOWN).shift(2.5*RIGHT)
        random_secret_modular_diff_text_1.set_color(color=[GREEN, BLUE], family=True)
        
        random_secret_modular_diff_text_2 = MathTex(r"\textbf{7}").scale(2.5).next_to(line, DOWN).shift(1.8*RIGHT)
        random_secret_modular_diff_text_2.set_color(color=[GREEN, BLUE], family=True)

        partial_diff_group = VGroup(
            random_secret_modular_diff_text_1,
            random_secret_modular_diff_text_2,
        )

        self.create_clock()
        
        self.play(Create(combined_rect_1))
        self.wait(1)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[9-2])
            self.play(Transform(combined_rect_1, self.yellow_box))
            self.add(self.yellow_box)
            self.remove(combined_rect_1)
        
        # Animate the yellow box moving from 2 to 8
        for i in [1, 0, 9, 8]:
            target_number = self.numbers[9-i]
            self.play(self.yellow_box.animate.surround(target_number))

        self.play(
            Transform(self.yellow_box, random_secret_modular_diff_text_1),
        )
        self.wait(1)

        self.add(random_secret_modular_diff_text_1)
        self.remove(self.yellow_box)
        
        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)  # Initialize variable to store the yellow box

        self.play(Create(combined_rect_2))
        self.wait(1)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[9-0])
            self.play(Transform(combined_rect_2, self.yellow_box))
            self.add(self.yellow_box)
            self.remove(combined_rect_2)
        
        # Animate the yellow box moving from 0 to 7
        for i in [9, 8, 7]:
            target_number = self.numbers[9-i]
            self.play(self.yellow_box.animate.surround(target_number))

        self.play(
            Transform(self.yellow_box, random_secret_modular_diff_text_2),
        )
        self.add(random_secret_modular_diff_text_2)
        self.remove(self.yellow_box)
        self.wait(1)

        self.play(
            FadeOut(self.circle),
            FadeOut(self.ticks),
            FadeOut(self.numbers),
            Transform(partial_diff_group, secret_number_group)
        )
        self.add(secret_number_group)
        self.remove(partial_diff_group)
        self.remove(self.circle)
        self.remove(self.ticks)
        self.remove(self.numbers)
        self.wait(1)


        modular_arithmetic_text = MathTex(r"\textbf{Modular Arithmetic}", color=BLUE).scale(1.2)
        partial_operations_text = MathTex(r"\textbf{(} + , - \textbf{) mod } \mathit{p}", color=GREEN).scale(1.2).next_to(modular_arithmetic_text, RIGHT)
        all_operations_text = MathTex(r"\textbf{(} + , - , \times , \div \textbf{) mod } \mathit{p}", color=GREEN).scale(1.2).next_to(modular_arithmetic_text, RIGHT).shift(3*UP).shift(2.5*LEFT)

        modular_arithmetic_group = VGroup(modular_arithmetic_text, partial_operations_text).shift(3*UP).shift(2*LEFT)

        elements_text = MathTex(r"\{0,1,2,3,4,5,6,7,8,9\}").scale(1).next_to(modular_arithmetic_group, DOWN, buff=1)

        addition_text = MathTex(r"8 + 4 \equiv 2 \mod 10").scale(1).next_to(elements_text, DOWN, buff=1)
        subtraction_text = MathTex(r"8 - 4 \equiv 4 \mod 10").scale(1).next_to(addition_text, DOWN, buff=0.5)
        multiplication_text = MathTex(r"3 \times 7 = 21 \equiv 1 \mod 10").scale(1).next_to(subtraction_text, DOWN, buff=0.5)
        division_text = MathTex(r"1 \div 7 = 7^{-1} \equiv 3 \mod 10").scale(1).next_to(multiplication_text, DOWN, buff=0.5)

        self.play(
            FadeOut(secret_number_group),
            FadeOut(line),
            FadeOut(random_number_group),
            FadeOut(random_secret_group),
            DrawBorderThenFill(modular_arithmetic_text),
            DrawBorderThenFill(partial_operations_text),
            DrawBorderThenFill(elements_text),
            DrawBorderThenFill(addition_text),
            DrawBorderThenFill(subtraction_text),
        )
        self.add(
            modular_arithmetic_text,
            partial_operations_text,
            elements_text,
            addition_text,
            subtraction_text,
        )
        self.remove(
            secret_number_group,
            line,
            random_number_group,
            random_secret_group,
        )
        self.wait(1)


        self.play(
            modular_arithmetic_text.animate.shift(0.5*LEFT),
            Transform(partial_operations_text, all_operations_text),
            FadeIn(multiplication_text),
            FadeIn(division_text),
        )
        self.add(
            all_operations_text,
            multiplication_text,
            division_text,
        )
        self.remove(partial_operations_text)
        self.wait(1)

        self.play(
            FadeOut(modular_arithmetic_text),
            FadeOut(all_operations_text),
            FadeOut(elements_text),
            FadeOut(addition_text),
            FadeOut(subtraction_text),
            FadeOut(multiplication_text),
            FadeOut(division_text),
        )
        self.wait(1)

        return []