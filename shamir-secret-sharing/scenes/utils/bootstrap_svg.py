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