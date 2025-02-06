import os
import logging
import shutil
from distutils.dir_util import copy_tree
from ebbs import Builder

class latex(Builder):
    def __init__(this, name="LaTeX document builder"):
        super().__init__(name)
    
        this.supportedProjectTypes.append("doc")

    #Required Builder method. See that class for details.
    def Build(this):

        if (this.incPath is not None):
            copy_tree(this.incPath, this.buildPath)

        copy_tree(this.srcPath, this.buildPath)
        this.RunCommand("lualatex -interaction=nonstopmode main.tex")
        this.RunCommand("lualatex -interaction=nonstopmode main.tex")