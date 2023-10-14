from manim import *

class ArithmeticVsModular(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 10],
            y_range=[-2, 10],
            axis_config={"color": BLUE},
        )

        # Regular Arithmetic Line: y = x
        line_reg = ParametricFunction(lambda t: axes.c2p(t, t), t_range=[-2, 10], color=WHITE)
        label_reg = MathTex("y=x").next_to(line_reg, UP)

        # Modular Arithmetic with modulo 5
        # Multiple lines can pass through the point (3, 3) modulo 5
        lines_mod = [
            # ParametricFunction(lambda t: axes.c2p(t, (2*t + 5) % 101), t_range=[-2, 110]).set_color(RED),
            # ParametricFunction(lambda t: axes.c2p(t, (103*t + 5) % 101), t_range=[-2, 110]).set_color(GREEN),
            # ParametricFunction(lambda t: axes.c2p(t, (t) % 5), t_range=[-2, 10]).set_color(RED),
            # ParametricFunction(lambda t: axes.c2p(t, (2*t) % 5), t_range=[-2, 10]).set_color(GREEN),
            # ParametricFunction(lambda t: axes.c2p(t, (0) % 5), t_range=[-2, 10]).set_color(PURPLE)
            ParametricFunction(lambda t: axes.c2p(t, (t/3) % 5), t_range=[-2, 10]).set_color(PURPLE)
        ]

        self.play(Create(axes), *[Create(line) for line in lines_mod])
        self.wait(2)


class ModularGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 15],
            y_range=[0, 10],
            axis_config={"color": BLUE},
        )

        # Define the function
        def func(x):
            return (x * 2) % 5  # Using the multiplicative inverse of 3 mod 5

        # Create the graph
        graph = axes.plot(func, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x/3 mod 5')

        # Display everything
        self.play(
            Create(axes),
            Create(graph),
            Write(graph_label)
        )
        self.wait()


from manim import *

class ClockCircleWithMovement(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2)
        
        # Create clock ticks and numbers
        ticks = VGroup()
        numbers = VGroup()
        for i in range(10):
            # Calculate the angle for each tick
            angle = -TAU/4 + i * TAU / 10  # Adjusted to start with 0 at the top
            start_point = circle.point_at_angle(angle)
            end_point = circle.point_at_angle(angle) * 0.9
            tick = Line(start_point, end_point, color=WHITE)
            ticks.add(tick)
            
            # Add numbers
            number = Text(str(i)).scale(0.5).next_to(tick, end_point - start_point, buff=0.2)
            numbers.add(number)
        
        # Create a rectangle around 8
        rect = SurroundingRectangle(numbers[8], color=YELLOW)
        
        # Display the circle, ticks, numbers, and rectangle
        self.play(
            Create(circle),
            Create(ticks),
            Write(numbers),
            Create(rect)
        )
        
        # Move 5 divisions in a clockwise manner: 8 -> 9 -> 0 -> 1 -> 2 -> 3
        positions = [8, 9, 0, 1, 2, 3]
        for pos in positions[1:]:
            self.play(rect.animate.next_to(numbers[pos], DOWN, buff=0), run_time=0.5)
        
        self.wait()


class Graph(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 1_000, 100], y_range=[0, 1_000, 100])
        labels = axes.get_axis_labels(
            MathTex(r"\textbf{secret number}").set_color(GREEN).scale(0.7),
            MathTex(r"\textbf{random number}").set_color(BLUE).scale(0.7)
        )
        self.play(
            Create(axes),
            Create(labels)
        )
        return
        point_label = MathTex("(", r"\textbf{secret number}", ",", r"\textbf{random number}", ")").set_color(WHITE).move_to(axes.c2p(5, 5)).shift(0.5*(UP + RIGHT))
        point_label[1].set_color(GREEN)  # Set x-coordinate "0" to green
        point_label[3].set_color(BLUE)  # Set x-coordinate "0" to green
        dot = Dot(point=axes.c2p(5, 5), color=RED)
        self.play(DrawBorderThenFill(dot), DrawBorderThenFill(point_label))

        new_axes = Axes(x_range=[0, 100_000_000], y_range=[0, 100_000_000])
        new_labels = axes.get_axis_labels(
            MathTex(r"\textbf{secret number}").set_color(GREEN).scale(0.7),
            MathTex(r"\textbf{random number}").set_color(BLUE).scale(0.7)
        )

        self.play(
            Transform(axes, new_axes),
            Transform(labels, new_labels),
        )

        self.wait(2)

