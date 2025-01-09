a = [list(map(int, i.split())) for i in a.splitlines()]

def isValid(level) :
	if level[0] == level[1] :
		return 0
	
	inc = ((level[1] - level[0]) > 0)

	for i in range(1, len(level)) :
		a = level[i] - level[i-1]
		if ((a > 0) != inc) :
			return 0
		if abs(a) > 3 :
			return 0
		if abs(a) < 1 :
			return 0
		
	return 1

def isValid2(level) :
	if isValid(level) :
		return 1
	for i in range(len(level)) :
		newLevel = level[:i] + level[i+1:]
		if isValid(newLevel) :
			return 1
	return 0

s = 0
for i in a :
	s += isValid2(i)
print(s)