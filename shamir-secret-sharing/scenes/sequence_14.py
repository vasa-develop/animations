from manim import *

class Sequence14(Scene):
    
    def construct(self):
        """
        TODO: Add animation for 
        
        Now, in theory this seems like a perfect system to share secrets.
        Let’s try to go through a practical example and see if this works
        as we expect it to work.
        """

        # Create Axes
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 5],
            axis_config={"color": WHITE},
        )

        dot_1 = Dot().set_color(GREEN).move_to(axes.c2p(0, 0))
        dot_2 = Dot().set_color(GRAY).move_to(axes.c2p(1, 1/3))
        dot_3 = Dot().set_color(GRAY).move_to(axes.c2p(3, 1))

        # Create label for y-intercept value
        dot_1_label = MathTex(r"(0,0)").next_to(dot_1, DOWN, buff=0.1)
        dot_2_label = MathTex(r"(1,1/3)").next_to(dot_2, UP, buff=0.1)

        line = Line(dot_1.get_center(), dot_3.get_center()).set_color(GREEN)

        self.play(Create(axes))
        self.play(
            Create(dot_1),
            Create(dot_2),
            Write(dot_1_label),
            Write(dot_2_label),
        )
        self.play(Create(line))
        self.add(axes, dot_1, dot_2, dot_1_label, dot_2_label, line)

        group = VGroup(axes, dot_1, dot_2, dot_1_label, dot_2_label, line)


        code = '''class Line:
    def s_x(x):
        return x/3
'''
        rendered_code_1 = Code(
            code=code,
            tab_width=2,
            background="window",
            language="Python",
            font="Monospace",
            font_size=18,
            style=Code.styles_list[13],
        )
        self.play(
            Transform(group, rendered_code_1),
        )

        code = '''class Line:
    def s_x(x):
        return x/3
    
    print(s_x(3))   # 1.0
    print(s_x(1))   # 0.3333333333333333
'''
        rendered_code_2 = Code(
            code=code,
            tab_width=2,
            background="window",
            language="Python",
            font="Monospace",
            font_size=18,
            style=Code.styles_list[13],
        )
        self.play(Transform(rendered_code_1, rendered_code_2))



        code = '''class Line:
    def s_x(x):
        return x/3
    
    print(s_x(3))   # 1.0
    print(s_x(1))   # 0.3333333333333333
    print('{0:.60f}'.format(s_x(1)))
    # 0.333333333333333314829616256247390992939472198486328125
'''
        rendered_code_2 = Code(
            code=code,
            tab_width=2,
            background="window",
            language="Python",
            font="Monospace",
            font_size=18,
            style=Code.styles_list[13],
        )
        self.play(Transform(rendered_code_1, rendered_code_2))


        floating_point_numbers_text = MathTex(r"\textbf{Floating Point Numbers}").scale(1.5).shift(3*DOWN)
        self.play(
            Write(floating_point_numbers_text)
        )















        self.wait(2)