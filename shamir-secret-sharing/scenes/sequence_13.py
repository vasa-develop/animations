from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence13(Scene):
    
    def construct(self):
        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))
        self.add(recap_text)
        self.play(FadeOut(recap_text))
        self.remove(recap_text)

        number_password_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2)
        
        self.play(
            DrawBorderThenFill(number_password_text)
        )

        self.add(number_password_text)

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


        problem_1_text = MathTex(r"\textbf{Problem 1: Information Leakage}", color=RED).scale(1.2).shift(3*UP)
        self.play(Write(problem_1_text))
        self.add(problem_1_text)


        self.play(
            FadeOut(friend_left),
            FadeOut(friend_right),
            FadeOut(friend_left_password_text),
            FadeOut(friend_right_password_text),
        )

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


        problem_2_text = MathTex(r"\textbf{Problem 2: Threshold Secret Sharing}", color=RED).scale(1.2).next_to(problem_1_text, direction=DOWN).shift(3*DOWN)
        self.play(Write(problem_2_text))
        self.add(problem_2_text)


        self.play(
            DrawBorderThenFill(friend_1_emoji),
            DrawBorderThenFill(friend_2_emoji),
            DrawBorderThenFill(friend_3_emoji),
            DrawBorderThenFill(friend_1_text),
            DrawBorderThenFill(friend_2_text),
            DrawBorderThenFill(friend_3_text),
            DrawBorderThenFill(equal_to_1),
            DrawBorderThenFill(equal_to_2),
            DrawBorderThenFill(equal_to_3),
            DrawBorderThenFill(perfect_secrecy_text)
        )

        share_1 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).shift(2*DOWN + 3*LEFT)
        share_2 = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).next_to(share_1, direction=RIGHT, buff=0.5)
        share_3 = BootstrapSVGMobject('person-fill', color=GRAY).set_color(GRAY).scale(0.4).next_to(share_2, direction=RIGHT, buff=0.5)
        arrow = Arrow(color= WHITE).next_to(share_3, direction=RIGHT, buff=0.5)
        unlock = BootstrapSVGMobject('unlock-fill', color=GREEN).scale(0.4).next_to(arrow, direction=RIGHT, buff=0.5)

        self.play(
            DrawBorderThenFill(share_1),
            DrawBorderThenFill(share_2),
            DrawBorderThenFill(share_3),
            DrawBorderThenFill(arrow),
            DrawBorderThenFill(unlock)
        )

        """
        TODO: Add animation for

        As we learned, if you have less than the threshold number of secret
        shares, you learn no information about the secret, hence this gives
        us the property of perfect secrecy. You can only restore the secret,
        if you have at least the threshold number of secrets.
        
        """


        self.wait(2)