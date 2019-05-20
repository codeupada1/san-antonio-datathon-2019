#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

1. dd-wrangling.ipynb
2.
3.

"""



# ===========
# ENVIRONMENT
# ===========


import os
import sys

import pandas as pd

from env import path



# ===========
# ACQUISITION
# ===========


def read_data(filename):
	"""
	Reads in the dataset: Sanitary Sewer Overflow (SSO)
    from the San Antonio Water System (SAWS)

	"""
	return pd.read_csv(path + filename, low_memory=False)




# ==================================================
# MAIN
# ==================================================


def clear():
	os.system("cls" if os.name == "nt" else "clear")

def main():
    """Main entry point for the script."""
    pass


if __name__ == '__main__':
    sys.exit(main())










__authors__ = ["Joseph Burton", "Ednalyn C. De Dios", "Jason Dunn", "Sandy Graham", "Jesse J. Ruiz"]
__copyright__ = "Copyright 2019, Codeup Data Science"
__credits__ = ["Maggie Guist", "Zach Gulde"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainers__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"

