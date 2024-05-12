from setuptools import find_packages

name = "DRAWING WITH A.I"
version = "0.1.0"

packages = find_packages()

install_requires = ["-r requirements.txt"]

author = "TDN-M"
author_email = "dung.ngt1988@gmail.com"
description = "App for LLM Drawing Evaluation"
long_description = "App that generates random themes, allows user drawing and evaluates drawings using LLM."
url = "https://github.com/TDNM88"

setup_requirements = ["setuptools>=40"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Framework :: Transformers",
]