#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

1. sewer-dd.ipynb
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
	Reads in a subset of the dataset: Chicago Women's
	Health Risk Study, 1995-1998 (ICPSR 3002)

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










__authors__ = ["Ednalyn C. De Dios, et al.", "Jesse J. Ruiz"]
__copyright__ = "Copyright 2019, Codeup Data Science"
__credits__ = ["Maggie Guist", "Zach Gulde"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainers__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"

