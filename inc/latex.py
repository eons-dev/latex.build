import os
import logging
import shutil
from distutils.dir_util import copy_tree, mkpath
from ebbs import Builder

class latex(Builder):
    def __init__(this, name="LaTeX document builder"):
        super().__init__(name)
    
        this.supportedProjectTypes.append("doc")

    #Required Builder method. See that class for details.
    def Build(this):
        copy_tree(this.incPath, this.buildPath)
        copy_tree(this.srcPath, this.buildPath)
        this.RunCommand("pdflatex -interaction=nonstopmode main.tex")
        this.RunCommand("pdflatex -interaction=nonstopmode main.tex")