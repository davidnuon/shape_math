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

	print "Top Center: %s " % str(cr.top_center(things))
	print "Left Center: %s" % str(cr.left_center(things))
	print "Right Center: %s" % str(cr.right_center(things))
	print "Bottom Center: %s" % str(cr.bottom_center(things))
	print "Top Left: %s" % str(cr.top_left(things))
	print "Top Right: %s" % str(cr.top_right(things))
	print "Bottom Left: %s" % str(cr.bottom_left(things))
	print "Bottom Right: %s" % str(cr.bottom_right(things))

if __name__ == '__main__':
	main()