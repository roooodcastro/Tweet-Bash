#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages
import os
import utils

print utils.colorize("Starting installation of Tweet Bash...", "CYAN")

setup(name="tweet-bash",
      version=utils.app_version,
      description="Twitter app for Ubuntu's bash terminal",
      license="MIT",
      install_requires="tweepy >=1.7.1",
      author="Rodrigo Castro",
      author_email="castro.digao@gmail.com",
      url="http://github.com/roooodcastro/tweet-bash",
      packages = find_packages(),
      keywords= "twitter terminal",
      zip_safe = True)
