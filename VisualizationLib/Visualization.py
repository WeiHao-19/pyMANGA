#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@date: 2018-Today
@author: jasper.bathmann@ufz.de
"""


class Visualization:
    def __init__(self, args):
        self.case = args.find("type").text
        if self.case == "SimplePyplot":
            self.iniSimplePyplot(args)
        elif self.case == "NONE":
            self.case = "No"
            self.iniNONE(args)
        else:
            raise KeyError("Required visualization type not implemented.")
        print(self.case + " visualization successfully initiated.")

    def iniSimplePyplot(self, args):
        from .SimplePyplot import SimplePyplot
        self.visualization = SimplePyplot(args)

    def iniNONE(self, args):
        from .NONE import NONE
        self.visualization = NONE(args)

    def update(self, tree_groups, time):
        self.visualization.update(tree_groups, time)

    def getVisualizationType(self):
        return self.case

    def show(self, time):
        self.visualization.show(time)
