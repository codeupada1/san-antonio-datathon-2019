#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

1. master-sara.ipynb
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
	Reads in the datasets from the San Antonio River Authority:
    - Flood Stage Levels
    - Rainfall Details
    - Rainfall Summary
    - Water Quality
	"""
	return pd.read_csv(path + filename, low_memory=False, error_bad_lines=False)
    

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










__authors__ = ["Joseph Burton", "Ednalyn C. De Dios", "Sandy Graham"]
__copyright__ = "Copyright 2019, Codeup Data Science"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainers__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"

