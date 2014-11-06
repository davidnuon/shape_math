"""

CIRCLE
	TopCENTER: 
	Filter data by selecting values above average for all Y values  
	To find TopCENTER X value, add maximum and minimum X-values and then divide by 2. 
	To Find TopCENTER y-value, use VLOOKUP command with TopCENTER X value to find the corresponding y-value. 

"""
def top_center(rows):
	yCoords = map(lambda x : x[6], rows)
	xCoords = map(lambda x : x[5], rows)
	theCoords = zip(xCoords, yCoords)

	meanY = sum(yCoords)/len(yCoords)
	meanX = sum(xCoords)/len(xCoords)

	bigYs = filter(lambda x : x[1] > meanY, theCoords)
	return bigYs




"""
	 LeftCENTER
	Filter data by selecting values below average for all X values  
	To find LeftCENTER Y value, add maximum and minimum Y values and then divide by 2. 
	To Find LeftCENTER X-value, use VLOOKUP command with LeftCENTER Y value to find the corresponding X-value. 
	RightCENTER
	Filter data by selecting values above average for all X values  
	To find RightCENTER Y value, add maximum and minimum Y values and then divide by 2. 
	To Find RightCENTER X-value, use VLOOKUP command with RightCENTER Y value to find the corresponding X-value. 
	BottomCENTER
	Filter data by selecting values below average for all Y values  
	To find BottomCENTER X value, add maximum and minimum X values and then divide by 2. 
	To Find BottomCENTER Y value, use VLOOKUP command with BottomCENTER X value to find the corresponding y-value. 

	TopLEFT
	Filter data by selecting values below average for all X values  and selecting values above average for all Y values
	Add  maximum and minimum X value and  then divide by 2 to find Point 1
	Use VLOOKUP command with point 1 to corresponding Y value (Pair 1)
	Add maximum and minimum Y value and divide by 2 to find point 2. 
	Use VLOOKUP command with point 1 to find the corresponding X value (Pair 2)
	Find the average of pair 1 and pair 2 and this will be the points for TopLEFT
	TopRIGHT
	Filter data by selecting values above average for all X values  and selecting values greater than the average for all Y values
	Add maximum and minimum X value and then divide by 2 to find point 1
	Use Excel VLOOKUP command with point 1 to find the corresponding Y value (Pair 1)
	Add maximum and minimum Y value and then divide by 2 to find point 2. 
	Use VLOOKUP command with the point 2 to find the corresponding x value (Point 2)
	Find the average of pair1 and pair 2. this will be the points for TopRIGHT
	BottomLEFT
	 Filter data by selecting values below average for all X values and selecting values below average for all Y values
	Add maximum and minimum X value and divide by 2 to find point 1
	Use Excel VLOOKUP command using point 1 to find the corresponding Y value (Pair 1)
	Add maximum and minimum Y value and divide by 2 to find point 2 
	Use VLOOKUP command with point 2 to find the corresponding X value (Pair 2)
	Find the average of pair 1 and pair 2. This will be the points for the BottomLEFT
	BottomRIGHT 
	Filter data by selecting values above average for all X values  and selecting values less than the average for the Y value 
	Add maximum and minimum X value and then divide by 2 to find point 1
	Use Excel VLOOKUP command with point one to find the corresponding Y axis (Pair 1) 
	Add maximum  and minimum Y value and divide by 2 to find point 2 
	Use VLOOKUP command with the center  y axis to find the corresponding X axis (Pair 2)
	Find the average of pair 1 and pair 2 and this will be the points for BottomRIGHT

"""