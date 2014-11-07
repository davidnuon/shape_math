def mean(coords):
	return sum(coords)/len(coords)

def find_bigs(theCoords, idx, threshold):
	return filter(lambda x : x[idx] > threshold, theCoords)

def find_smalls(theCoords, idx, threshold):
	return filter(lambda x : x[idx] < threshold, theCoords)


def find_min_component(theCoords, idx):
	return min(map(lambda x : x[idx], theCoords)) 

def find_max_component(theCoords, idx):
	return max(map(lambda x : x[idx], theCoords)) 	

def center(a,b):
	return (a + b)/2


def vlookup(theCoords, idx, threshold):
	diffs = map(lambda x : abs(x[idx] - threshold), theCoords)
	return sorted(zip(diffs, theCoords))[0][1]


X_AXIS = 0
Y_AXIS = 1

def parse_rows(rows):
	yCoords = map(lambda x : x[6], rows)
	xCoords = map(lambda x : x[5], rows)
	theCoords = zip(xCoords, yCoords)	

	return (yCoords, xCoords, theCoords)
