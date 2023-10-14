from manim import *

class Sequence2(Scene):

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

    
    def construct(self, *args) -> [Line, VGroup, VGroup, VGroup]:

        randomness_text = None

        if len(args) == 0:
            randomness_text = MathTex(r"\textbf{Randomness}").scale(2.5)
            randomness_text.set_color(color=[GREEN, BLUE], family=True)
            self.play(DrawBorderThenFill(randomness_text))
            self.add(randomness_text)
        else:
            randomness_text = args[0]

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

        # Draw secret and secret caption text and move randomness text down
        self.play(
            DrawBorderThenFill(secret_number_group),
            ApplyMethod(randomness_text.shift, 2*DOWN)
        )

        self.add(secret_text)
        self.add(secret_caption_text)

        self.play(
            Transform(randomness_text, random_number_group),
        )

        self.add(random_number_group)
        self.remove(randomness_text)

        self.play(
            Create(line)
        )

        self.add(line)

        rect_height = secret_text.get_height() + random_number_text.get_height() + 0.7
        combined_rect_1 = Rectangle(height=rect_height, width=0.8, color=YELLOW).next_to(secret_text[-1], UP, buff=0).align_to(random_number_text[-1], DOWN).shift(2.5*RIGHT + 0.2*DOWN)
        combined_rect_2 = Rectangle(height=rect_height, width=0.8, color=YELLOW).next_to(secret_text[-1], UP, buff=0).align_to(random_number_text[-1], DOWN).shift(1.8*RIGHT + 0.2*DOWN)

        random_secret_modular_sum_text_1 = MathTex(r"\textbf{2}").scale(2.5).next_to(line, DOWN).shift(2.5*RIGHT)
        random_secret_modular_sum_text_1.set_color(color=[GREEN, BLUE], family=True)
        
        random_secret_modular_sum_text_2 = MathTex(r"\textbf{0}").scale(2.5).next_to(line, DOWN).shift(1.8*RIGHT)
        random_secret_modular_sum_text_2.set_color(color=[GREEN, BLUE], family=True)

        partial_sum_group = VGroup(
            random_secret_modular_sum_text_1,
            random_secret_modular_sum_text_2,
        )

        self.create_clock()


        self.play(Create(combined_rect_1))
        self.add(combined_rect_1)

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[9-8])
            self.play(Transform(combined_rect_1, self.yellow_box))
            self.add(self.yellow_box)
            self.remove(combined_rect_1)
        
        # Animate the yellow box moving from 8 to 2
        for i in [9, 0, 1, 2]:
            target_number = self.numbers[9-i]
            self.play(self.yellow_box.animate.surround(target_number))


        self.play(Transform(self.yellow_box, random_secret_modular_sum_text_1))
        self.add(random_secret_modular_sum_text_1)
        self.remove(self.yellow_box)


        self.play(Create(combined_rect_2))
        self.add(combined_rect_2)
        
        self.yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)  # Initialize variable to store the yellow box

        # Display the yellow box if it exists
        if self.yellow_box:
            self.yellow_box.surround(self.numbers[9-7])
            self.play(Transform(combined_rect_2, self.yellow_box))
            self.add(self.yellow_box)
            self.remove(combined_rect_2)
        
        # Animate the yellow box moving from 8 to 3
        for i in [8, 9, 0]:
            target_number = self.numbers[9-i]
            self.play(self.yellow_box.animate.surround(target_number))
        
        self.play(Transform(self.yellow_box, random_secret_modular_sum_text_2))
        self.add(random_secret_modular_sum_text_2)
        self.remove(self.yellow_box)

        self.play(
            FadeOut(self.circle),
            FadeOut(self.ticks),
            FadeOut(self.numbers),
            Transform(partial_sum_group, random_secret_group)
        )

        self.add(random_secret_group)
        self.remove(partial_sum_group)
        self.remove(self.circle)
        self.remove(self.ticks)
        self.remove(self.numbers)

        self.wait(2)

        return [line, secret_number_group, random_number_group, random_secret_group]