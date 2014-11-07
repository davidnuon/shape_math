from lib import *

"""

CIRCLE
	TopCENTER: 
	Filter data by selecting values above average for all Y values  
	To find TopCENTER X value, add maximum and minimum X-values and then divide by 2. 
	To Find TopCENTER y-value, use VLOOKUP command with TopCENTER X value to find the corresponding y-value. 

"""
def top_center(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)

	meanY = mean(yCoords)

	bigYs    = find_bigs(theCoords, Y_AXIS, meanY)
	bigYsMIN = find_min_component(bigYs, X_AXIS) 
	bigYsMAX = find_max_component(bigYs, X_AXIS) 
	centerX  = center(bigYsMAX,bigYsMIN)

	return vlookup(theCoords, X_AXIS, centerX)

"""
	LeftCENTER
	
	Filter data by selecting values below average for all X values  
	To find LeftCENTER Y value, add maximum and minimum Y values and then divide by 2. 
	To Find LeftCENTER X-value, use VLOOKUP command with LeftCENTER Y value to find the corresponding X-value. 
"""

def left_center(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)

	meanX = mean(xCoords)

	smallXs    = find_smalls(theCoords, X_AXIS, meanX)
	smallXsMIN = find_min_component(smallXs, Y_AXIS) 
	smallXsMAX = find_max_component(smallXs, Y_AXIS) 
	centerY  = center(smallXsMAX,smallXsMIN)

	return vlookup(theCoords, Y_AXIS, centerY)

"""
	RightCENTER
	Filter data by selecting values above average 
	for all X values  
	To find RightCENTER Y value, add maximum and minimum Y values and then divide by 2. 
	To Find RightCENTER X-value, use VLOOKUP command with RightCENTER Y value to find the corresponding X-value. 
"""
def right_center(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)

	bigXs = find_bigs(theCoords, X_AXIS, meanX)
	bigXsMIN = find_min_component(bigXs, Y_AXIS) 
	bigXsMAX = find_max_component(bigXs, Y_AXIS) 
	centerY  = center(bigXsMAX,bigXsMIN)

	return vlookup(theCoords, Y_AXIS, centerY)

"""	BottomCENTER
	Filter data by selecting values below average for all Y values  
	To find BottomCENTER X value, add maximum and minimum X values and then divide by 2. 
	To Find BottomCENTER Y value, use VLOOKUP command with BottomCENTER X value to find the corresponding y-value. 
"""
def bottom_center(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanY = mean(yCoords)
	smallYs = find_smalls(theCoords, Y_AXIS, meanY)
	smallXsMIN = find_min_component(smallYs, X_AXIS)
	smallXsMAX = find_max_component(smallYs, X_AXIS)
	
	centerX = center(smallXsMIN, smallXsMAX)
	return vlookup(theCoords, X_AXIS, centerX)


"""
	TopLEFT
	Filter data by selecting values below average for all X values  and selecting values above average for all Y values
	Add  maximum and minimum X value and  then divide by 2 to find Point 1
	Use VLOOKUP command with point 1 to corresponding Y value (Pair 1)
	Add maximum and minimum Y value and divide by 2 to find point 2. 
	Use VLOOKUP command with point 1 to find the corresponding X value (Pair 2)
	Find the average of pair 1 and pair 2 and this will be the points for TopLEFT
	"""
def top_left(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] < meanX and v[Y_AXIS] > meanY, theCoords)

	bigListMIN_X = find_min_component(bigList, X_AXIS)
	bigListMAX_X = find_max_component(bigList, X_AXIS)
	centerX = center(bigListMIN_X, bigListMAX_X)

	bigListMIN_Y = find_min_component(bigList, Y_AXIS)
	bigListMAX_Y = find_max_component(bigList, Y_AXIS)
	centerY = center(bigListMIN_Y, bigListMAX_Y)	

	pointA = vlookup(theCoords, X_AXIS, centerX)
	pointB = vlookup(theCoords, Y_AXIS, centerY)

	return ( (pointA[X_AXIS] + pointB[X_AXIS])/2, (pointA[Y_AXIS] + pointB[Y_AXIS])/2) 


	"""
	TopRIGHT
	Filter data by selecting values above average for all X values  and selecting values greater than the average for all Y values
	Add maximum and minimum X value and then divide by 2 to find point 1
	Use Excel VLOOKUP command with point 1 to find the corresponding Y value (Pair 1)
	Add maximum and minimum Y value and then divide by 2 to find point 2. 
	Use VLOOKUP command with the point 2 to find the corresponding x value (Point 2)
	Find the average of pair1 and pair 2. this will be the points for TopRIGHT
	"""

