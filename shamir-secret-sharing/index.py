from manim import *
import numpy as np

class TwoPointSecretReconstruction(Scene):
    def construct(self):
        # Step 1: Animation of writing "Secret: 0" in red
        secret_text = MathTex(r"\text{Secret: 1}", color=WHITE).scale(1.2)
        self.play(DrawBorderThenFill(secret_text))
        self.wait(1)

        # Move "Secret: 0" to the top
        self.play(secret_text.animate.shift(3.5*UP))
        self.wait(1)

        # Step 2: Draw x-y axes
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 5],
            axis_config={"color": WHITE},
        )
        self.play(Create(axes))
        self.wait(1)

        # Transform "0" in "Secret: 0" to "(0,0)" label on the graph
        point_label_0_0 = MathTex("(0,", "0", ")").set_color(WHITE).move_to(axes.c2p(0, 0)).shift(0.5*(DOWN + RIGHT))
        point_label_0_0[1].set_color(GREEN)  # Set y-coordinate "0" to green
        dot_0_0 = Dot(point=axes.c2p(0, 0), color=GREEN)
        self.play(DrawBorderThenFill(dot_0_0), Transform(secret_text, point_label_0_0))
        self.wait(2)

        randomness_text = MathTex("Randomness", color=WHITE).scale(1.2)
        self.play(Write(randomness_text))
        self.wait(1)

        point_label_1_1 = MathTex("(1,1)").set_color(WHITE).move_to(axes.c2p(1, 1)).shift(0.5*(DOWN + RIGHT))
        dot_1_1 = Dot(point=axes.c2p(1, 1), color=GRAY)
        self.play(DrawBorderThenFill(dot_1_1), Transform(randomness_text, point_label_1_1))
        self.wait(2)

        # Draw a green line going through point_label_0_0 and extending beyond point_label_1_1
        line = Line(dot_0_0.get_center(), dot_1_1.get_center() + 2*(dot_1_1.get_center() - dot_0_0.get_center())).set_color(GREEN)
        line_label = MathTex(r"\text{Secret Line}").set_color(WHITE).scale(0.7)

        self.play(Create(line), Write(line_label))
        self.wait(2)


        point_label_2_2 = MathTex("(2,2)").set_color(RED).move_to(axes.c2p(2, 2)).shift(0.5*(DOWN + RIGHT))
        dot_2_2 = Dot(point=axes.c2p(2, 2), color=RED)

        point_label_3_3 = MathTex("(3,3)").set_color(RED).move_to(axes.c2p(3, 3)).shift(0.5*(DOWN + RIGHT))
        dot_3_3 = Dot(point=axes.c2p(3, 3), color=RED)

        self.play(DrawBorderThenFill(dot_2_2), Write(point_label_2_2), DrawBorderThenFill(dot_3_3), Write(point_label_3_3))
        self.wait(2)


        # fade out everything except the the 2 points 
        self.play(FadeOut(secret_text), FadeOut(randomness_text), FadeOut(dot_0_0), FadeOut(dot_1_1), FadeOut(point_label_0_0), FadeOut(point_label_1_1), FadeOut(line), FadeOut(line_label))
        self.wait(1)

        # Step 3: Draw a green line through the 2 points upto starting from (3,3) to (0,0)
        line = Line(dot_3_3.get_center(), dot_0_0.get_center()).set_color(GREEN)
        line_label = MathTex(r"\text{Reconstructed Secret Line}").set_color(WHITE).scale(0.7)

        self.play(Create(line), Write(line_label))
        self.wait(2)

        self.play(DrawBorderThenFill(dot_0_0), Write(point_label_0_0))
        self.wait(2)


        # fade out everything except the the (2,2) point
        self.play(FadeOut(dot_3_3), FadeOut(line), FadeOut(line_label), FadeOut(point_label_0_0), FadeOut(point_label_3_3))

        # Y-coordinates for the points on x=0
        y_coords = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        fixed_point = axes.c2p(2, 2)

        # Create lines passing through (2,2) and the specified y-coordinates on x=0
        lines = []
        for y in y_coords:
            point_on_y_axis = axes.c2p(0, y)
            line = Line(start=fixed_point, end=point_on_y_axis, color=BLUE)
            lines.append(line)

        # Draw all lines in one go
        self.play(*[Create(line) for line in lines])

        self.wait(2)

        # Write the y-coordinates of the points on x=0
        point_labels = []
        for y in y_coords:
            point_label = MathTex("(0,", f"{y}", ")").set_color(WHITE).move_to(axes.c2p(0, y)).shift(0.5*(LEFT)).scale(0.5)
            point_label[1].set_color(BLUE)
            point_labels.append(point_label)
        
        # Write all labels in one go
        self.play(*[Write(point_label) for point_label in point_labels])

        self.wait(2)


        # fade everything including axes and recap
        self.play(*[FadeOut(line) for line in lines], *[FadeOut(point_label) for point_label in point_labels], FadeOut(dot_0_0), FadeOut(dot_2_2), FadeOut(point_label_2_2), FadeOut(axes))
        
        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))

        self.wait(1)

        self.play(FadeOut(recap_text))

        # Highlight point (2,2) in red
        self.play(Create(axes), DrawBorderThenFill(dot_2_2), Write(point_label_2_2))
        

        # Write all labels in one go
        self.play(*[Create(line) for line in lines], *[Write(point_label) for point_label in point_labels])

        self.wait(2)


        # Write a text saying "No information about the secret is leaked" at the top
        no_leak_text = MathTex(r"\text{No information about the secret is leaked with a single share}").set_color(WHITE).scale(0.7).shift(3*UP)
        self.play(Write(no_leak_text))

        self.wait(2)

        # fade out everything except the the (2,2) point
        self.play(*[FadeOut(line) for line in lines], *[FadeOut(point_label) for point_label in point_labels], FadeOut(no_leak_text))

        # Highlight point (3,3) in red
        self.play(DrawBorderThenFill(dot_3_3), Write(point_label_3_3))


        # Draw a line between (0,0) and (3,3)
        line = Line(axes.c2p(0, 0), axes.c2p(3, 3), color=GREEN)
        self.play(Create(line))

        # Add a label for the line
        line_label = MathTex(r"\text{Unique Secret Line}").set_color(WHITE).scale(0.7)
        line_label.next_to(line.get_center(), (UP + LEFT), buff=0.5)
        self.play(Write(line_label))

        self.wait(2)

        # Draw a point and label it as (0,0)
        self.play(DrawBorderThenFill(dot_0_0), Write(point_label_0_0))


        # Write a text saying "Any 2 points can be used to recover the secret point" at the top
        recover_text = MathTex(r"\text{Any 2 points can be used to recover the secret line and point}").set_color(WHITE).scale(0.7).shift(3*UP)
        self.play(Write(recover_text))

        # Define a couple of grey points on the line
        dot_0_5_0_5 = Dot().move_to(axes.c2p(0.5, 0.5)).set_color(GRAY)
        dot_1_5_1_5 = Dot().move_to(axes.c2p(1.5, 1.5)).set_color(GRAY)
        dot_2_5_2_5 = Dot().move_to(axes.c2p(2.5, 2.5)).set_color(GRAY)

        self.play(DrawBorderThenFill(dot_0_5_0_5), DrawBorderThenFill(dot_1_1), DrawBorderThenFill(dot_1_5_1_5), DrawBorderThenFill(dot_2_5_2_5))

        # Fade everything except the points on the graph
        self.play(
            FadeOut(axes),
            FadeOut(line),
            FadeOut(line_label),
            FadeOut(recover_text),
            FadeOut(point_label_0_0),
            FadeOut(point_label_2_2),
            FadeOut(point_label_3_3),
            dot_0_0.animate.set_color(GRAY),
        )



        """
            dot_0_0, dot_0_5_0_5, dot_1_1, dot_1_5_1_5, dot_2_2, dot_2_5_2_5, dot_3_3

            "2 out of N people can recover the secret"
        """

        # Define the positions for the dots on the first and second lines
        first_line_y = 4
        second_line_y = 2

        # Define the starting x-coordinate and the spacing between the dots
        start_x = 0  # Adjusted to move further right
        spacing = 0.8

        # List of grey dots
        grey_dots = [dot_0_0, dot_0_5_0_5, dot_1_1, dot_1_5_1_5, dot_2_5_2_5]

        # Calculate target positions for all grey dots
        target_positions_grey = [axes.c2p(start_x + i * spacing, second_line_y) for i in range(len(grey_dots))]

        # Target positions for the red dots
        target_position_dot_2_2 = axes.c2p(1, first_line_y)
        target_position_dot_3_3 = axes.c2p(2, first_line_y)

        # Move all dots (red and grey) to their target positions simultaneously
        self.play(
            dot_2_2.animate.move_to(target_position_dot_2_2),
            dot_3_3.animate.move_to(target_position_dot_3_3),
            *[dot.animate.move_to(target) for dot, target in zip(grey_dots, target_positions_grey)]
        )

        # Display the heading above the two lines of dots
        heading = MathTex(r"\text{2 out of N people can recover the secret}", color=WHITE).scale(0.8).move_to(UP * 3.5)
        self.play(Write(heading))

        self.wait(2)



        # Total width available on the screen (assuming a width of 7 units from -3.5 to 3.5)
        total_width = 4

        # Calculate the spacing for the red and grey dots
        num_red_dots = 3  # 2 original red dots + 1 grey dot that turns red
        num_grey_dots = 4  # 5 original grey dots - 1 grey dot that turns red

        spacing_red = total_width / (num_red_dots + 1)  # +1 to account for the starting space
        spacing_grey = total_width / (num_grey_dots + 1)

        # Define the starting x-coordinate (center-aligned)
        start_x_red = (-total_width / 4 + spacing_red) + 0.5
        start_x_grey = (-total_width / 4 + spacing_grey) + 0.5

        # List of grey dots excluding the middle dot
        grey_dots = [dot_0_0, dot_0_5_0_5, dot_1_5_1_5, dot_2_5_2_5]

        # Calculate target positions for the grey dots
        target_positions_grey = [axes.c2p(start_x_grey + i * spacing_grey, second_line_y) for i in range(num_grey_dots)]

        # Target positions for the red dots and the middle grey dot
        target_positions_red = [
            axes.c2p(start_x_red, first_line_y),
            axes.c2p(start_x_red + spacing_red, first_line_y),
            axes.c2p(start_x_red + 2 * spacing_red, first_line_y)
        ]

        # Move all dots (red and the middle grey dot) to their target positions simultaneously
        self.play(
            dot_2_2.animate.move_to(target_positions_red[0]),
            dot_3_3.animate.move_to(target_positions_red[2]),
            dot_1_1.animate.move_to(target_positions_red[1]).set_color(RED),  # Move and change color of dot_1_1
            *[dot.animate.move_to(target) for dot, target in zip(grey_dots, target_positions_grey)]
        )

        # Update the heading above the two lines of dots
        three_of_n_heading = MathTex(r"\text{3 out of N people can recover the secret}", color=WHITE).scale(0.8).move_to(UP * 3.5)
        self.play(Transform(heading, three_of_n_heading))

        self.wait(2)



        self.play(Create(axes))

        # 3. Simultaneously, move the red dots to (0,1), (1,0), (2,1)
        target_position_dot_2_2 = axes.c2p(0, 1)
        target_position_dot_1_1 = axes.c2p(1, 0)  # This was previously a grey dot, but now it's red
        target_position_dot_3_3 = axes.c2p(2, 1)

        self.play(
            *[FadeOut(dot) for dot in grey_dots],
            dot_2_2.animate.move_to(target_position_dot_2_2),
            dot_1_1.animate.move_to(target_position_dot_1_1),
            dot_3_3.animate.move_to(target_position_dot_3_3)
        )

        # Step 4: Draw a smooth curve through the points (0,1), (1,0), and (2,1)
        curve_points = [axes.c2p(0, 1), axes.c2p(0.5, 0.25), axes.c2p(1, 0), axes.c2p(1.5, 0.25), axes.c2p(2, 1), axes.c2p(2.5, 2.25), axes.c2p(3, 4)]
        curve = VMobject()
        curve.set_points_as_corners([*curve_points])
        curve.make_smooth()
        curve.set_color(GREEN)
        self.play(Create(curve))
        self.wait(2)

        secret_text = MathTex(r"\text{Secret: 1}", color=WHITE).scale(0.8).move_to(UP * 3.5)
        # convert three_of_n_heading to secret_text
        self.play(Transform(heading, secret_text))

        # Transform "1" in "Secret: 1" to "(0,1)" label on the graph
        point_label_0_1 = MathTex("(0,", "1", ")").set_color(WHITE).move_to(axes.c2p(0, 1)).shift(0.5*(DOWN + LEFT)).scale(0.9)
        point_label_0_1[1].set_color(GREEN)  # Set y-coordinate "0" to green
        dot_0_1 = Dot(point=axes.c2p(0, 1), color=GREEN)
        self.play(DrawBorderThenFill(dot_0_1), Transform(heading, point_label_0_1))
        self.wait(2)






        # Create the word "Randomness" using two separate MathTex objects
        randomness_text_part1 = MathTex("Rando", color=WHITE).scale(1.2)
        randomness_text_part2 = MathTex("mness", color=WHITE).scale(1.2)

        # Position them closely to make them appear as a single word
        randomness_text_part2.next_to(randomness_text_part1, RIGHT, buff=0)

        # Group the two parts using VGroup for easier manipulation
        randomness_group = VGroup(randomness_text_part1, randomness_text_part2)

        # Display the grouped randomness text
        self.play(Write(randomness_group))
        self.wait(1)

        # Define the point labels for (1,0) and (2,1)
        point_label_1_0 = MathTex("(1,0)").set_color(WHITE).move_to(axes.c2p(1, 0)).shift(0.5*(DOWN + RIGHT))
        point_label_2_1 = MathTex("(2,1)").set_color(WHITE).move_to(axes.c2p(2, 1)).shift(0.5*(DOWN + RIGHT))

        # Transform each part of the randomness_group to the respective point labels
        self.play(
            Transform(randomness_text_part1, point_label_1_0),
            Transform(randomness_text_part2, point_label_2_1),
            dot_1_1.animate.set_color(GRAY),
            dot_3_3.animate.set_color(GRAY),
        )
        self.wait(2)


        line_label = MathTex(r"\text{Secret Quadratic Curve}").set_color(WHITE).scale(0.7)
        self.play(Write(line_label))

        dot_0_5 = Dot(point=axes.c2p(0.5, 0.25), color=GRAY)
        dot_1_5 = Dot(point=axes.c2p(1.5, 0.25), color=GRAY)
        dot_2_5 = Dot(point=axes.c2p(2.5, 2.25), color=GRAY)
        dot_3_4 = Dot(point=axes.c2p(3, 4), color=GRAY)

        self.play(DrawBorderThenFill(dot_0_5), DrawBorderThenFill(dot_1_5), DrawBorderThenFill(dot_2_5), DrawBorderThenFill(dot_3_4))
        self.wait(2)

        # fade out everything except the the (1,0), (2,1), (3,4) points
        # self.play(FadeOut(randomness_group), FadeOut(dot_0_1), FadeOut(point_label_0_1), FadeOut(dot_2_2), FadeOut(point_label_2_2), FadeOut(dot_3_3), FadeOut(point_label_3_3), FadeOut(line_label), FadeOut(dot_1_1), FadeOut(point_label_1_1), FadeOut(curve), FadeOut(axes))
        self.play(
            FadeOut(curve),
            FadeOut(line_label),
            FadeOut(dot_2_2),
            FadeOut(dot_0_1),
            FadeOut(dot_0_5),
            FadeOut(dot_1_5),
            FadeOut(dot_2_5),
            FadeOut(randomness_text_part1),
            FadeOut(randomness_text_part2),
            FadeOut(heading),
            dot_1_1.animate.set_color(RED),
            dot_3_3.animate.set_color(RED),
            dot_3_4.animate.set_color(RED),
        )

        line_label = MathTex(r"\text{Reconstructed Secret Quadratic Curve}").set_color(WHITE).scale(0.7)

        self.play(Create(curve), Write(line_label))
        self.wait(1)
        self.play(Write(heading), DrawBorderThenFill(dot_0_1))
        self.wait(2)

        # fade everything including axes and recap
        self.play(FadeOut(curve), FadeOut(line_label), FadeOut(heading), FadeOut(dot_0_1), FadeOut(dot_1_1), FadeOut(dot_3_3), FadeOut(dot_3_4), FadeOut(axes))

        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))

        self.wait(1)

        self.play(FadeOut(recap_text))









        # Create the axes
        axes = Axes(
            x_range=[0, 3],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )
        self.play(Create(axes))

        # Highlight the points (1,0) and (2,1) as red dots
        dot_1_0 = Dot(point=axes.c2p(1, 0), color=RED)
        dot_2_1 = Dot(point=axes.c2p(2, 1), color=RED)
        self.play(DrawBorderThenFill(dot_1_0), DrawBorderThenFill(dot_2_1))

        # Add labels for the points
        label_1_0 = MathTex("(1,0)").set_color(RED).next_to(dot_1_0, DOWN)
        label_2_1 = MathTex("(2,1)").set_color(RED).next_to(dot_2_1, UP)
        self.play(Write(label_1_0), Write(label_2_1))

        # Define the control points for the quadratic curves
        control_points = [
            [axes.c2p(0, -1), axes.c2p(1, 0), axes.c2p(2, 1), axes.c2p(3, 2)],
            [axes.c2p(0, 1), axes.c2p(1, 0), axes.c2p(2, 1), axes.c2p(3, 1)],
            [axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(2, 1), axes.c2p(3, 0)],
            [axes.c2p(0, -2), axes.c2p(1, 0), axes.c2p(2, 1), axes.c2p(3, -1)]
        ]

        y_intercepts = [-1, 1, 0, -2]  # y-axis intercepts for the curves
        y_intercept_labels = []

        # Draw the quadratic curves
        curves = []
        for points in control_points:
            curve = VMobject()
            curve.set_points_smoothly(points)
            curve.set_color(BLUE)
            self.play(Create(curve))
            curves.append(curve)

        # Label the y-axis intercepts for all curves at once
        for i, y_intercept in enumerate(y_intercepts):
            y_intercept_label = MathTex(f"({0},{y_intercept})").next_to(axes.c2p(0, y_intercept), LEFT)
            self.play(Write(y_intercept_label), run_time=0.5)
            y_intercept_labels.append(y_intercept_label)

        # Fade out everything except the (1,0), (2,1) dots and labels, and the axes
        self.play(
            *[FadeOut(curve) for curve in curves],
            *[FadeOut(label) for label in y_intercept_labels]
        )

        self.wait(2)

        # Highlight the point (0,1) as a green dot
        dot_0_1 = Dot(point=axes.c2p(0, 1), color=GREEN)

        # Add label for the point (0,1)
        label_0_1 = MathTex("(0,1)").set_color(GREEN).next_to(dot_0_1, RIGHT)
        self.play(DrawBorderThenFill(dot_0_1), Write(label_0_1))

        # Step 4: Draw a smooth curve through the points (0,1), (1,0), and (2,1)
        curve_points = [axes.c2p(0, 1), axes.c2p(0.5, 0.25), axes.c2p(1, 0), axes.c2p(1.5, 0.25), axes.c2p(2, 1), axes.c2p(2.5, 2.25), axes.c2p(3, 4)]
        curve = VMobject()
        curve.set_points_as_corners([*curve_points])
        curve.make_smooth()
        curve.set_color(GREEN)
        self.play(Create(curve))
        self.wait(2)

        # Write a text saying "Any 3 points can be used to recover the secret curve and point" at the top
        recover_text = MathTex(r"\text{Any 3 points can be used to recover the secret curve and point}").set_color(WHITE).scale(0.7).shift(3*UP)
        self.play(Write(recover_text))


        # fade everything
        self.play(
            FadeOut(curve),
            FadeOut(recover_text),
            FadeOut(dot_0_1),
            FadeOut(label_0_1),
            FadeOut(dot_1_0),
            FadeOut(dot_2_1),
            FadeOut(label_1_0),
            FadeOut(label_2_1),
            FadeOut(axes)
        )


        # Create the heading
        heading = Text("Pattern", font_size=36).shift(UP*3.5)

        # Create the table
        table = Table(
            [["1", "2"],
             ["2", "3"],
             ["3", "4"],
             ["4", "5"],
             ["n", "n+1 shares"]],
            col_labels=[Tex("polynomial degree", font_size=48), Tex("min. number of shares needed to recover the secret", font_size=48)],
            include_outer_lines=True
        ).scale(0.7)

        # Align the table below the heading
        table.next_to(heading, DOWN, buff=0.3)

        # Create the curve annotations
        line_annotation = Text("Line", font_size=22).next_to(table.get_rows()[1], RIGHT, buff=1)
        quadratic_annotation = Text("Quadratic Curve", font_size=22).next_to(table.get_rows()[2], RIGHT, buff=1)
        cubic_annotation = Text("Cubic Curve", font_size=22).next_to(table.get_rows()[3], RIGHT, buff=1)
        quartic_annotation = Text("Quartic Curve", font_size=22).next_to(table.get_rows()[4], RIGHT, buff=1)
        nth_degree_annotation = Text("nth Degree Curve", font_size=22).next_to(table.get_rows()[5], RIGHT, buff=1)

        # Add everything to the scene
        self.play(Write(heading))
        self.play(Create(table))
        self.play(Write(line_annotation))
        self.play(Write(quadratic_annotation))
        self.play(Write(cubic_annotation))
        self.play(Write(quartic_annotation))
        self.play(Write(nth_degree_annotation))

        self.wait(2)


        # fade everything
        self.play(
            FadeOut(table),
            FadeOut(line_annotation),
            FadeOut(quadratic_annotation),
            FadeOut(cubic_annotation),
            FadeOut(quartic_annotation),
            FadeOut(nth_degree_annotation),
            FadeOut(heading)
        )

        # Recap text
        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))

        self.wait(1)

        