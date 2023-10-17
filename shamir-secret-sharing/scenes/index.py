from manim import *
from intro import Intro
from sequence_1 import Sequence1
from sequence_2 import Sequence2

class Coreographer(Scene):
    def construct(self):
        eli5_text, topic_text = Intro.construct(self)
        randomness_text = Sequence1.construct(self, eli5_text, topic_text)
        # Sequence2.construct(self, randomness_text)