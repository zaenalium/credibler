from codecs import open
from os import path
import re

from setuptools import setup,find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = "credibler",
    version = "0.0.1",
    author="zaenal",
    author_email="ahmadzaenal125@gmail.com",
    url = "https://github.com/zaenalium/credibler",
    license = "MIT License",
    description = "Advanced credit scoring risk modeling",
    long_description = long_description,
    keywords = ["credit scoring", "scorecard", "EDA","data preprocessing", "binning"],
    packages = find_packages(),
    # include_package_data = True,
    install_requires = ['ydata-profiling>=4.3.2','numpy>=1.18.1',
                        'matplotlib>=3.1.3','pandas>=1.0.3','scikit-learn>=0.23.1','imbalanced-learn==0.11.0',
                        'statsmodels>=0.11.1','scorecardpy>=0.1.9.2','seaborn>=0.10.1','scipy>=1.4.1','toad>=0.0.60'
                        ]
)