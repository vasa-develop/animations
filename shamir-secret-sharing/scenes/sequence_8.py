from manim import *
from utils.bootstrap_svg import BootstrapSVGMobject

class Sequence8(Scene):
    
    def construct(self):
        """
        TODO: Add animation for 
        
        Now let's discuss the second problem.
        """

        secret_text = MathTex(r"\textbf{secret}", color=RED).scale(1.3).shift(5*LEFT)
        plus_sign = MathTex(r"\textbf{+}", color=WHITE).scale(1.3).next_to(secret_text, RIGHT)
        random_number_text = MathTex(r"\textbf{randomess}", color=BLUE).scale(1.3).next_to(plus_sign, RIGHT)
        equal_to_sign = MathTex(r"\textbf{=}", color=WHITE).scale(1.3).next_to(random_number_text, RIGHT)
        random_secret_text = MathTex(r"\textbf{random secret}").scale(1.3).next_to(equal_to_sign, RIGHT)
        random_secret_text.set_color(color=[GREEN, BLUE], family=True)

        self.play(
            DrawBorderThenFill(secret_text),
            DrawBorderThenFill(plus_sign),
            DrawBorderThenFill(random_number_text),
            DrawBorderThenFill(equal_to_sign),
            DrawBorderThenFill(random_secret_text)
        )
        self.add(secret_text, plus_sign, random_number_text, equal_to_sign, random_secret_text)

        left_person_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2.5*(LEFT)).shift(DOWN)
        right_person_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2.5*(RIGHT)).shift(DOWN)
        left_person_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2.5*(LEFT)).shift(DOWN)
        right_person_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2.5*(RIGHT)).shift(DOWN)
        lock = BootstrapSVGMobject('lock-fill', color=RED).scale(0.5).shift(2*(UP))
        unlock = BootstrapSVGMobject('unlock-fill', color=GREEN).scale(0.5).shift(2*(UP))

        self.play(
            secret_text.animate.move_to(lock.get_center()),
            random_number_text.animate.move_to(left_person_locked.get_center()),
            random_secret_text.animate.move_to(right_person_locked.get_center()),
            FadeOut(plus_sign),
            FadeOut(equal_to_sign)
        )
        self.remove(plus_sign, equal_to_sign)

        self.play(
            Transform(secret_text, lock),
            Transform(random_number_text, left_person_locked),
            Transform(random_secret_text, right_person_locked)
        )
        self.add(lock, left_person_locked, right_person_locked)
        self.remove(secret_text, random_number_text, random_secret_text)

        self.play(
            Transform(lock, unlock),
            Transform(left_person_locked, left_person_check),
            Transform(right_person_locked, right_person_check)
        )
        self.add(unlock, left_person_check, right_person_check)
        self.remove(lock, left_person_locked, right_person_locked)

        lock = BootstrapSVGMobject('lock-fill', color=RED).scale(0.5).shift(2*(UP))
        
        person_1_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(4*(LEFT)).shift(0.5*DOWN)
        person_2_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2*(LEFT)).shift(0.5*DOWN)
        person_3_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(0.5*DOWN)
        person_4_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2*(RIGHT)).shift(0.5*DOWN)
        person_5_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(4*(RIGHT)).shift(0.5*DOWN)

        person_6_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(4*(LEFT)).shift(2.5*DOWN)
        person_7_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2*(LEFT)).shift(2.5*DOWN)
        person_8_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2.5*DOWN)
        person_9_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(2*(RIGHT)).shift(2.5*DOWN)
        person_10_locked = BootstrapSVGMobject('person-fill-lock', color=BLUE).scale(0.5).shift(4*(RIGHT)).shift(2.5*DOWN)

        person_1_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(4*(LEFT)).shift(0.5*DOWN)
        person_2_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2*(LEFT)).shift(0.5*DOWN)
        person_3_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(0.5*DOWN)
        person_4_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2*(RIGHT)).shift(0.5*DOWN)
        person_5_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(4*(RIGHT)).shift(0.5*DOWN)

        person_6_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(4*(LEFT)).shift(2.5*DOWN)
        person_7_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2*(LEFT)).shift(2.5*DOWN)
        person_8_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(0.5*DOWN)
        person_9_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(2*(RIGHT)).shift(2.5*DOWN)
        person_10_check = BootstrapSVGMobject('person-fill-check', color=GREEN).scale(0.5).shift(4*(RIGHT)).shift(2.5*DOWN)

        person_3_x = BootstrapSVGMobject('person-fill-x', color=GRAY).scale(0.5).shift(0.5*DOWN)
        person_9_x = BootstrapSVGMobject('person-fill-x', color=GRAY).scale(0.5).shift(2*(RIGHT)).shift(2.5*DOWN)

        self.play(
            Transform(unlock, lock),
            FadeOut(left_person_check),
            FadeOut(right_person_check),
            DrawBorderThenFill(person_1_locked),
            DrawBorderThenFill(person_2_locked),
            DrawBorderThenFill(person_3_locked),
            DrawBorderThenFill(person_4_locked),
            DrawBorderThenFill(person_5_locked),
            DrawBorderThenFill(person_6_locked),
            DrawBorderThenFill(person_7_locked),
            DrawBorderThenFill(person_8_locked),
            DrawBorderThenFill(person_9_locked),
            DrawBorderThenFill(person_10_locked),
        )
        self.add(lock, person_1_locked, person_2_locked, person_3_locked, person_4_locked, person_5_locked, person_6_locked, person_7_locked, person_8_locked, person_9_locked, person_10_locked)
        self.remove(unlock, left_person_check, right_person_check)

        self.play(
            Transform(person_3_locked, person_3_x),
        )
        self.add(person_3_x)
        self.remove(person_3_locked)

        self.play(
            Transform(person_9_locked, person_9_x),
        )
        self.add(person_9_x)
        self.remove(person_9_locked)


        self.play(
            Transform(person_1_locked, person_1_check),
        )
        self.add(person_1_check)
        self.remove(person_1_locked)

        self.play(
            Transform(person_2_locked, person_2_check),
        )
        self.add(person_2_check)
        self.remove(person_2_locked)

        unlock = BootstrapSVGMobject('unlock-fill', color=RED).scale(0.5).shift(2*(UP))

        self.play(
            Transform(lock, unlock)
        )
        self.add(unlock)
        self.remove(lock)


        self.wait(2)




