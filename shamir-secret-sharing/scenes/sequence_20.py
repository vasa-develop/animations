from manim import *
import numpy as np
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence20(Scene):
    
    def construct(self):
        """
        This video mostly covered how we can use concepts like Lagrange interpolation to share secrets, but there are a lot of other applications.

        For example, we use it to encode and read data from CDs, QR codes, such that even if the CD gets scratched or QR codes are not fully visible, we can still recover the original data in perfect shape!
        """

        # fade in lagrange interpolation text
        lagrange_interpolation_text = MathTex(r"\textbf{Lagrange Interpolation}", color=BLUE).scale(1.5)
        self.play(Write(lagrange_interpolation_text))
        self.add(lagrange_interpolation_text)
        self.wait(1)

        data_encoding_n_recovery_text = MathTex(r"\textbf{Data Encoding and Recovery}", color=BLUE).scale(1.5)
        self.play(TransformMatchingShapes(lagrange_interpolation_text, data_encoding_n_recovery_text))
        self.add(data_encoding_n_recovery_text)
        self.remove(lagrange_interpolation_text)
        self.wait(1)

        data_to_be_encoded = MathTex(r"\textbf{Data to be encoded}", color=BLUE).scale(1).to_edge(UP).shift(0.5*DOWN)

        # Create a rectangle to represent the block of data
        data_block = RoundedRectangle(width=6, height=4, corner_radius=0.001, fill_opacity=1, fill_color=BLACK)
        self.play(
            TransformMatchingShapes(data_encoding_n_recovery_text, data_to_be_encoded),
            Create(data_block)
        )
        self.add(data_to_be_encoded, data_block)
        self.remove(data_encoding_n_recovery_text)
        self.wait(1)

        # Create a grid of 0s and 1s within the rectangle
        rows = 10  # Adjust the number of rows and columns to fit your desired density of 0s and 1s
        columns = 15
        binary_grid = VGroup()  # This will hold all the 0s and 1s
        for row in range(rows):
            for column in range(columns):
                binary_digit = Text(str(np.random.choice(["0", "1"])), font_size=20)  # Randomly choose 0 or 1
                # Position each digit within the rectangle based on the row and column indices
                binary_digit.move_to(data_block.get_corner(UL) + RIGHT * (column + 0.5) * (data_block.width / columns) + DOWN * (row + 0.5) * (data_block.height / rows))
                binary_grid.add(binary_digit)

        self.play(Create(binary_grid))
        self.add(binary_grid)
        self.wait(1)

        single_input_data_group = VGroup(data_block, binary_grid)

        # create a 5x2 grid of single input data groups
        grid = VGroup()
        for row in range(3):
            for column in range(2):
                single_input_data_group_copy = single_input_data_group.copy()
                single_input_data_group_copy.shift(RIGHT * (column + 0.5) * (single_input_data_group_copy.width + 1) + DOWN * (row + 0.5) * (single_input_data_group_copy.height + 1))
                grid.add(single_input_data_group_copy)


        # scale the grid to fit the screen and shift it to the left side of the screen
        input_grid = grid.copy().scale(0.3).shift(11.5*LEFT).shift(7*UP)
        output_grid = grid.copy().scale(0.3).shift(2.5*LEFT).shift(7*UP)


        self.play(
            TransformMatchingShapes(single_input_data_group, input_grid),
            data_to_be_encoded.animate.shift(0.7*DOWN + 4.5*LEFT).scale(0.7)
        )
        self.add(input_grid)
        self.remove(single_input_data_group)
        self.wait(1)

        input_grid_copy_1 = input_grid.copy()
        input_grid_copy_2 = input_grid.copy()


        disc = BootstrapSVGMobject('disc-fill', color=BLUE).shift(UP)
        qr_code = BootstrapSVGMobject('qr-code', color=BLUE).shift(2*DOWN)

        self.play(
            Transform(input_grid_copy_1, disc),
            Transform(input_grid_copy_2, qr_code),
        )
        self.add(disc, qr_code)
        self.remove(input_grid_copy_1, input_grid_copy_2)
        self.wait(1)

        # add some 3 zig-zag black scratch lines on the disc
        scratch_line_1 = Line(start=disc.get_corner(UL), end=disc.get_corner(DR), color=BLACK, stroke_width=6)
        scratch_line_2 = Line(start=disc.get_corner(UR), end=disc.get_corner(DL), color=BLACK, stroke_width=6)
        scratch_line_3 = Line(start=disc.get_corner(LEFT), end=disc.get_corner(RIGHT), color=BLACK, stroke_width=6)
        self.play(
            Create(scratch_line_1),
            Create(scratch_line_2),
            Create(scratch_line_3),
        )
        self.add(scratch_line_1, scratch_line_2, scratch_line_3)
        self.wait(1)
        

        # add some black blocks on the qr code (make sure they are on the qr code and do have black background and boundary). use the location of qr_code to place the black blocks
        black_block_1 = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.001, fill_opacity=1, fill_color=BLACK, stroke_color=BLACK).move_to(qr_code.get_corner(UL) + 0.25*RIGHT + 0.25*DOWN)
        black_block_2 = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.001, fill_opacity=1, fill_color=BLACK, stroke_color=BLACK).move_to(qr_code.get_corner(UR) + 0.25*LEFT + 0.25*DOWN)
        black_block_3 = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.001, fill_opacity=1, fill_color=BLACK, stroke_color=BLACK).move_to(qr_code.get_corner(DL) + 0.25*RIGHT + 0.25*UP)
        black_block_4 = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.001, fill_opacity=1, fill_color=BLACK, stroke_color=BLACK).move_to(qr_code.get_corner(DR) + 0.25*LEFT + 0.25*UP)
        self.play(
            Create(black_block_1),
            Create(black_block_2),
            Create(black_block_3),
            Create(black_block_4),
        )
        self.add(black_block_1, black_block_2, black_block_3, black_block_4)
        self.wait(1)

        disc_copy = disc.copy()
        qr_code_copy = qr_code.copy()
        copy_group = VGroup(disc_copy, qr_code_copy)



        decoded_data = MathTex(r"\textbf{Decoded data}", color=BLUE).scale(0.7).to_edge(UP).shift(1.2*DOWN + 4.5*RIGHT)

        self.play(
            Transform(copy_group, output_grid),
            DrawBorderThenFill(decoded_data)
        )
        self.add(output_grid, decoded_data)
        self.remove(copy_group)

        self.play(
            Indicate(input_grid, scale_factor=1.05, color=GREEN),
            Indicate(output_grid, scale_factor=1.05, color=GREEN),
        )

        # fade everything out
        final_group = VGroup(
            input_grid, output_grid, data_to_be_encoded, decoded_data, scratch_line_1, scratch_line_2, scratch_line_3, black_block_1, black_block_2, black_block_3, black_block_4,
            disc, qr_code
        )

        secure_multiparty_computation_text = MathTex(r"\textbf{Secure Multiparty Computation}", color=BLUE).scale(1.5).to_edge(UP).shift(DOWN)
        reed_solomon_code_text = MathTex(r"\textbf{Reed-Solomon Code}", color=BLUE).scale(1.5).next_to(secure_multiparty_computation_text, DOWN, buff=1)
        polynomial_commitments_text = MathTex(r"\textbf{Polynomial Commitments}", color=BLUE).scale(1.5).next_to(reed_solomon_code_text, DOWN, buff=1)
        zero_knowledge_proofs_text = MathTex(r"\textbf{Zero-Knowledge Proofs}", color=BLUE).scale(1.5).next_to(polynomial_commitments_text, DOWN, buff=1)
        ideas_group = VGroup(secure_multiparty_computation_text, reed_solomon_code_text, polynomial_commitments_text, zero_knowledge_proofs_text)

        # add a bulb lightbulb bootstrap icon in the center of the screen and place the 4 texts on each side of the lightbulb
        lightbulb = BootstrapSVGMobject('lightbulb-fill', color=YELLOW).scale(0.5)
        self.play(Transform(final_group, lightbulb))
        self.add(lightbulb)
        self.remove(final_group)
        self.wait(1)

        self.play(
            Transform(lightbulb, ideas_group),
        )
        self.add(ideas_group)
        self.remove(lightbulb)

        self.play(
            FadeOut(ideas_group),
            run_time=3
        )

        self.wait(2)