from lib import *
import cr

"""
	TopCENTER 
	Filter data by selecting values above average for all Y values  
	To find TopCENTER X value, add maximum and minimum X-values and then divide by 2. 
	To Find TopCENTER Y-value, use VLOOKUP command with TopCENTER X value to find the corresponding y-value. 
"""

def top_center(rows):
	return cr.top_center(rows)

def left_center(rows):
	return cr.left_center(rows)

def right_center(rows):
	return cr.right_center(rows)

def bottom_center(rows):
	return cr.bottom_center(rows)

def top_left(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] < meanX and v[Y_AXIS] > meanY, theCoords)
	minX = min(map(lambda v: v[X_AXIS], bigList))
	maxY = max(map(lambda v: v[Y_AXIS], bigList))
	return (minX, maxY)

def top_right(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] > meanX and v[Y_AXIS] > meanY, theCoords)
	minX = max(map(lambda v: v[X_AXIS], bigList))
	maxY = max(map(lambda v: v[Y_AXIS], bigList))
	return (minX, maxY)

def bottom_left(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] < meanX and v[Y_AXIS] < meanY, theCoords)
	minX = min(map(lambda v: v[X_AXIS], bigList))
	maxY = min(map(lambda v: v[Y_AXIS], bigList))
	return (minX, maxY)

def bottom_right(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] > meanX and v[Y_AXIS] < meanY, theCoords)
	minX = max(map(lambda v: v[X_AXIS], bigList))
	maxY = min(map(lambda v: v[Y_AXIS], bigList))
	return (minX, maxY)


# """
# 	LeftCENTER 
# 	Filters data by selecting cases below average in the X values
# 	Subtract maximum and minimum Y value and divide by 2 to find center Y values
# 	Use VLOOKUP command with center Y value to find center X value
# 	RightCENTER 
# 	Filter data by selecting cases above average  for  all X values
# 	Subtract maximum and Minimum y value and divide by 2 to find center Y value
# 	Use VLOOKUP command with center y axis to find center X value 
# 	BottomCENTER 
# 	Filter data by selecting values below average for all Y values 
# 	Subtract maximum  from minimum  X value and then divide by 2 to find center X value 
# 	Use VLOOKUP command with center X value to find center Y value 
# 	TopLEFT
# 	Filter data by selecting values below average for all X values and selecting all values greater than the average in all Y values
# 	Find minimum x value and  find maximum y value
# 	TopRIGHT
# 	Filter data by selecting values above average for all  X values and selecting values above average for all  Y values
# 	Find maximum x value and find maximum y value
# 	BottomLEFT
# 	Filter data by selecting values below average for all X values and selecting values below average for all Y values
# 	Find minimum X value  and find minimum  Y value
# 	BottomRIGHT
# 	Filter data by selecting values above average for X values and selecting values below average for all Y values
# 	Find maximum X values and find minimum Y value 
# """"