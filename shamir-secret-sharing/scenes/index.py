from manim import *
from sequence_1 import Sequence1
from intro import Intro

class Coreographer(Scene):
    def construct(self):
       Intro.construct(self)
       Sequence1.construct(self)
