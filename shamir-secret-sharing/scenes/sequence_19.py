from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence19(Scene):
    
    def construct(self):
        """
        We covered a lot in this video, so let’s do a quick recap and close with a few other applications that use the same concepts that we covered in this video.

We started with a naive way to share a secret between you and your friend where we solved 2 main problems:

1. We added randomness to our secret using modular arithmetic to achieve perfect secrecy where we don’t leak any information about the secret from just a single secret share.
2. We used graphs to represent our secret and randomness as points to create a secret sharing scheme which could handle scenarios where we can recover our secret with a fraction of the total distributed shares, which maintaining perfect secrecy.

Next, we looked into Lagrange interpolation what showed us a method to recover a secret curve given we have threshold number of points, or shares available.

Once our secret sharing scheme worked in theory, we tried to create a practical implementation for our scheme where we encountered some limitations regarding precision of fractional values due to the way computers store and operate on numbers.

Next, when we tried to update our secret sharing scheme such that it does not involve any fractional values. This time we lost the power of perfect secrecy, again due to fractional values.

Finally, we devised a secret sharing scheme using modular arithmetic where we can made sure that all operations such as addition, subtraction, multiplication, and division always lead to an integer, hence solving the precision and perfect secrecy issues altogether.
        """

        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))
        self.add(recap_text)
        self.wait(0.5)
        
        self.play(FadeOut(recap_text))
        self.remove(recap_text)

        number_password_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2)
        
        self.play(
            DrawBorderThenFill(number_password_text)
        )
        self.add(number_password_text)
        self.wait(0.5)

        # move number_password_text up and add 2 friends
        friend_left = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.5).shift(2*(DOWN+LEFT))
        friend_right = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.5).shift(2*(DOWN+RIGHT))

        self.play(
            number_password_text.animate.shift(2*UP),
            DrawBorderThenFill(friend_left),
            DrawBorderThenFill(friend_right)
        )

        self.add(friend_left)
        self.add(friend_right)
        self.wait(0.5)

        number_password_text_invisible = MathTex(r"\textbf{12345678}", color=GREEN).scale(2).shift(2*UP)
        friend_left_password_text = MathTex(r"\textbf{1234}", color=WHITE).scale(1.2).next_to(friend_left, direction=DOWN).shift(2*(UP + LEFT))
        friend_right_password_text = MathTex(r"\textbf{5678}", color=WHITE).scale(1.2).next_to(friend_right, direction=DOWN).shift(2*(UP + RIGHT))

        self.play(
            friend_left.animate.shift(2*(UP + LEFT)),
            friend_right.animate.shift(2*(UP + RIGHT)),
            Transform(number_password_text, friend_left_password_text),
            Transform(number_password_text_invisible, friend_right_password_text)
        )

        self.add(friend_left_password_text)
        self.add(friend_right_password_text)
        self.remove(number_password_text)
        self.remove(number_password_text_invisible)
        self.wait(0.5)


        problem_1_text = MathTex(r"\textbf{Problem 1: Information Leakage}", color=RED).scale(1.2).shift(3*UP)
        self.play(Write(problem_1_text))
        self.add(problem_1_text)
        self.wait(0.5)

        friend_group = VGroup(friend_left, friend_right, friend_left_password_text, friend_right_password_text)
        
        self.wait(0.5)

        friend_1_emoji = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).shift(1.5*UP + 5*LEFT)
        friend_1_text = MathTex(r"\textbf{share = 1234}", color=WHITE).scale(0.7).next_to(friend_1_emoji, direction=DOWN)
        friend_1 = VGroup(friend_1_emoji, friend_1_text)
        equal_to_1 = MathTex(r"\textbf{=}", color=WHITE).scale(1.3).next_to(friend_1, RIGHT)

        friend_2_emoji = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4)
        friend_2_text = MathTex(r"\textbf{share = 5678}", color=WHITE).scale(0.7).next_to(friend_2_emoji, direction=DOWN)
        friend_2 = VGroup(friend_2_emoji, friend_2_text).next_to(equal_to_1, direction=RIGHT)
        equal_to_2 = MathTex(r"\textbf{=}", color=WHITE).scale(1.3).next_to(friend_2, RIGHT)

        friend_3_emoji = BootstrapSVGMobject('person-fill', color=GRAY).scale(0.4).set_color(GRAY)
        friend_3_text = MathTex(r"\textbf{No secret share}", color=WHITE).scale(0.7).next_to(friend_3_emoji, direction=DOWN)
        friend_3 = VGroup(friend_3_emoji, friend_3_text).next_to(equal_to_2, direction=RIGHT)
        equal_to_3 = MathTex(r"\textbf{=}", color=WHITE).scale(1.3).next_to(friend_3, RIGHT)

        perfect_secrecy_text = MathTex(r"\textbf{Perfect Secrecy}", color=GREEN).scale(0.7).next_to(equal_to_3, direction=RIGHT) 

        problem_1_group = VGroup(
            friend_1_emoji,
            friend_1_text,
            friend_2_emoji,
            friend_2_text,
            friend_3_emoji,
            friend_3_text,
            equal_to_1,
            equal_to_2,
            equal_to_3,
            perfect_secrecy_text
        )

        self.play(
            TransformMatchingShapes(friend_group, problem_1_group)
        )
        self.wait(0.5)

        problem_2_text = MathTex(r"\textbf{Problem 2: Threshold Secret Sharing}", color=RED).scale(1.2).next_to(problem_1_text, direction=DOWN).shift(3*DOWN)
        self.play(Write(problem_2_text))
        self.add(problem_2_text)
        self.wait(0.5)

        share_1 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).shift(2*DOWN + 3*LEFT)
        share_2 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).next_to(share_1, direction=RIGHT, buff=0.5)
        share_3 = BootstrapSVGMobject('person-fill', color=RED).set_color(RED).scale(0.4).next_to(share_2, direction=RIGHT, buff=0.5)
        arrow = Arrow(color= WHITE).next_to(share_3, direction=RIGHT, buff=0.5)
        unlock = BootstrapSVGMobject('unlock-fill', color=GREEN).scale(0.4).next_to(arrow, direction=RIGHT, buff=0.5)

        self.play(
            DrawBorderThenFill(share_1),
            DrawBorderThenFill(share_2),
            DrawBorderThenFill(share_3),
            DrawBorderThenFill(arrow),
            DrawBorderThenFill(unlock)
        )
        self.wait(0.5)

        self.wait(2)