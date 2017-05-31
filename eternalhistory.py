#!/usr/bin/env python

# Search through shell history, output commands matching search string
# Requires .bashrc to be setup to correctly save history. See README

# Shamelessly stolen from https://twitter.com/michaelhoffman/status/639178145673932800

from __future__ import print_function
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true', help='Search all history')
parser.add_argument('--year', type=str, default=None, help='Restrict search to a given year (eg. 2015)')
parser.add_argument('--month', type=str, default=None, help='Restrict search to a given month (eg. 02)')
parser.add_argument('search', help='search string', type=str, nargs="*")

search_type = parser.add_mutually_exclusive_group()
search_type.add_argument('--and', action='store_true', dest='and_search', help='Search for intersect of all argument')
search_type.add_argument('--or', action='store_false', dest='and_search', help='Search for union of all argument')

parser.set_defaults(and_search=False)
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


first_term = args.search[0]
# recursively search for "search string" in "search_path" using grep.

command = 'grep -r {} {}'.format(first_term, search_path)
if len(args.search) > 1 and args.and_search:
    # Loop through each additional search term
    # add a pipe grepping for that term
    for term in args.search[1:]:
        command += '| grep {}'.format(term)

os.system(command)