def top_right(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] > meanX and v[Y_AXIS] > meanY, theCoords)

	bigListMIN_X = find_min_component(bigList, X_AXIS)
	bigListMAX_X = find_max_component(bigList, X_AXIS)
	centerX = center(bigListMIN_X, bigListMAX_X)

	bigListMIN_Y = find_min_component(bigList, Y_AXIS)
	bigListMAX_Y = find_max_component(bigList, Y_AXIS)
	centerY = center(bigListMIN_Y, bigListMAX_Y)	

	pointA = vlookup(theCoords, X_AXIS, centerX)
	pointB = vlookup(theCoords, Y_AXIS, centerY)

	return ( (pointA[X_AXIS] + pointB[X_AXIS])/2, (pointA[Y_AXIS] + pointB[Y_AXIS])/2) 

	"""
	BottomLEFT
	 Filter data by selecting values below average for all X values and selecting values below average for all Y values
	Add maximum and minimum X value and divide by 2 to find point 1
	Use Excel VLOOKUP command using point 1 to find the corresponding Y value (Pair 1)
	Add maximum and minimum Y value and divide by 2 to find point 2 
	Use VLOOKUP command with point 2 to find the corresponding X value (Pair 2)
	Find the average of pair 1 and pair 2. This will be the points for the BottomLEFT
"""

def bottom_left(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] < meanX and v[Y_AXIS] < meanY, theCoords)

	bigListMIN_X = find_min_component(bigList, X_AXIS)
	bigListMAX_X = find_max_component(bigList, X_AXIS)
	centerX = center(bigListMIN_X, bigListMAX_X)

	bigListMIN_Y = find_min_component(bigList, Y_AXIS)
	bigListMAX_Y = find_max_component(bigList, Y_AXIS)
	centerY = center(bigListMIN_Y, bigListMAX_Y)	

	pointA = vlookup(theCoords, X_AXIS, centerX)
	pointB = vlookup(theCoords, Y_AXIS, centerY)

	return ( (pointA[X_AXIS] + pointB[X_AXIS])/2, (pointA[Y_AXIS] + pointB[Y_AXIS])/2) 

"""	
	BottomRIGHT 
	Filter data by selecting values above average for all X values  and selecting values less than the average for the Y value 
	Add maximum and minimum X value and then divide by 2 to find point 1
	Use Excel VLOOKUP command with point one to find the corresponding Y axis (Pair 1) 
	Add maximum  and minimum Y value and divide by 2 to find point 2 
	Use VLOOKUP command with the center  y axis to find the corresponding X axis (Pair 2)
	Find the average of pair 1 and pair 2 and this will be the points for BottomRIGHT

"""
def bottom_right(rows):
	yCoords, xCoords, theCoords = parse_rows(rows)
	meanX = mean(xCoords)
	meanY = mean(yCoords)
	bigList = filter(lambda v : v[X_AXIS] > meanX and v[Y_AXIS] < meanY, theCoords)

	bigListMIN_X = find_min_component(bigList, X_AXIS)
	bigListMAX_X = find_max_component(bigList, X_AXIS)
	centerX = center(bigListMIN_X, bigListMAX_X)

	bigListMIN_Y = find_min_component(bigList, Y_AXIS)
	bigListMAX_Y = find_max_component(bigList, Y_AXIS)
	centerY = center(bigListMIN_Y, bigListMAX_Y)	

	pointA = vlookup(theCoords, X_AXIS, centerX)
	pointB = vlookup(theCoords, Y_AXIS, centerY)

	return ( (pointA[X_AXIS] + pointB[X_AXIS])/2, (pointA[Y_AXIS] + pointB[Y_AXIS])/2) 
