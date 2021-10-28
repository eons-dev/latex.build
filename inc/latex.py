import os
import logging
import shutil
import jsonpickle
from distutils.dir_util import copy_tree, mkpath
from ebbs import Builder

class wordpress_plugin(Builder):
    def __init__(self, name="Wordpress Plugin Builder"):
        super().__init__(name)
    
        self.supportedProjectTypes.append("plugin")

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