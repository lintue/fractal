"""Library of algorithms and tools.

Includes:
- Julia
- b
- c
"""

import os

from PIL import Image


class Algorithms:
    """Mathematical functions."""

    def __init__(self, pattern, w, h, scale):
        self.pattern = pattern
        self.w = w
        self.h = h
        self.scale = scale

    def heuristic(self):
        """Heuristic for determining algorithm."""

        patterns = ["julia", "Julia", "JULIA",
                    "abc", "Abc", "ABC",
                    "cba", "Cba", "CBA"]

        if self.pattern in patterns:
            if self.pattern in patterns[0: 2]:
                image = Algorithms.julia(self)
            # elif self.pattern is b:
            #   image = Algorithms.b(self)
            # etc.
            else:
                # TO DO: raise error and/or fall back on default?
                image = Algorithms.julia(self)
        else:
            raise Exception("Please specify a valid pattern.")

        return image

    # Julia
    def julia(self):
        image = Image.new("RGB", (self.w, self.h))
        pix = image.load()

        cX, cY = -0.7, 0.27015
        moX, moY = 0.0, 0.0
        iter = 255

        for x in range(self.w):
            for y in range(self.h):
                zx = 1.5 * (x - self.w / 2) / (0.5 * self.scale * self.w) + moX
                zy = 1.0 * (y - self.h / 2) / (0.5 * self.scale * self.h) + moY
                i = iter
                while zx * zx + zy * zy < 4 and i > 1:
                    temp = zx * zx - zy * zy + cX
                    zy, zx = 2.0 * zx * zy + cY, temp
                    i -= 1
                pix[x, y] = (i << 21) + (i << 10) + i * 8

        return image


class Utils:
    """Utilities for image processing."""
    # TO DO: GIF, post-processing, etc.

    def display_img(image):
        image.show()

    def save_img(image):
        if not os.path.exists("./saved"):
            os.makedirs("./saved")
        i = 0
        while os.path.exists("./saved/fractal-%s.png" % i):
            i += 1
        image.save("./saved/fractal-%s.png" % i)
