from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence7(Scene):
    
    def construct(self):
        """
        NOTE: We can skip this part.
        TODO: Add animation for 
        
        Feel free to take a moment and think about how just by changing the
        way we add 2 different numbers, we have made it a lot harder to brute force
        the secret. While it is not clear at first, this small change in using
        modular arithmetic increases the security of our secret-sharing system by
        a lot.
        """
        
        
        
        
        
        
        
        
        """
        TODO: Add animation for 

        To recap what we have learned until now, we started by sharing an 8-digit
        secret between you and your friend and we mentioned that this naive
        approach has 2 problems. The first problem was to find a way to share
        a secret such that a person with a secret share has the same probability
        of brute-forcing the secret as a person without a secret share.

        As we saw, adding randomness to our secret and using modular arithmetic
        helped us to solve this problem.

        Use IMovie to record the following:
        https://chat.openai.com/c/4c703edb-71c8-4b7b-aeba-6cd68214a902
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

        problem = MathTex(r"\textbf{Problem 1: Information Leakage}", color=RED).scale(1.2).shift(3*UP)
        self.play(Write(problem))
        self.add(problem)

        friends_group = VGroup(friend_left, friend_right, friend_left_password_text, friend_right_password_text, problem)

        
        problem_text_1 = MathTex(r"\textbf{Achieving perfect secrecy by adding}", color=RED).scale(1.2).shift(3*UP)
        problem_text_2 = MathTex(r"\textbf{randomness to our secret}", color=RED).scale(1.2).next_to(problem_text_1, direction=DOWN)

        friend_1_emoji = BootstrapSVGMobject('person-fill', color=BLUE).scale(0.4).shift(5*LEFT)
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

        group = VGroup(problem_text_1, problem_text_2, friend_1, friend_2, friend_3, equal_to_1, equal_to_2, equal_to_3, perfect_secrecy_text)

        self.play(
            TransformMatchingShapes(friends_group, group)
        )
        self.wait(0.5)



