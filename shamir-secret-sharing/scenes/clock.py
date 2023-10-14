from manim import *

class ClockCircle(Scene):
    def construct(self):

        # show secret text
        secret_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2.5).shift(2*UP).shift(2*LEFT)
        secret_caption_text = MathTex(r"\textbf{(secret)}", color=GREEN).scale(1.5).next_to(secret_text, RIGHT)

        random_number_text = MathTex(r"\textbf{81284539}", color=BLUE).scale(2.5).next_to(secret_text, DOWN)
        random_number_caption_text = MathTex(r"\textbf{(randomess)}", color=BLUE).scale(1.5).next_to(random_number_text, RIGHT)
        plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(2.5).next_to(random_number_text, LEFT)

        random_number_group = VGroup(random_number_text, random_number_caption_text, plus_sign)

        # a line below the randomness text
        line = Line(start=3*LEFT, end=3*RIGHT).next_to(random_number_text, DOWN)

        # sum representing the random secret
        random_secret_text = MathTex(r"\textbf{93529107}").scale(2.5).next_to(line, DOWN)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_caption_text = MathTex(r"\textbf{(random secret)}").scale(1.5).next_to(random_secret_text, RIGHT)
        random_secret_caption_text.set_color(color=[GREEN, BLUE], family=True)
        random_secret_group = VGroup(random_secret_text, random_secret_caption_text)


        self.play(
            Create(secret_text),
            Create(secret_caption_text),
            Create(random_number_group),
            Create(line),
            Create(random_secret_group)
        )


        # Create a circle
        circle = Circle(radius=1.5)
        
        # Create clock ticks and numbers
        ticks = VGroup()
        numbers = VGroup()
        yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)  # Initialize variable to store the yellow box
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
            
            # Create a vertical yellow box around the number 8
            if number_value == 8:
                # yellow_box = Rectangle(height=0.5, width=0.3, color=YELLOW, fill_opacity=0.3)
                yellow_box.surround(number)
        

        circle.shift(5*RIGHT + 2*DOWN)
        ticks.shift(5*RIGHT + 2*DOWN)
        numbers.shift(5*RIGHT + 2*DOWN)
        yellow_box.shift(5*RIGHT + 2*DOWN)
        
        # Display the circle, ticks, and numbers
        self.play(
            Create(circle),
            Create(ticks),
            Write(numbers)
        )
        
        # Display the yellow box if it exists
        if yellow_box:
            self.play(Create(yellow_box))
        
        # Animate the yellow box moving from 8 to 3
        for i in [7, 6, 5, 4, 3]:
            target_number = numbers[9-i]
            self.play(yellow_box.animate.surround(target_number))
        
        self.wait()
