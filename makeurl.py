#!/usr/bin/env python3.6

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

url = 'https://raw.githubusercontent.com/luhux/images/master/' + filename
print(url)
