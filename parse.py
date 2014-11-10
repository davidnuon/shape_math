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
	return {"top_center" : cr.top_center(things),
	"left_center" : cr.left_center(things),
	"right_center" : cr.right_center(things),
	"bottom_center" : cr.bottom_center(things),
	"top_left" : cr.top_left(things),
	"top_right" : cr.top_right(things),
	"bottom_left" : cr.bottom_left(things),
	"bottom_right" : cr.bottom_right(things)}

def process_squares(things):
	return {"top_center" : sq.top_center(things),
	"left_center" : sq.left_center(things),
	"right_center" : sq.right_center(things),
	"bottom_center" : sq.bottom_center(things),
	"top_left" : sq.top_left(things),
	"top_right" : sq.top_right(things),
	"bottom_left" : sq.bottom_left(things),
	"bottom_right" : sq.bottom_right(things)}


def format_result(result):
	template = "%s,%s,%s,%s," +  ",".join((["%.4f"] * 16))
	return template % (
		str(result['participant']),
		str(result['trial']),
		str(result['target']),
		str(result['compatible']),
		result["data"]["top_center"][0],
		result["data"]["top_center"][1],
		result["data"]["left_center"][0],
		result["data"]["left_center"][1],
		result["data"]["right_center"][0],
		result["data"]["right_center"][1],
		result["data"]["bottom_center"][0],
		result["data"]["bottom_center"][1],
		result["data"]["top_left"][0],
		result["data"]["top_left"][1],
		result["data"]["top_right"][0],
		result["data"]["top_right"][1],
		result["data"]["bottom_left"][0],
		result["data"]["bottom_left"][1],
		result["data"]["bottom_right"][0],
		result["data"]["bottom_right"][1]	
	)

def main():
	buffy = ""
	with open(the_filename) as f:
		buffy = f.read()

	lines = buffy.split("\n")
	lines = map(lambda x : map(_tonum, x.replace('\n', '').split(',')), lines)
	lines = filter(lambda line: len(line) == 7, lines)
	
	participants = set(map(lambda x : x[0], lines))
	for participant in participants:
		current_data = filter(lambda x : x[0] == participant, lines)

		trials = set(map(lambda x : x[2], current_data))
		experimentData = []
		for trial in trials:
			rows  = filter_by_variable(current_data, trial)
			targetShape = rows[0][3]
			compatible  = rows[0][1] == 'c'
			result = {}
				
			if compatible:
				if targetShape == 'c':
					result['data'] = process_circles(rows)
				elif targetShape == 's':
					result['data'] = process_squares(rows)
			else:
				if targetShape == 'c':
					result['data'] = process_squares(rows)
				elif targetShape == 's':
					result['data'] = process_circles(rows)

			result['participant'] = int(rows[0][0])
			result['trial'] = int(trial)
			result['target'] = targetShape
			result['compatible'] = 'C' if compatible else 'I'

			experimentData.append(result)

	header =  "participant,trial,target,compatible,topCenterX,topCenterY,leftCenterX,leftCenterY,rightCenterX,rightCenterY,bottomCenterX,bottomCenterY,topLeftX,topLeftY,topRightX,topRightY,bottomLeftX,bottomLeftY,bottomRightX,bottomRightY"
	print header

	for e in experimentData:
 		print format_result(e)


if __name__ == '__main__':
	main()