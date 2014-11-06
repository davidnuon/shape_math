"""
•	TopCENTER 
	•	Filter data by selecting values above average for all Y values  
	•	To find TopCENTER X value, add maximum and minimum X-values and then divide by 2. 
	•	To Find TopCENTER Y-value, use VLOOKUP command with TopCENTER X value to find the corresponding y-value. 
"""

#	0    1    2    3   4        5            6  
# [4.0, 'c', 1.0, 'c', 1393.0, 63.40470236, 43.4568177]
def top_center(rows):
	
	# meanY = sum(map(lambda x : x[6], rows))/len(rows)

"""
	•	LeftCENTER 
	•	Filters data by selecting cases below average in the X values
	•	Subtract maximum and minimum Y value and divide by 2 to find center Y values
	•	Use VLOOKUP command with center Y value to find center X value
	•	RightCENTER 
	•	Filter data by selecting cases above average  for  all X values
	•	Subtract maximum and Minimum y value and divide by 2 to find center Y value
	•	Use VLOOKUP command with center y axis to find center X value 
	•	BottomCENTER 
	•	Filter data by selecting values below average for all Y values 
	•	Subtract maximum  from minimum  X value and then divide by 2 to find center X value 
	•	Use VLOOKUP command with center X value to find center Y value 
	•	TopLEFT
	•	Filter data by selecting values below average for all X values and selecting all values greater than the average in all Y values
	•	Find minimum x value and  find maximum y value
	•	TopRIGHT
	•	Filter data by selecting values above average for all  X values and selecting values above average for all  Y values
	•	Find maximum x value and find maximum y value
	•	BottomLEFT
	•	Filter data by selecting values below average for all X values and selecting values below average for all Y values
	•	Find minimum X value  and find minimum  Y value
	•	BottomRIGHT
	•	Filter data by selecting values above average for X values and selecting values below average for all Y values
	•	Find maximum X values and find minimum Y value 
""""