from manim import *

class Example(Scene):
    def construct(self):
        
        single_digit_table = Table(
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

        single_digit_table.add_highlighted_cell((1,2), color=PURPLE)
        
        single_digit_table.add_highlighted_cell((2,1), color=PURPLE)
        single_digit_table.add_highlighted_cell((3,1), color=PURPLE)
        single_digit_table.add_highlighted_cell((4,1), color=PURPLE)
        single_digit_table.add_highlighted_cell((5,1), color=PURPLE)
        single_digit_table.add_highlighted_cell((6,1), color=PURPLE)
        single_digit_table.add_highlighted_cell((7,1), color=PURPLE)
        # single_digit_table.add_highlighted_cell((8,1), color=PURPLE)
        # single_digit_table.add_highlighted_cell((9,1), color=PURPLE)
        # single_digit_table.add_highlighted_cell((10,1), color=PURPLE)
        # single_digit_table.add_highlighted_cell((11,1), color=PURPLE)

        self.add(single_digit_table)








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
        # table.add_highlighted_cell((1,8), color=PURPLE)
        # table.add_highlighted_cell((1,9), color=PURPLE)
        # table.add_highlighted_cell((1,10), color=PURPLE)
        # table.add_highlighted_cell((1,11), color=PURPLE)

        
        table.add_highlighted_cell((2,1), color=PURPLE)
        table.add_highlighted_cell((3,1), color=PURPLE)
        table.add_highlighted_cell((4,1), color=PURPLE)
        table.add_highlighted_cell((5,1), color=PURPLE)
        table.add_highlighted_cell((6,1), color=PURPLE)
        table.add_highlighted_cell((7,1), color=PURPLE)
        # table.add_highlighted_cell((8,1), color=PURPLE)
        # table.add_highlighted_cell((9,1), color=PURPLE)
        # table.add_highlighted_cell((10,1), color=PURPLE)
        # table.add_highlighted_cell((11,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(8):
            for j in range(8):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_6(i-2, j-2) == "1":
                        print(i, j)
                        if i != 1 and j != 1:
                            table.add_highlighted_cell((i,j), color=GREEN)


        #self.add(table)

