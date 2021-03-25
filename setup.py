# Module: RecFeatureSelect
# Author: Daniel Ryan Furman <dryanfurman@gmail.com>
# License: MIT
# Last modified : 3.10.2021

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="RecFeatureSelect",
    version="0.1",
    author="Daniel Ryan Furman",
    author_email="dryanfurman@gmail.com",
    description=("Feature selection via recursive removal of the most correlated pair. The feature importance scores are used as the rankings, deciding which variable to drop at each call."),
    long_description="See documentation at https://github.com/daniel-furman/RecFeatureSelect",
    license="MIT",
    keywords="features, correlation, recursion, algorithms",
    url="https://github.com/daniel-furman/RecursiveFeatureSelection",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "pandas", "scipy"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
        ],
)
