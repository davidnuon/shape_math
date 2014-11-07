#!/usr/bin/env python 

import sys
import cr
import sq

the_filename = sys.argv[1]

def _tonum(t):
	try:
		return float(t)
	except:
		return t

def filter_by_variable(list, cat):
	return filter(lambda x : x[2] == cat, list)

def process_circles(things):
	print "Top Center: %s " % str(cr.top_center(things))
	print "Left Center: %s" % str(cr.left_center(things))
	print "Right Center: %s" % str(cr.right_center(things))
	print "Bottom Center: %s" % str(cr.bottom_center(things))
	print "Top Left: %s" % str(cr.top_left(things))
	print "Top Right: %s" % str(cr.top_right(things))
	print "Bottom Left: %s" % str(cr.bottom_left(things))
	print "Bottom Right: %s" % str(cr.bottom_right(things))

def process_squares(things):
	print "Top Center: %s " % str(sq.top_center(things))
	print "Left Center: %s" % str(sq.left_center(things))
	print "Right Center: %s" % str(sq.right_center(things))
	print "Bottom Center: %s" % str(sq.bottom_center(things))
	print "Top Left: %s" % str(sq.top_left(things))
	print "Top Right: %s" % str(sq.top_right(things))
	print "Bottom Left: %s" % str(sq.bottom_left(things))
	print "Bottom Right: %s" % str(sq.bottom_right(things))

def main():
	buffy = ""
	with open(the_filename) as f:
		buffy = f.read()

	lines = buffy.split("\r")
	lines = map(lambda x : map(_tonum, x.replace('\n', '').split('\t')), lines)

	things =  filter_by_variable(lines, 2.0)
	process_squares(things)


if __name__ == '__main__':
	main()