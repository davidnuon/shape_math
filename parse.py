#!/usr/bin/env python 

import sys
import cr

the_filename = sys.argv[1]

def _tonum(t):
	try:
		return float(t)
	except:
		return t

def filter_by_variable(list, cat):
	return filter(lambda x : x[2] == cat, list)


def main():
	buffy = ""
	with open(the_filename) as f:
		buffy = f.read()

	lines = buffy.split("\r")
	lines = map(lambda x : map(_tonum, x.replace('\n', '').split('\t')), lines)

	things =  filter_by_variable(lines, 1.0)

	print cr.top_center(things)



if __name__ == '__main__':
	main()