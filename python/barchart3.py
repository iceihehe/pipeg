# -*- coding=utf-8 -*-

import abc
import os
import re
import tempfile
import Qtrac
try:
    import cyImage as Image
except ImportError:
    import Image


def main():
    pairs = (("Mon", 16), ("Tue", 17), ("Wed", 19), ("Thu", 22),
            ("Fri", 24), ("Sat", 21), ("Sun", 19))
    textBarCharter = BarCharter(TextBarRenderer())
    textBarCharter.render("Forecast 6/8", pairs)


@Qtrac.has_methods("initialize", "draw_caption", "draw_bar","finalize")
class BarRenderer:

    __metaclass__ = abc.ABCMeta


class BarCharter:

    def __init__(self, renderer):
        if not isinstance(renderer, BarRenderer):
            raise TypeError("Expected object of type BarRenderer, got {}".
                    format(type(renderer).__name__))
        self.__renderer = renderer


    def render(self, caption, pairs):
        maximum = max(value for _, value in pairs)
        self.__renderer.initialize(len(pairs), maximum)
        self.__renderer.draw_caption(caption)
        for name, value in pairs:
            self.__renderer.draw_bar(name, value)
        self.__renderer.finalize()


class TextBarRenderer(object):

    def __init__(self, scaleFactor=40):
        self.scaleFactor = scaleFactor


    def initialize(self, bars, maximum):
        assert bars > 0 and maximum > 0
        self.scale = self.scaleFactor / maximum


    def draw_caption(self, caption):
        print("{0:^{2}}\n{1:^{2}}".format(caption, "=" * len(caption),
                self.scaleFactor))


    def draw_bar(self, name, value):
        print("{} {}".format("*" * int(value * self.scale), name))


    def finalize(self):
        pass



if __name__ == "__main__":
    main()
