from manim import *
import numpy as np
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence12(Scene):

    def draw_curve(self, curve_points, color=RED):
        curve = VMobject()
        curve.set_points_as_corners([*curve_points])
        curve.make_smooth()
        curve.set_color(color)

        curve_light = VMobject()
        curve_light.set_points_as_corners([*curve_points])
        curve_light.make_smooth()
        curve_light.set_stroke(color=color, opacity=0.2)

        return curve, curve_light



    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[0, 5],
            y_range=[0, 20],
            axis_config={"color": WHITE},
        )
        axes.scale(0.7).shift(DOWN)
        labels = axes.get_axis_labels(
            MathTex(r"\textbf{x}").scale(0.7), 
            MathTex(r"\textbf{y}").scale(0.7)
        )

        s_dot_1 = Dot(point=axes.c2p(1, 4), color=RED)
        s_dot_2 = Dot(point=axes.c2p(2, 9), color=RED)
        s_dot_3 = Dot(point=axes.c2p(3, 16), color=RED)

        s_label_1 = Tex(r"(1, 4)").scale(0.7).next_to(s_dot_1, UP)
        s_label_2 = Tex(r"(2, 9)").scale(0.7).next_to(s_dot_2, UP+LEFT)
        s_label_3 = Tex(r"(3, 16)").scale(0.7).next_to(s_dot_3, UP+LEFT)

        self.play(
            Create(axes),
            Create(labels),
            DrawBorderThenFill(s_dot_1),
            DrawBorderThenFill(s_dot_2),
            DrawBorderThenFill(s_dot_3),
            Write(s_label_1),
            Write(s_label_2),
            Write(s_label_3),
        )
        self.add(axes, s_dot_1, s_dot_2, s_dot_3, s_label_1, s_label_2, s_label_3)
        self.wait(0.5)

        def s_x_values(x):
            return (x+1)**2

        curve_points = [axes.c2p(i, s_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=RED)
        s_curve = curves[0]
        s_curve_light = curves[1]
        self.play(Create(s_curve))
        self.add(s_curve, s_curve_light)
        self.wait(0.5)


        # Define the coordinate pairs
        s_coordinates = [(1, 4), (2, 9), (3, 16)]
        
        # Create the coordinate pairs as a list of Tex objects
        s_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in s_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        s_left_brace = Brace(s_coordinate_pairs, direction=LEFT)

        s_equal_to = MathTex(r"=").next_to(s_left_brace, LEFT)
        s_x = MathTex(r"s(x)").scale(1.5).shift(3*UP).shift(6*LEFT).set_color(RED)
        s_x.next_to(s_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        s_function_representation = VGroup(
            s_x,
            s_equal_to,
            s_left_brace,
            s_coordinate_pairs
        )
        s_function_representation.scale(1).shift(2*UP)

        self.play(
            Transform(s_curve, s_x),
            s_dot_1.animate.set_opacity(0.2),
            s_dot_2.animate.set_opacity(0.2),
            s_dot_3.animate.set_opacity(0.2),
            # FadeOut(dot_1),
            # FadeOut(dot_2),
            # FadeOut(dot_3),
        ) 
        self.add(s_x)
        self.remove(s_curve)
        self.wait(0.5)

        group = VGroup(s_x, s_label_1, s_label_2, s_label_3)

        # Display the function representation
        self.play(TransformMatchingShapes(group, s_function_representation))
        self.add(s_function_representation)
        self.remove(group)
        self.wait(0.5)

        self.play(
            s_function_representation.animate.scale(0.6).shift(UP).shift(4*LEFT)
        )











        f_dot_1 = Dot(point=axes.c2p(1, 4), color=YELLOW)
        f_dot_2 = Dot(point=axes.c2p(2, 0), color=YELLOW)
        f_dot_3 = Dot(point=axes.c2p(3, 0), color=YELLOW)

        f_label_1 = Tex(r"(1, 4)").scale(0.7).next_to(f_dot_1, UP)
        f_label_2 = Tex(r"(2, 0)").scale(0.7).next_to(f_dot_2, UP)
        f_label_3 = Tex(r"(3, 0)").scale(0.7).next_to(f_dot_3, UP)

        self.play(
            DrawBorderThenFill(f_dot_1),
            DrawBorderThenFill(f_dot_2),
            DrawBorderThenFill(f_dot_3),
            Write(f_label_1),
            Write(f_label_2),
            Write(f_label_3),
        )
        self.add(f_dot_1, f_dot_2, f_dot_3, f_label_1, f_label_2, f_label_3)
        self.wait(0.5)

        def f_x_values(x):
            return (x-2)*(x-3)*2

        curve_points = [axes.c2p(i, f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        f_curve = curves[0]
        f_curve_light = curves[1]
        self.play(Create(f_curve))
        self.add(f_curve, f_curve_light)
        self.wait(0.5)

        # Define the coordinate pairs
        f_coordinates = [(1, 4), (2, 0), (3, 0)]
        
        # Create the coordinate pairs as a list of Tex objects
        f_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in f_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        f_left_brace = Brace(f_coordinate_pairs, direction=LEFT)

        f_equal_to = MathTex(r"=").scale(1.5).next_to(f_left_brace, LEFT)
        f_x = MathTex(r"f(x)").scale(1.5).shift(3*UP).set_color(YELLOW)
        f_x.next_to(f_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        f_function_representation = VGroup(
            f_x,
            f_equal_to,
            f_left_brace,
            f_coordinate_pairs
        )
        f_function_representation.scale(0.6).shift(3*UP).shift(0.5*LEFT)
        
        group = VGroup(f_label_1, f_label_2, f_label_3)

        self.play(
            Transform(f_curve, f_x),
            TransformMatchingShapes(group, f_function_representation),
            f_dot_1.animate.set_opacity(0.2),
            f_dot_2.animate.set_opacity(0.2),
            f_dot_3.animate.set_opacity(0.2),
            # FadeOut(dot_1),
            # FadeOut(dot_2),
            # FadeOut(dot_3),
        )
        self.add(f_x, f_function_representation)
        self.remove(f_curve, group)
        self.wait(0.5)













        g_dot_1 = Dot(point=axes.c2p(1, 0), color=GREEN)
        g_dot_2 = Dot(point=axes.c2p(2, 9), color=GREEN)
        g_dot_3 = Dot(point=axes.c2p(3, 0), color=GREEN)

        g_label_1 = Tex(r"(1, 0)").scale(0.7).next_to(g_dot_1, UP+LEFT)
        g_label_2 = Tex(r"(2, 9)").scale(0.7).next_to(g_dot_2, UP)
        g_label_3 = Tex(r"(3, 0)").scale(0.7).next_to(g_dot_3, UP+RIGHT)

        self.play(
            DrawBorderThenFill(g_dot_1),
            DrawBorderThenFill(g_dot_2),
            DrawBorderThenFill(g_dot_3),
            Write(g_label_1),
            Write(g_label_2),
            Write(g_label_3),
        )
        self.add(g_dot_1, g_dot_2, g_dot_3, g_label_1, g_label_2, g_label_3)
        self.wait(0.5)

        def g_x_values(x):
            return (x-1)*(x-3)*(-9)
        
        curve_points = [axes.c2p(i, g_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        g_curve = curves[0]
        g_curve_light = curves[1]
        self.play(Create(g_curve))
        self.add(g_curve, g_curve_light)
        self.wait(0.5)

        # Define the coordinate pairs
        g_coordinates = [(1, 0), (2, 9), (3, 0)]
        
        # Create the coordinate pairs as a list of Tex objects
        g_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in g_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        g_left_brace = Brace(g_coordinate_pairs, direction=LEFT)

        g_equal_to = MathTex(r"=").scale(1.5).next_to(g_left_brace, LEFT)
        g_x = MathTex(r"g(x)").scale(1.5).shift(2*UP).set_color(GREEN)
        g_x.next_to(g_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        g_function_representation = VGroup(
            g_x,
            g_equal_to,
            g_left_brace,
            g_coordinate_pairs
        )
        g_function_representation.scale(0.6).shift(3*UP).shift(3*RIGHT)
        
        group = VGroup(g_label_1, g_label_2, g_label_3)

        self.play(
            Transform(g_curve, g_x),
            TransformMatchingShapes(group, g_function_representation),
            g_dot_1.animate.set_opacity(0.2),
            g_dot_2.animate.set_opacity(0.2),
            g_dot_3.animate.set_opacity(0.2),
            # FadeOut(dot_1),
            # FadeOut(dot_2),
            # FadeOut(dot_3),
        )
        self.add(g_x, g_function_representation)
        self.remove(g_curve, group)
        self.wait(0.5)











        h_dot_1 = Dot(point=axes.c2p(1, 0), color=BLUE)
        h_dot_2 = Dot(point=axes.c2p(2, 0), color=BLUE)
        h_dot_3 = Dot(point=axes.c2p(3, 16), color=BLUE)

        h_label_1 = Tex(r"(1, 0)").scale(0.7).next_to(h_dot_1, UP+0.2*RIGHT)
        h_label_2 = Tex(r"(2, 0)").scale(0.7).next_to(h_dot_2, UP)
        h_label_3 = Tex(r"(3, 16)").scale(0.7).next_to(h_dot_3, UP+LEFT)

        self.play(
            DrawBorderThenFill(h_dot_1),
            DrawBorderThenFill(h_dot_2),
            DrawBorderThenFill(h_dot_3),
            Write(h_label_1),
            Write(h_label_2),
            Write(h_label_3),
        )
        self.add(h_dot_1, h_dot_2, h_dot_3, h_label_1, h_label_2, h_label_3)
        self.wait(0.5)

        def h_x_values(x):
            return (x-1)*(x-2)*(8)
        
        curve_points = [axes.c2p(i, h_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=BLUE)
        h_curve = curves[0]
        h_curve_light = curves[1]
        self.play(Create(h_curve))
        self.add(h_curve, h_curve_light)
        self.wait(0.5)


        # Define the coordinate pairs
        h_coordinates = [(1, 0), (2, 0), (3, 16)]
        
        # Create the coordinate pairs as a list of Tex objects
        h_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in h_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        h_left_brace = Brace(h_coordinate_pairs, direction=LEFT)

        h_equal_to = MathTex(r"=").scale(1.5).next_to(h_left_brace, LEFT)
        h_x = MathTex(r"h(x)").scale(1.5).shift(2*UP).set_color(BLUE)
        h_x.next_to(h_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        h_function_representation = VGroup(
            h_x,
            h_equal_to,
            h_left_brace,
            h_coordinate_pairs
        )
        h_function_representation.scale(0.6).shift(3*UP).shift(6.5*RIGHT)
        
        group = VGroup(h_label_1, h_label_2, h_label_3)

        self.play(
            Transform(h_curve, h_x),
            TransformMatchingShapes(group, h_function_representation),
            h_dot_1.animate.set_opacity(0.2),
            h_dot_2.animate.set_opacity(0.2),
            h_dot_3.animate.set_opacity(0.2),
            # FadeOut(dot_1),
            # FadeOut(dot_2),
            # FadeOut(dot_3),
        )
        self.add(h_x, h_function_representation)
        self.remove(h_curve, group)
        self.wait(0.5)


        rect_height = h_coordinate_pairs.get_height() / 3
        rect_width = h_coordinate_pairs.get_width() + 0.2
        s_rect = Rectangle(height=rect_height, width=rect_width, color=RED).next_to(s_coordinate_pairs[-1], UP, buff=0).align_to(s_coordinate_pairs[0], DOWN).shift(0.1*DOWN)
        f_rect = Rectangle(height=rect_height, width=rect_width, color=YELLOW).next_to(f_coordinate_pairs[-1], UP, buff=0).align_to(f_coordinate_pairs[0], DOWN).shift(0.1*DOWN)
        g_rect = Rectangle(height=rect_height, width=rect_width, color=GREEN).next_to(g_coordinate_pairs[-1], UP, buff=0).align_to(g_coordinate_pairs[0], DOWN).shift(0.1*DOWN)
        h_rect = Rectangle(height=rect_height, width=rect_width, color=BLUE).next_to(h_coordinate_pairs[-1], UP, buff=0).align_to(h_coordinate_pairs[0], DOWN).shift(0.1*DOWN)
        
        self.play(
            Create(s_rect),
            Create(f_rect),
            Create(g_rect),
            Create(h_rect),
            s_dot_1.animate.set_opacity(1),
            f_dot_1.animate.set_opacity(1),
            g_dot_1.animate.set_opacity(1),
            h_dot_1.animate.set_opacity(1),
        )
        self.add(s_rect, f_rect, g_rect, h_rect)
        self.wait(0.5)

        self.play(
            s_rect.animate.shift(0.55*DOWN),
            f_rect.animate.shift(0.55*DOWN),
            g_rect.animate.shift(0.55*DOWN),
            h_rect.animate.shift(0.55*DOWN),
            s_dot_1.animate.set_opacity(0.2),
            f_dot_1.animate.set_opacity(0.2),
            g_dot_1.animate.set_opacity(0.2),
            h_dot_1.animate.set_opacity(0.2),
            s_dot_2.animate.set_opacity(1),
            f_dot_2.animate.set_opacity(1),
            g_dot_2.animate.set_opacity(1),
            h_dot_2.animate.set_opacity(1),
        )
        self.wait(0.5)

        self.play(
            s_rect.animate.shift(0.55*DOWN),
            f_rect.animate.shift(0.55*DOWN),
            g_rect.animate.shift(0.55*DOWN),
            h_rect.animate.shift(0.55*DOWN),
            s_dot_2.animate.set_opacity(0.2),
            f_dot_2.animate.set_opacity(0.2),
            g_dot_2.animate.set_opacity(0.2),
            h_dot_2.animate.set_opacity(0.2),
            s_dot_3.animate.set_opacity(1),
            f_dot_3.animate.set_opacity(1),
            g_dot_3.animate.set_opacity(1),
            h_dot_3.animate.set_opacity(1),
        )
        self.wait(0.5)

        self.play(
            FadeOut(s_rect),
            FadeOut(f_rect),
            FadeOut(g_rect),
            FadeOut(h_rect),
            s_dot_3.animate.set_opacity(0.2),
            f_dot_3.animate.set_opacity(0.2),
            g_dot_3.animate.set_opacity(0.2),
            h_dot_3.animate.set_opacity(0.2),
        )
        self.remove(s_rect, f_rect, g_rect, h_rect)
        self.wait(0.5)

        self.play(
            s_function_representation.animate.shift(0.5*LEFT),
            g_function_representation.animate.set_opacity(0.2),
            h_function_representation.animate.set_opacity(0.2),

            f_curve_light.animate.set_stroke(opacity=1),
            f_dot_1.animate.set_opacity(1),
            f_dot_2.animate.set_opacity(1),
            f_dot_3.animate.set_opacity(1),
            f_label_1.animate.set_opacity(1),
            f_label_2.animate.set_opacity(1),
            f_label_3.animate.set_opacity(1),
        )
        self.wait(0.5)



        
        
        new_f_coordinates = [(1, 1), (2, 0), (3, 0)]

        # Create the coordinate pairs as a list of Tex objects
        new_f_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in new_f_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        new_f_left_brace = Brace(new_f_coordinate_pairs, direction=LEFT)

        new_f_coefficient = MathTex(r"4 \times").scale(1).next_to(new_f_left_brace, LEFT)
        new_f_equal_to = MathTex(r"=").scale(1.5).next_to(new_f_coefficient, LEFT)
        new_f_x = MathTex(r"f(x)").scale(1.5).shift(3*UP).set_color(YELLOW)
        new_f_x.next_to(new_f_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        new_f_function_representation = VGroup(
            new_f_x,
            new_f_coefficient,
            new_f_equal_to,
            new_f_left_brace,
            new_f_coordinate_pairs
        )
        new_f_function_representation.scale(0.6).shift(3*UP).shift(0.5*LEFT)
    

        self.play(
            TransformMatchingShapes(f_function_representation, new_f_function_representation)
        )
        self.add(new_f_function_representation)
        self.remove(f_function_representation)
        self.wait(0.5)

        """ dot_1 = Dot(point=axes.c2p(1, 1), color=YELLOW)
        dot_2 = Dot(point=axes.c2p(2, 0), color=YELLOW)
        dot_3 = Dot(point=axes.c2p(3, 0), color=YELLOW)

        label_1 = Tex(r"(1, 1)").scale(0.7).next_to(dot_1, UP)
        label_2 = Tex(r"(2, 0)").scale(0.7).next_to(dot_2, UP+LEFT)
        label_3 = Tex(r"(3, 0)").scale(0.7).next_to(dot_3, UP+LEFT)

        self.play(
            DrawBorderThenFill(dot_1),
            DrawBorderThenFill(dot_2),
            DrawBorderThenFill(dot_3),
            Write(label_1),
            Write(label_2),
            Write(label_3),
        )
        self.add(dot_1, dot_2, dot_3, label_1, label_2, label_3)

        def f_x_values(x):
            return (x-2)*(x-3)/2
        
        curve_points = [axes.c2p(i, f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        f_curve = curves[0]
        self.play(Create(f_curve))
        self.add(f_curve)

        self.play(
            FadeOut(dot_1),
            FadeOut(dot_2),
            FadeOut(dot_3),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(label_3),
        )
        self.remove(dot_1, dot_2, dot_3, label_1, label_2, label_3)

        def new_f_x_values(x):
            return (x-2)*(x-3)*2

        curve_points = [axes.c2p(i, new_f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        new_f_curve = curves[0]
        self.play(Transform(f_curve, new_f_curve))
        self.add(new_f_curve)
        self.remove(f_curve)


        dot_1 = Dot(point=axes.c2p(1, 4), color=YELLOW)
        dot_2 = Dot(point=axes.c2p(2, 0), color=YELLOW)
        dot_3 = Dot(point=axes.c2p(3, 0), color=YELLOW)

        label_1 = Tex(r"(1, 4)").scale(0.7).next_to(dot_1, UP)
        label_2 = Tex(r"(2, 0)").scale(0.7).next_to(dot_2, UP+LEFT)
        label_3 = Tex(r"(3, 0)").scale(0.7).next_to(dot_3, UP+LEFT)

        self.play(
            DrawBorderThenFill(dot_1),
            DrawBorderThenFill(dot_2),
            DrawBorderThenFill(dot_3),
            Write(label_1),
            Write(label_2),
            Write(label_3),
        )
        self.add(dot_1, dot_2, dot_3, label_1, label_2, label_3)


        self.play(
            FadeOut(dot_1),
            FadeOut(dot_2),
            FadeOut(dot_3),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(label_3),
            FadeOut(new_f_curve)
        )
        self.remove(dot_1, dot_2, dot_3, label_1, label_2, label_3, new_f_curve) """

        
        
        
        
        
        
        
        
        
        self.play(            
            f_curve_light.animate.set_stroke(opacity=0.2),
            f_dot_1.animate.set_opacity(0.2),
            f_dot_2.animate.set_opacity(0.2),
            f_dot_3.animate.set_opacity(0.2),
            f_label_1.animate.set_opacity(0),
            f_label_2.animate.set_opacity(0),
            f_label_3.animate.set_opacity(0),

            g_function_representation.animate.set_opacity(1),
            g_curve_light.animate.set_stroke(opacity=1),
            g_dot_1.animate.set_opacity(1),
            g_dot_2.animate.set_opacity(1),
            g_dot_3.animate.set_opacity(1),
            g_label_1.animate.set_opacity(1),
            g_label_2.animate.set_opacity(1),
            g_label_3.animate.set_opacity(1),
        )
        self.wait(0.5)

        new_g_coordinates = [(1, 0), (2, 1), (3, 0)]

        # Create the coordinate pairs as a list of Tex objects
        new_g_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in new_g_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        new_g_left_brace = Brace(new_g_coordinate_pairs, direction=LEFT)

        new_g_coefficient = MathTex(r"9 \times").scale(1).next_to(new_g_left_brace, LEFT)
        new_g_equal_to = MathTex(r"=").scale(1.5).next_to(new_g_coefficient, LEFT)
        new_g_x = MathTex(r"g(x)").scale(1.5).shift(3*UP).set_color(GREEN)
        new_g_x.next_to(new_g_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        new_g_function_representation = VGroup(
            new_g_x,
            new_g_coefficient,
            new_g_equal_to,
            new_g_left_brace,
            new_g_coordinate_pairs
        )
        new_g_function_representation.scale(0.6).shift(3*UP).shift(3.25*RIGHT)
    

        self.play(
            TransformMatchingShapes(g_function_representation, new_g_function_representation),
        )
        self.add(new_g_function_representation)
        self.remove(g_function_representation)
        self.wait(0.5)

        """ dot_1 = Dot(point=axes.c2p(1, 0), color=GREEN)
        dot_2 = Dot(point=axes.c2p(2, 1), color=GREEN)
        dot_3 = Dot(point=axes.c2p(3, 0), color=GREEN)

        label_1 = Tex(r"(1, 0)").scale(0.7).next_to(dot_1, UP)
        label_2 = Tex(r"(2, 1)").scale(0.7).next_to(dot_2, UP+LEFT)
        label_3 = Tex(r"(3, 0)").scale(0.7).next_to(dot_3, UP+LEFT)

        self.play(
            DrawBorderThenFill(dot_1),
            DrawBorderThenFill(dot_2),
            DrawBorderThenFill(dot_3),
            Write(label_1),
            Write(label_2),
            Write(label_3),
        )
        self.add(dot_1, dot_2, dot_3, label_1, label_2, label_3)

        def g_x_values(x):
            return (x-1)*(x-3)*(-1)
        
        curve_points = [axes.c2p(i, g_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        g_curve = curves[0]
        self.play(Create(g_curve))
        self.add(g_curve)

        self.play(
            FadeOut(dot_1),
            FadeOut(dot_2),
            FadeOut(dot_3),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(label_3),
        )
        self.remove(dot_1, dot_2, dot_3, label_1, label_2, label_3)

        def new_g_x_values(x):
            return (x-1)*(x-3)*(-9)

        curve_points = [axes.c2p(i, new_g_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        new_g_curve = curves[0]
        self.play(Transform(g_curve, new_g_curve))
        self.add(new_g_curve)
        self.remove(g_curve)


        dot_1 = Dot(point=axes.c2p(1, 0), color=GREEN)
        dot_2 = Dot(point=axes.c2p(2, 9), color=GREEN)
        dot_3 = Dot(point=axes.c2p(3, 0), color=GREEN)

        label_1 = Tex(r"(1, 0)").scale(0.7).next_to(dot_1, UP+LEFT)
        label_2 = Tex(r"(2, 9)").scale(0.7).next_to(dot_2, UP)
        label_3 = Tex(r"(3, 0)").scale(0.7).next_to(dot_3, UP+RIGHT)

        self.play(
            DrawBorderThenFill(dot_1),
            DrawBorderThenFill(dot_2),
            DrawBorderThenFill(dot_3),
            Write(label_1),
            Write(label_2),
            Write(label_3),
        )
        self.add(dot_1, dot_2, dot_3, label_1, label_2, label_3)


        self.play(
            FadeOut(dot_1),
            FadeOut(dot_2),
            FadeOut(dot_3),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(label_3),
            FadeOut(new_g_curve)
        )
        self.remove(dot_1, dot_2, dot_3, label_1, label_2, label_3, new_g_curve) """










        self.play(            
            g_curve_light.animate.set_stroke(opacity=0.2),
            g_dot_1.animate.set_opacity(0.2),
            g_dot_2.animate.set_opacity(0.2),
            g_dot_3.animate.set_opacity(0.2),
            g_label_1.animate.set_opacity(0),
            g_label_2.animate.set_opacity(0),
            g_label_3.animate.set_opacity(0),

            h_function_representation.animate.set_opacity(1),
            h_curve_light.animate.set_stroke(opacity=1),
            h_dot_1.animate.set_opacity(1),
            h_dot_2.animate.set_opacity(1),
            h_dot_3.animate.set_opacity(1),
            h_label_1.animate.set_opacity(1),
            h_label_2.animate.set_opacity(1),
            h_label_3.animate.set_opacity(1),
        )
        self.wait(0.5)

        new_h_coordinates = [(1, 0), (2, 0), (3, 1)]

        # Create the coordinate pairs as a list of Tex objects
        new_h_coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in new_h_coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        new_h_left_brace = Brace(new_h_coordinate_pairs, direction=LEFT)

        new_h_coefficient = MathTex(r"16 \times").scale(1).next_to(new_h_left_brace, LEFT)
        new_h_equal_to = MathTex(r"=").scale(1.5).next_to(new_h_coefficient, LEFT)
        new_h_x = MathTex(r"h(x)").scale(1.5).shift(3*UP).set_color(BLUE)
        new_h_x.next_to(new_h_equal_to, LEFT)
        
        # Group the curly brace and coordinate pairs
        new_h_function_representation = VGroup(
            new_h_x,
            new_h_coefficient,
            new_h_equal_to,
            new_h_left_brace,
            new_h_coordinate_pairs
        )
        new_h_function_representation.scale(0.6).shift(3*UP).shift(7*RIGHT)
    

        self.play(
            TransformMatchingShapes(h_function_representation, new_h_function_representation),
        )
        self.add(new_h_function_representation)
        self.remove(h_function_representation)
        self.wait(0.5)


        self.play(
            FadeOut(s_curve_light),
            FadeOut(f_curve_light),
            FadeOut(g_curve_light),
            FadeOut(h_curve_light),

            FadeOut(s_dot_1),
            FadeOut(s_dot_2),
            FadeOut(s_dot_3),
            FadeOut(s_label_1),
            FadeOut(s_label_2),
            FadeOut(s_label_3),

            FadeOut(f_dot_1),
            FadeOut(f_dot_2),
            FadeOut(f_dot_3),
            FadeOut(f_label_1),
            FadeOut(f_label_2),
            FadeOut(f_label_3),

            FadeOut(g_dot_1),
            FadeOut(g_dot_2),
            FadeOut(g_dot_3),
            FadeOut(g_label_1),
            FadeOut(g_label_2),
            FadeOut(g_label_3),

            FadeOut(h_dot_1),
            FadeOut(h_dot_2),
            FadeOut(h_dot_3),
            FadeOut(h_label_1),
            FadeOut(h_label_2),
            FadeOut(h_label_3),
        )
        self.remove(
            s_curve_light,
            f_curve_light,
            g_curve_light,
            h_curve_light,
            s_dot_1,
            s_dot_2,
            s_dot_3,
            s_label_1,
            s_label_2,
            s_label_3,
            f_dot_1,
            f_dot_2,
            f_dot_3,
            f_label_1,
            f_label_2,
            f_label_3,
            g_dot_1,
            g_dot_2,
            g_dot_3,
            g_label_1,
            g_label_2,
            g_label_3,
            h_dot_1,
            h_dot_2,
            h_dot_3,
            h_label_1,
            h_label_2,
            h_label_3,
        )
        self.wait(0.5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






 
        s_x = MathTex(r"s(x) = ").scale(1).shift(3*UP).shift(6*LEFT).set_color(RED)
        self.play(Transform(s_function_representation, s_x))
        self.add(s_x)
        self.remove(s_function_representation)
        self.wait(0.5)





        f_x_expression = MathTex(r"4 \times (x-2)(x-3)").set_color(YELLOW).scale(1).next_to(s_x, RIGHT)

        def f_x_values(x):
            return (x-2)*(x-3)*4

        f_dot_1 = Dot(point=axes.c2p(1, f_x_values(1)), color=YELLOW)
        f_dot_2 = Dot(point=axes.c2p(2, f_x_values(2)), color=YELLOW)
        f_dot_3 = Dot(point=axes.c2p(3, f_x_values(3)), color=YELLOW)

        f_label_1 = Tex(r"(1, 8)").scale(0.7).next_to(f_dot_1, UP+RIGHT)
        f_label_2 = Tex(r"(2, 0)").scale(0.7).next_to(f_dot_2, UP)
        f_label_3 = Tex(r"(3, 0)").scale(0.7).next_to(f_dot_3, UP)
        
        curve_points = [axes.c2p(i, f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        f_curve = curves[0]


        self.play(
            TransformMatchingShapes(new_f_function_representation, f_x_expression),
            Create(f_curve),
            DrawBorderThenFill(f_dot_1),
            DrawBorderThenFill(f_dot_2),
            DrawBorderThenFill(f_dot_3),
            Write(f_label_1),
            Write(f_label_2),
            Write(f_label_3),
        )
        self.add(
            f_x_expression, 
            f_dot_1, 
            f_dot_2, 
            f_dot_3, 
            f_label_1, 
            f_label_2, 
            f_label_3
        )
        self.remove(new_f_function_representation)
        self.wait(0.5)

        self.play(
            Indicate(f_dot_2, color=YELLOW, scale_factor=1.2),
            Indicate(f_label_2, color=YELLOW),
            Indicate(f_dot_3, color=YELLOW, scale_factor=1.2),
            Indicate(f_label_3, color=YELLOW),
        )
        self.wait(0.5)

        self.play(
            Indicate(f_dot_1, color=YELLOW, scale_factor=1.2),
            Indicate(f_label_1, color=YELLOW),
        )
        self.wait(0.5)

        self.play(
            FadeOut(f_dot_1),
            FadeOut(f_label_1),
        )
        self.remove(f_dot_1, f_label_1)
        self.wait(0.5)


        def new_f_x_values(x):
            return (x-2)*(x-3)*2

        curve_points = [axes.c2p(i, new_f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        new_f_curve = curves[0]

        f_x_intermediate_evaluation = MathTex(r"\frac{4(x-2)(x-3)}{(1-2)(1-3)}").set_color(YELLOW).scale(1).next_to(s_x, RIGHT)
        
        f_dot_1 = Dot(point=axes.c2p(1, new_f_x_values(1)), color=YELLOW)
        f_label_1 = Tex(r"(1, 4)").scale(0.7).next_to(f_dot_1, UP)

        self.play(
            Transform(f_curve, new_f_curve),
            TransformMatchingShapes(f_x_expression, f_x_intermediate_evaluation),
            FadeIn(f_dot_1),
            Write(f_label_1),
        )
        self.add(new_f_curve, f_x_intermediate_evaluation, f_dot_1, f_label_1)
        self.remove(f_curve, f_x_expression)
        self.wait(0.5)

        self.play(
            FadeOut(new_f_curve),
            FadeOut(f_dot_1),
            FadeOut(f_label_1),
            FadeOut(f_dot_2),
            FadeOut(f_label_2),
            FadeOut(f_dot_3),
            FadeOut(f_label_3)
        )
        self.remove(
            new_f_curve,
            f_dot_1,
            f_label_1,
            f_dot_2,
            f_label_2,
            f_dot_3,
            f_label_3
        )
        self.wait(0.5)
        
        










        plus_sign_1 = MathTex(r"+").scale(1).next_to(f_x_intermediate_evaluation, RIGHT)
        g_x_expression = MathTex(r"9 \times (x-1)(x-3)").set_color(GREEN).scale(1).next_to(plus_sign_1, RIGHT)

        def g_x_values(x):
            return (x-1)*(x-3)*9

        g_dot_1 = Dot(point=axes.c2p(1, g_x_values(1)), color=GREEN)
        g_dot_2 = Dot(point=axes.c2p(2, g_x_values(2)), color=GREEN)
        g_dot_3 = Dot(point=axes.c2p(3, g_x_values(3)), color=GREEN)

        g_label_1 = Tex(r"(1, 0)").scale(0.7).next_to(g_dot_1, UP+LEFT)
        g_label_2 = Tex(r"(2, -9)").scale(0.7).next_to(g_dot_2, UP)
        g_label_3 = Tex(r"(3, 0)").scale(0.7).next_to(g_dot_3, UP+RIGHT)
        
        curve_points = [axes.c2p(i, g_x_values(i)) for i in np.arange(0.2, 4, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        g_curve = curves[0]


        self.play(
            FadeIn(plus_sign_1),
            TransformMatchingShapes(new_g_function_representation, g_x_expression),
            Create(g_curve),
            DrawBorderThenFill(g_dot_1),
            DrawBorderThenFill(g_dot_2),
            DrawBorderThenFill(g_dot_3),
            Write(g_label_1),
            Write(g_label_2),
            Write(g_label_3),
        )
        self.add(
            g_x_expression, 
            g_dot_1, 
            g_dot_2, 
            g_dot_3, 
            g_label_1, 
            g_label_2, 
            g_label_3
        )
        self.remove(new_g_function_representation)
        self.wait(0.5)

        self.play(
            Indicate(g_dot_1, color=GREEN, scale_factor=1.2),
            Indicate(g_label_1, color=GREEN),
            Indicate(g_dot_3, color=GREEN, scale_factor=1.2),
            Indicate(g_label_3, color=GREEN),
        )
        self.wait(0.5)

        self.play(
            Indicate(g_dot_2, color=GREEN, scale_factor=1.2),
            Indicate(g_label_2, color=GREEN),
        )
        self.wait(0.5)

        self.play(
            FadeOut(g_dot_2),
            FadeOut(g_label_2),
        )
        self.remove(g_dot_2, g_label_2)
        self.wait(0.5)


        def new_g_x_values(x):
            return (x-1)*(x-3)*9*(-1)

        curve_points = [axes.c2p(i, new_g_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        new_g_curve = curves[0]

        g_x_intermediate_evaluation = MathTex(r"\frac{9(x-1)(x-3)}{(2-1)(2-3)}").set_color(GREEN).scale(1).next_to(plus_sign_1, RIGHT)
        
        g_dot_2 = Dot(point=axes.c2p(2, new_g_x_values(2)), color=GREEN)
        g_label_2 = Tex(r"(2, 9)").scale(0.7).next_to(g_dot_2, UP)

        self.play(
            Transform(g_curve, new_g_curve),
            TransformMatchingShapes(g_x_expression, g_x_intermediate_evaluation),
            FadeIn(g_dot_2),
            Write(g_label_2),
        )
        self.add(new_g_curve, g_x_intermediate_evaluation, g_dot_2, g_label_2)
        self.remove(g_curve, g_x_expression)
        self.wait(0.5)

        self.play(
            FadeOut(new_g_curve),
            FadeOut(g_dot_1),
            FadeOut(g_label_1),
            FadeOut(g_dot_2),
            FadeOut(g_label_2),
            FadeOut(g_dot_3),
            FadeOut(g_label_3)
        )
        self.remove(
            new_g_curve,
            g_dot_1,
            g_label_1,
            g_dot_2,
            g_label_2,
            g_dot_3,
            g_label_3
        )
        self.wait(0.5)
















        plus_sign_2 = MathTex(r"+").scale(1).next_to(g_x_intermediate_evaluation, RIGHT)
        h_x_expression = MathTex(r"16 \times (x-1)(x-2)").set_color(BLUE).scale(1).next_to(plus_sign_2, RIGHT)

        def h_x_values(x):
            return (x-1)*(x-2)*16

        h_dot_1 = Dot(point=axes.c2p(1, h_x_values(1)), color=BLUE)
        h_dot_2 = Dot(point=axes.c2p(2, h_x_values(2)), color=BLUE)
        h_dot_3 = Dot(point=axes.c2p(3, h_x_values(3)), color=BLUE)

        h_label_1 = Tex(r"(1, 0)").scale(0.7).next_to(h_dot_1, UP+RIGHT)
        h_label_2 = Tex(r"(2, 0)").scale(0.7).next_to(h_dot_2, UP+RIGHT)
        h_label_3 = Tex(r"(3, 16)").scale(0.7).next_to(h_dot_3, UP+LEFT)
        
        curve_points = [axes.c2p(i, h_x_values(i)) for i in np.arange(0.5, 2.5, 0.1)]

        curves = self.draw_curve(curve_points, color=BLUE)
        h_curve = curves[0]


        self.play(
            FadeIn(plus_sign_2),
            TransformMatchingShapes(new_h_function_representation, h_x_expression),
            Create(h_curve),
            DrawBorderThenFill(h_dot_1),
            DrawBorderThenFill(h_dot_2),
            #DrawBorderThenFill(h_dot_3),
            Write(h_label_1),
            Write(h_label_2),
            #Write(h_label_3),
        )
        self.add(
            h_x_expression, 
            h_dot_1, 
            h_dot_2, 
            #h_dot_3, 
            h_label_1, 
            h_label_2, 
            #h_label_3
        )
        self.remove(new_h_function_representation)
        self.wait(0.5)

        self.play(
            Indicate(h_dot_1, color=BLUE, scale_factor=1.2),
            Indicate(h_label_1, color=BLUE),
            Indicate(h_dot_2, color=BLUE, scale_factor=1.2),
            Indicate(h_label_2, color=BLUE),
        )
        self.wait(0.5)

        #self.play(
        #    Indicate(h_dot_3, color=BLUE, scale_factor=1.2),
        #    Indicate(h_label_3, color=BLUE),
        #)

        #self.play(
        #    FadeOut(h_dot_3),
        #    FadeOut(h_label_3),
        #)
        #self.remove(h_dot_3, h_label_3)


        def new_h_x_values(x):
            return (x-1)*(x-2)*16/2

        curve_points = [axes.c2p(i, new_h_x_values(i)) for i in np.arange(0, 3.2, 0.1)]

        curves = self.draw_curve(curve_points, color=BLUE)
        new_h_curve = curves[0]

        h_x_intermediate_evaluation = MathTex(r"\frac{16(x-1)(x-2)}{(3-1)(3-2)}").set_color(BLUE).scale(1).next_to(plus_sign_2, RIGHT)
        
        h_dot_3 = Dot(point=axes.c2p(3, new_h_x_values(3)), color=BLUE)
        h_label_3 = Tex(r"(3, 16)").scale(0.7).next_to(h_dot_3, RIGHT)

        self.play(
            Transform(h_curve, new_h_curve),
            TransformMatchingShapes(h_x_expression, h_x_intermediate_evaluation),
            FadeIn(h_dot_3),
            Write(h_label_3),
        )
        self.add(new_h_curve, h_x_intermediate_evaluation, h_dot_3, h_label_3)
        self.remove(h_curve, h_x_expression)
        self.wait(0.5)

        self.play(
            FadeOut(new_h_curve),
            FadeOut(h_dot_1),
            FadeOut(h_label_1),
            FadeOut(h_dot_2),
            FadeOut(h_label_2),
            FadeOut(h_dot_3),
            FadeOut(h_label_3)
        )
        self.remove(
            new_h_curve,
            h_dot_1,
            h_label_1,
            h_dot_2,
            h_label_2,
            h_dot_3,
            h_label_3
        )
        self.wait(0.5)




        





        s_dot_1 = Dot(point=axes.c2p(1, 4), color=RED)
        s_dot_2 = Dot(point=axes.c2p(2, 9), color=RED)
        s_dot_3 = Dot(point=axes.c2p(3, 16), color=RED)

        s_label_1 = Tex(r"(1, 4)").scale(0.7).next_to(s_dot_1, UP)
        s_label_2 = Tex(r"(2, 9)").scale(0.7).next_to(s_dot_2, (UP+LEFT)*0.5)
        s_label_3 = Tex(r"(3, 16)").scale(0.7).next_to(s_dot_3, (UP+LEFT)*0.5)


        def new_f_x_values(x):
            return (x-2)*(x-3)*2

        curve_points = [axes.c2p(i, new_f_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=YELLOW)
        f_curve = curves[0]


        self.play(
            DrawBorderThenFill(s_dot_1),
            DrawBorderThenFill(s_dot_2),
            DrawBorderThenFill(s_dot_3),
            Write(s_label_1),
            Write(s_label_2),
            Write(s_label_3),
            Create(f_curve),
            plus_sign_1.animate.set_opacity(0.2),
            plus_sign_2.animate.set_opacity(0.2),
            g_x_intermediate_evaluation.animate.set_opacity(0.2),
            h_x_intermediate_evaluation.animate.set_opacity(0.2),
        )
        self.add(s_dot_1, s_dot_2, s_dot_3, s_label_1, s_label_2, s_label_3, f_curve)
        self.wait(0.5)

        
        
        
        def new_f_g_x_values(x):
            return (x-2)*(x-3)*2 + (x-1)*(x-3)*9*(-1)

        curve_points = [axes.c2p(i, new_f_g_x_values(i)) for i in np.arange(0, 4.6, 0.1)]

        curves = self.draw_curve(curve_points, color=GREEN)
        f_g_curve = curves[0]


        self.play(
            plus_sign_1.animate.set_opacity(1),
            g_x_intermediate_evaluation.animate.set_opacity(1),
            Transform(f_curve, f_g_curve),
            run_time=3
        )
        self.add(f_g_curve)
        self.remove(f_curve)
        self.wait(0.5)






        def new_f_g_h_x_values(x):
            return (x-2)*(x-3)*2 + (x-1)*(x-3)*9*(-1) + (x-1)*(x-2)*16/2

        curve_points = [axes.c2p(i, new_f_g_h_x_values(i)) for i in np.arange(0, 4, 0.1)]

        curves = self.draw_curve(curve_points, color=RED)
        f_g_h_curve = curves[0]


        self.play(
            plus_sign_2.animate.set_opacity(1),
            h_x_intermediate_evaluation.animate.set_opacity(1),
            Transform(f_g_curve, f_g_h_curve),
            run_time=3
        )
        self.add(f_g_h_curve)
        self.remove(f_g_curve)
        self.wait(0.5)




        i_1_text = MathTex(r"x_{i} = 1").scale(1).next_to(h_function_representation, DOWN).shift(DOWN)
        j_2_text = MathTex(r"x_{j} = 2").scale(1).next_to(i_1_text, DOWN)
        k_3_text = MathTex(r"x_{k} = 3").scale(1).next_to(j_2_text, DOWN)
        a_4_text = MathTex(r"y_{i} = 4").scale(1).next_to(k_3_text, DOWN)
        b_9_text = MathTex(r"y_{j} = 9").scale(1).next_to(a_4_text, DOWN)
        c_16_text = MathTex(r"y_{k} = 16").scale(1).next_to(b_9_text, DOWN)

        new_notation = VGroup(
            i_1_text,
            j_2_text,
            k_3_text,
            a_4_text,
            b_9_text,
            c_16_text
        )

        self.play(
            Write(new_notation)
        )
        self.add(new_notation)
        self.wait(0.5)

        new_s_label_1 = MathTex(r"(x_{i}, y_{i})").scale(0.7).next_to(s_dot_1, UP)
        new_s_label_2 = MathTex(r"(x_{j}, y_{j})").scale(0.7).next_to(s_dot_2, UP+LEFT)
        new_s_label_3 = MathTex(r"(x_{k}, y_{k})").scale(0.7).next_to(s_dot_3, UP+LEFT)
        new_f_x_intermediate_evaluation = MathTex(r"\frac{y_{i}(x-x_{j})(x-x_{k})}{(x_{i}-x_{j})(x_{i}-x_{k})}").set_color(YELLOW).scale(0.8).next_to(s_x, RIGHT) 
        new_g_x_intermediate_evaluation = MathTex(r"\frac{y_{j}(x-x_{i})(x-x_{k})}{(x_{j}-x_{i})(x_{j}-x_{k})}").set_color(GREEN).scale(0.8).next_to(plus_sign_1, RIGHT) 
        new_h_x_intermediate_evaluation = MathTex(r"\frac{y_{k}(x-x_{i})(x-x_{j})}{(x_{k}-x_{i})(x_{k}-x_{j})}").set_color(BLUE).scale(0.8).next_to(plus_sign_2, RIGHT) 



        old_group = VGroup(
            s_label_1,
            s_label_2,
            s_label_3,
            f_x_intermediate_evaluation,
            g_x_intermediate_evaluation,
            h_x_intermediate_evaluation
        )

        new_group = VGroup(
            new_s_label_1,
            new_s_label_2,
            new_s_label_3,
            new_f_x_intermediate_evaluation,
            new_g_x_intermediate_evaluation,
            new_h_x_intermediate_evaluation
        )

        self.play(
            FadeOut(old_group),
            TransformMatchingShapes(new_notation, new_group),
        )
        self.remove(old_group, new_notation)
        self.add(new_group)


        self.wait(2)