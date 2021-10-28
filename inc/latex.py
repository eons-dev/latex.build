import os
import logging
import shutil
from distutils.dir_util import copy_tree, mkpath
from ebbs import Builder

class latex(Builder):
    def __init__(self, name="LaTeX document builder"):
        super().__init__(name)
    
        self.supportedProjectTypes.append("doc")

    #Required Builder method. See that class for details.
    def Build(self):
        if os.path.exists(self.buildPath):
            logging.info(f"DELETING {self.buildPath}")
            shutil.rmtree(self.buildPath)

        logging.info(f"Using build path {self.buildPath}")
        mkpath(self.buildPath)
        copy_tree(self.srcPath, os.path.join(self.buildPath))
        os.chdir(self.buildPath)
        self.RunCommand("latex -interaction=nonstopmode main.tex")
        self.RunCommand("latex -interaction=nonstopmode main.tex")