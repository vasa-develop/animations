from manim import *

class Test(Scene):
    def construct(self):
        self.opening()
        self.introduction()

    def opening(self):
        eli5_text = MathTex(r"\text{ELI5}", color=BLUE).scale(3).shift(2*UP)
        topic_text = MathTex(r"\text{Shamir Secret Sharing and Lagrange Interpolation}", color=WHITE).shift(1*DOWN)
        self.play(DrawBorderThenFill(eli5_text), DrawBorderThenFill(topic_text), run_time=5)
        self.wait(2)

        #clear screen
        self.play(FadeOut(eli5_text), FadeOut(topic_text))

    def introduction(self):
        NETFLIX_IMAGE = "./scenes/assets/netflix.jpeg"

        image = ImageMobject(NETFLIX_IMAGE)
        self.play(DrawBorderThenFill(image))


class Opening(Scene):
    def construct(self):
        eli5_text = MathTex(r"\text{ELI5}", color=BLUE).scale(3).shift(2*UP)
        topic_text = MathTex(r"\text{Shamir Secret Sharing and Lagrange Interpolation}", color=WHITE).shift(1*DOWN)
        self.play(DrawBorderThenFill(eli5_text), DrawBorderThenFill(topic_text), run_time=5)
        self.wait(2)

class Introduction(Scene):
    def construct(self):
        NETFLIX_IMAGE = "./scenes/assets/netflix.png"

        image = ImageMobject(NETFLIX_IMAGE)
        self.play(GrowFromCenter(image))



from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class TwitterEmojiSVGMobject(SVGMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = '-'.join(f'{ord(c):x}' for c in emoji)
        url = f'https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{emoji_code}.svg'
        path_svg = Path.cwd() / f'{emoji_code}.svg'
        urllib.request.urlretrieve(url, path_svg)
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class TwitterEmoji(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        em = TwitterEmojiSVGMobject('🧑‍💻').scale(0.5)
        t = Text('Twitter (SVG)').scale(2)
        Group(em, t).arrange(DOWN).scale(1.6)
        self.play(DrawBorderThenFill(em))

        # transform emoji into a dot
        dot = Dot(color=WHITE).scale(0.5)
        dot.move_to(em.get_center())
        self.play(Transform(em, dot))

        self.wait(4)








from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class OpenEmojiSVGMobject(SVGMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = '-'.join(f'{ord(c):x}' for c in emoji)
        emoji_code = emoji_code.upper()  # <-  needed for openmojis
        url = f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{emoji_code}.svg'
        path_svg = Path.cwd() / f'{emoji_code}.svg'
        urllib.request.urlretrieve(url, path_svg)
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class OpenEmoji(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        em = OpenEmojiSVGMobject('🧑')
        t = Text('OpenMoji (SVG)').scale(2)
        Group(em, t).arrange(DOWN).scale(1.4)
        self.play(DrawBorderThenFill(em))

        # transform emoji into a dot
        dot = Dot(color=WHITE).scale(0.5)
        dot.move_to(em.get_center())
        self.play(Transform(em, dot))

        self.wait(4)

from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class BootstrapSVGMobject(SVGMobject):
    def __init__(self, emoji, color=BLACK, **kwargs):
        url = f'https://raw.githubusercontent.com/twbs/icons/main/icons/{emoji}.svg'
        path_svg = Path.cwd() / f'{emoji}.svg'
        urllib.request.urlretrieve(url, path_svg)
        path_svg.write_text(path_svg.read_text().replace('currentColor', color))
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class BootstrapEmoji(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        em = BootstrapSVGMobject('emoji-smile-fill', color=BLUE).scale(0.5)
        # more at https://icons.getbootstrap.com/
        t = Text('Bootstrap (SVG)').scale(2)
        Group(em, t).arrange(DOWN).scale(1.4)
        self.play(DrawBorderThenFill(em))

        # transform emoji into a dot
        dot = Dot(color=RED).scale(2)
        dot.move_to(em.get_center())
        self.play(Transform(em, dot))

        self.wait(4)