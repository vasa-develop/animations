from manim import *
import os

class Sequence1(Scene):
    def construct(self):
        NETFLIX_IMAGE = os.getcwd() + "/assets/netflix.jpeg"

        image = ImageMobject(NETFLIX_IMAGE)
        self.play(FadeIn(image))