from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence1(Scene):
    def construct(self, *args) -> [MathTex]:

        eli5_text = None
        topic_text = None

        if (len(args) == 0):
            eli5_text = MathTex(r"\text{ELI5}", color=BLUE).scale(3).shift(2*UP)
            topic_text = MathTex(r"\text{Shamir Secret Sharing and Lagrange Interpolation}", color=WHITE).shift(1*DOWN)
        else:
            eli5_text = args[0]
            topic_text = args[1]
        

        self.camera.background_color = BLACK
        left_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(2*(DOWN+LEFT))
        right_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(2*(DOWN+RIGHT))

        self.play(
            Transform(eli5_text, left_friend),
            Transform(topic_text, right_friend)
        )

        self.add(left_friend)
        self.add(right_friend)
        self.remove(eli5_text)
        self.remove(topic_text)
        self.wait(1)

        NETFLIX_IMAGE = "./assets/netflix.jpeg"

        image = ImageMobject(NETFLIX_IMAGE).scale(0.5).shift(2*UP)
        self.play(FadeIn(image))

        self.add(image)
        self.wait(2)

        film = BootstrapSVGMobject('film', color=BLUE).shift(2*UP)
        self.play(FadeOut(image, run_time=1), FadeIn(film, run_time=1))

        self.add(film)
        self.remove(image)
        self.wait(2)

        password_text_visible = MathTex(r"\textbf{Password}", color=GREEN).scale(1.2).shift(2*UP)
        password_text_invisible = MathTex(r"\textbf{Password}", color=GREEN).scale(1.2).shift(2*UP)
        self.play(Transform(film, password_text_visible))

        self.add(password_text_visible)
        self.remove(film)
        self.wait(2)

        left_friend_password_text = MathTex(r"\textbf{Pass????}", color=YELLOW).scale(1.2).next_to(left_friend, direction=UP)
        right_friend_password_text = MathTex(r"\textbf{????word}", color=YELLOW).scale(1.2).next_to(right_friend, direction=UP)
        lock = BootstrapSVGMobject('lock-fill', color=RED).scale(0.5).shift(2*UP)
        self.play(
            Transform(password_text_visible, left_friend_password_text), 
            Transform(password_text_invisible, right_friend_password_text), 
            Transform(film, lock)
        )

        self.add(left_friend_password_text)
        self.add(right_friend_password_text)
        self.add(lock)
        self.remove(password_text_visible)
        self.remove(password_text_invisible)
        self.remove(film)
        self.wait(2)

        # draw a arraw between left_friend_password_text and lock (leave some space between them)
        # Calculate the starting and ending points of the arrow
        left_arrow_start_point = left_friend_password_text.get_center() + 0.5*UP
        left_arrow_end_point = lock.get_center() + 0.5*(DOWN + LEFT)
        right_arrow_start_point = right_friend_password_text.get_center() + 0.5*UP
        right_arrow_end_point = lock.get_center() + 0.5*(DOWN + RIGHT)

        # Create the arrows
        left_friend_arrow = Arrow(left_arrow_start_point, left_arrow_end_point, buff=0.1)
        right_friend_arrow = Arrow(right_arrow_start_point, right_arrow_end_point, buff=0.1)

        # Add the arrow to the scene
        self.play(
            Create(left_friend_arrow), 
            Create(right_friend_arrow),
            Wiggle(lock, amplitude=1, n_wiggles=6)
        )

        self.add(left_friend_arrow)
        self.add(right_friend_arrow)

        # change the color of the arrows to RED
        self.play(
            left_friend_arrow.animate.set_color(RED),
            right_friend_arrow.animate.set_color(RED)
        )
        
        self.play(
            FadeOut(left_friend_arrow),
            FadeOut(right_friend_arrow)
        )

        self.remove(left_friend_arrow)
        self.remove(right_friend_arrow)

        self.wait(2)

        merged_password_text_visible = MathTex(r"\textbf{Password}", color=GREEN).scale(1.2).shift(DOWN)
        merged_password_text_invisible = MathTex(r"\textbf{Password}", color=GREEN).scale(1.2).shift(DOWN)
        self.play(
            Transform(left_friend_password_text, merged_password_text_visible),
            Transform(right_friend_password_text, merged_password_text_invisible)
        )

        self.add(merged_password_text_visible)
        self.remove(left_friend_password_text)
        self.remove(right_friend_password_text)
        self.wait(2)

        middle_arrow_start_point = merged_password_text_visible.get_center() + 0.5*UP
        middle_arrow_end_point = lock.get_center() + 0.75*(DOWN)

        # Create the arrow
        middle_arrow = Arrow(middle_arrow_start_point, middle_arrow_end_point, buff=0.1)

        # unlocked lock
        unlocked_lock = BootstrapSVGMobject('unlock-fill', color=GREEN).scale(0.5).shift(2*UP)

        self.play(
            Create(middle_arrow),
            Transform(lock, unlocked_lock)
        )

        self.add(middle_arrow)
        self.add(unlocked_lock)
        self.remove(lock)
        self.wait(2)

        question_mark_text = MathTex(r"\textbf{How can we do this?}", color=RED).scale(2)

        self.play(
            FadeOut(middle_arrow),
            FadeOut(merged_password_text_visible),
            FadeOut(left_friend),
            FadeOut(right_friend),
            Transform(unlocked_lock, question_mark_text),
        )

        self.add(question_mark_text)
        self.remove(middle_arrow)
        self.remove(merged_password_text_visible)
        self.remove(merged_password_text_invisible)
        self.remove(unlocked_lock)
        self.remove(left_friend)
        self.remove(right_friend)
        self.wait(2)

        number_password_text = MathTex(r"\textbf{12345678}", color=GREEN).scale(2)
        
        self.play(
            Transform(question_mark_text, number_password_text)
        )

        self.add(number_password_text)
        self.remove(question_mark_text)

        self.wait(2)

        # move number_password_text up and add 2 friends
        left_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(2*(DOWN+LEFT))
        right_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(2*(DOWN+RIGHT))

        self.play(
            number_password_text.animate.shift(2*UP),
            DrawBorderThenFill(left_friend),
            DrawBorderThenFill(right_friend)
        )

        self.add(left_friend)
        self.add(right_friend)

        self.wait(2)

        number_password_text_invisible = MathTex(r"\textbf{12345678}", color=GREEN).scale(2).shift(2*UP)
        left_friend_password_text = MathTex(r"\textbf{1234}", color=YELLOW).scale(1.2).next_to(left_friend, direction=DOWN).shift(2*(UP + LEFT))
        right_friend_password_text = MathTex(r"\textbf{5678}", color=YELLOW).scale(1.2).next_to(right_friend, direction=DOWN).shift(2*(UP + RIGHT))


        self.play(
            left_friend.animate.shift(2*(UP + LEFT)),
            right_friend.animate.shift(2*(UP + RIGHT)),
            Transform(number_password_text, left_friend_password_text),
            Transform(number_password_text_invisible, right_friend_password_text)
        )

        self.add(left_friend_password_text)
        self.add(right_friend_password_text)
        self.remove(number_password_text)
        self.remove(number_password_text_invisible)

        self.wait(2)


        number_password_text = MathTex(r"\textbf{This approach has 2 problems!}", color=RED).scale(1.5).shift(2*UP)
        self.play(
            DrawBorderThenFill(number_password_text)
        )

        self.add(number_password_text)
        self.wait(2)

        problem_1_text = MathTex(r"\textbf{Problem 1: Information Leakage}", color=RED).scale(1.5).shift(2*UP)
        self.play(
            Transform(number_password_text, problem_1_text)
        )

        self.add(problem_1_text)
        self.remove(number_password_text)

        self.wait(2)

        
        self.play(
            FadeOut(left_friend),
            FadeOut(right_friend),
            FadeOut(right_friend_password_text),
            FadeOut(problem_1_text)
        )

        self.remove(left_friend)
        self.remove(right_friend)
        self.remove(right_friend_password_text)
        self.remove(problem_1_text)

        password_fragment = MathTex(r"\textbf{1234}", color=YELLOW).scale(2)

        self.play(
            TransformMatchingTex(left_friend_password_text, password_fragment)
        )

        self.add(password_fragment)
        self.remove(left_friend_password_text)




        new_password_fragment = MathTex(r"\textbf{1234}", color=YELLOW).scale(2).shift(4*LEFT)

        # Create the text
        text_1 = MathTex(r"\textbf{(0-9)}", color=YELLOW).scale(1.5).next_to(new_password_fragment, RIGHT, buff=0.1)
        
        # Create the underline
        underline_1 = Line(start=text_1.get_corner(DL), end=text_1.get_corner(DR)).next_to(text_1, DOWN, buff=0.1)

        # Create the text
        text_2 = MathTex(r"\textbf{(0-9)}", color=YELLOW).scale(1.5).next_to(text_1, RIGHT, buff=0.1)
        
        # Create the underline
        underline_2 = Line(start=text_2.get_corner(DL), end=text_2.get_corner(DR)).next_to(text_2, DOWN, buff=0.1)

        # Create the text
        text_3 = MathTex(r"\textbf{(0-9)}", color=YELLOW).scale(1.5).next_to(text_2, RIGHT, buff=0.1)
        
        # Create the underline
        underline_3 = Line(start=text_3.get_corner(DL), end=text_3.get_corner(DR)).next_to(text_3, DOWN, buff=0.1)

        # Create the text
        text_4 = MathTex(r"\textbf{(0-9)}", color=YELLOW).scale(1.5).next_to(text_3, RIGHT, buff=0.1)
        
        # Create the underline
        underline_4 = Line(start=text_4.get_corner(DL), end=text_4.get_corner(DR)).next_to(text_4, DOWN, buff=0.1)
        
        full_password_group = VGroup(new_password_fragment, text_1, text_2, text_3, text_4, underline_1, underline_2, underline_3, underline_4)

        # Display the text and the underline
        self.play(
            Transform(password_fragment, full_password_group)
        )

        self.add(full_password_group)
        self.remove(password_fragment)

        permutation_group = VGroup(text_1, text_2, text_3, text_4, underline_1, underline_2, underline_3, underline_4)

        self.play(
            TransformMatchingShapes(full_password_group, permutation_group)
        )

        self.add(permutation_group)
        self.remove(full_password_group)
        self.remove(new_password_fragment)

        self.play(
            ApplyMethod(permutation_group.shift, LEFT)
        )


        text_1 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_1, RIGHT, buff=0.1).shift(0.5*LEFT)
        text_2 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_1, RIGHT, buff=0.1)
        text_3 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_2, RIGHT, buff=0.1)
        text_4 = MathTex(r"\textbf{10}", color=YELLOW).scale(1.5).next_to(text_3, RIGHT, buff=0.1)

        permutation_calculation_group = VGroup(text_1, text_2, text_3, text_4)

        self.play(
            Transform(permutation_group, permutation_calculation_group)
        )

        self.add(permutation_calculation_group)
        self.remove(permutation_group)

        ten_thousand_text = MathTex(r"\textbf{10,000 possible combinations}", color=YELLOW).scale(1.5)

        self.play(
            Transform(permutation_calculation_group, ten_thousand_text)
        )

        self.add(ten_thousand_text)
        self.remove(permutation_calculation_group)

        self.play(
            ApplyMethod(ten_thousand_text.shift, 2*UP)
        )

        text_1 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).shift(4.5*LEFT)
        text_2 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_1, RIGHT, buff=0.1)
        text_3 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_2, RIGHT, buff=0.1)
        text_4 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_3, RIGHT, buff=0.1)
        text_5 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_4, RIGHT, buff=0.1)
        text_6 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_5, RIGHT, buff=0.1)
        text_7 = MathTex(r"\textbf{10}", "\\times", color=YELLOW).scale(1.5).next_to(text_6, RIGHT, buff=0.1)
        text_8 = MathTex(r"\textbf{10}", color=YELLOW).scale(1.5).next_to(text_7, RIGHT, buff=0.1)

        full_permutation_calculation_group = VGroup(text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8).shift(2*DOWN)

        vs_text = MathTex(r"\textbf{vs}", color=RED).scale(2)

        self.play(
            DrawBorderThenFill(vs_text),
            DrawBorderThenFill(full_permutation_calculation_group)
        )

        hundred_million_text = MathTex(r"\textbf{100,000,000 possible combinations}", color=YELLOW).scale(1.5).shift(2*DOWN)

        self.play(
            Transform(full_permutation_calculation_group, hundred_million_text)
        )

        self.add(hundred_million_text)
        self.remove(full_permutation_calculation_group)





        aim_line_1 = MathTex(r"\textbf{Aim: Find a way such that a person with a secret share}", color=YELLOW).scale(0.8)
        aim_line_2 = MathTex(r"\textbf{has the same probability of brute-forcing the secret as}", color=YELLOW).scale(0.8)
        aim_line_3 = MathTex(r"\textbf{a person without a secret share.}", color=YELLOW).scale(0.8)

        group = VGroup(aim_line_1, aim_line_2, aim_line_3)
        group.arrange(DOWN, aligned_edge=LEFT).shift(2.5*UP)

        left_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(4*(LEFT))
        equal_sign_1 = MathTex(r"\textbf{=}", color=WHITE).scale(2).shift(2*(LEFT))
        middle_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5)
        equal_sign_2 = MathTex(r"\textbf{=}", color=WHITE).scale(2).shift(2*(RIGHT))
        right_friend = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5).shift(4*(RIGHT))

        left_friend_share = MathTex(r"\textbf{1234}", color=BLUE).scale(0.8).next_to(left_friend, DOWN)
        middle_friend_share = MathTex(r"\textbf{5678}", color=BLUE).scale(0.8).next_to(middle_friend, DOWN)
        right_friend_share = MathTex(r"\textbf{No secret share}", color=BLUE).scale(0.8).next_to(right_friend, DOWN)

        bottom_text_1 = MathTex(r"\textbf{Everyone should need to calculate}", color=RED).scale(0.8).shift(3*DOWN)
        bottom_text_2 = MathTex(r"\textbf{100 million possible combinations.}", color=RED).scale(0.8).shift(4*DOWN)

        bottom_group = VGroup(bottom_text_1, bottom_text_2)
        bottom_group.arrange(DOWN, aligned_edge=LEFT).shift(3*DOWN)

        self.play(
            Transform(ten_thousand_text, group),
            FadeOut(vs_text),
            FadeOut(hundred_million_text)
        )

        self.add(group)
        self.remove(vs_text)
        self.remove(ten_thousand_text)

        self.play(
            DrawBorderThenFill(left_friend), 
            DrawBorderThenFill(left_friend_share),
        )

        self.add(left_friend)
        self.add(left_friend_share)

        self.play(
            DrawBorderThenFill(equal_sign_1),
            DrawBorderThenFill(middle_friend), 
            DrawBorderThenFill(middle_friend_share),
        )

        self.add(equal_sign_1)
        self.add(middle_friend)
        self.add(middle_friend_share)

        self.play(
            DrawBorderThenFill(equal_sign_2),
            DrawBorderThenFill(right_friend),
            DrawBorderThenFill(right_friend_share),
        )

        self.add(equal_sign_2)
        self.add(right_friend)
        self.add(right_friend_share)

        self.play(
            DrawBorderThenFill(bottom_group)
        )

        self.add(bottom_group)

        # full group includes elements from group and bottom group
        full_group = VGroup(group, bottom_group)


        # fade everything out and show the word "Randomness"
        # randomness_text = MathTex(r"\textbf{Randomness}", color=GREEN).scale(2.5)
        randomness_text = MathTex(r"\textbf{Randomness}").scale(2.5)
        randomness_text.set_color(color=[GREEN, BLUE], family=True)

        
        self.play(
            FadeOut(left_friend),
            FadeOut(left_friend_share),
            FadeOut(equal_sign_1),
            FadeOut(middle_friend),
            FadeOut(middle_friend_share),
            FadeOut(equal_sign_2),
            FadeOut(right_friend),
            FadeOut(right_friend_share),
            FadeOut(bottom_text_1),
            FadeOut(bottom_text_2),
            TransformMatchingShapes(full_group, randomness_text)
        )

        self.add(randomness_text)
        self.remove(full_group)
        self.remove(group)
        self.remove(bottom_group)
        self.remove(left_friend)
        self.remove(left_friend_share)
        self.remove(equal_sign_1)
        self.remove(middle_friend)
        self.remove(middle_friend_share)
        self.remove(equal_sign_2)
        self.remove(right_friend)
        self.remove(right_friend_share)
        self.remove(bottom_text_1)
        self.remove(bottom_text_2)

        self.wait(2)

        return [randomness_text]