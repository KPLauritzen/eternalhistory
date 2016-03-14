#!/usr/bin/env python

# Search through shell history, output commands matching search string
# Requires .bashrc to be setup to correctly save history. See README

# Shamelessly stolen from https://twitter.com/michaelhoffman/status/639178145673932800

from __future__ import (print_function, division, absolute_import)
import argparse
import logging as log
import subprocess as sp
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true', help='Search all history')
parser.add_argument('--year', type=str, default=None, help='Restrict search to this year (eg. 2015)')
parser.add_argument('--month', type=str, default=None, help='Restrict search to this month (eg. 02)')
parser.add_argument('-s', '--search', help='search string', type=str, required=True)
args = parser.parse_args()

# Get strings for current date
curr_year = time.strftime('%Y')
curr_month = time.strftime('%m')
curr_day = time.strftime('%d')

# Check if year or month was set. Otherwise use current date
if args.year is None:
    search_year = curr_year
else:
    search_year = args.year

if args.month is None:
    search_month = curr_month
else:
    search_month = args.month


# The command history is saved in subdirs of this folder
root_path = os.path.expanduser('~/.history')
if args.all:
    search_path = root_path
elif args.month is not None:
    search_path = '{root_path}/{search_year}/{search_month}'.format(**locals())
elif args.year is not None:
    search_path = '{root_path}/{search_year}'.format(**locals())
else:
    search_path = '{root_path}/{curr_year}/{curr_month}'.format(**locals())


search_string = args.search
# recursively search for "search string" in "search_path" using grep.
try:
    search_hist = sp.check_output(['grep', '-r', search_string, search_path])
# check_output throws an error if the command returns nothing.
except sp.CalledProcessError:
    search_hist = 'no results'

# Show the actual output of the command
print(search_hist)
