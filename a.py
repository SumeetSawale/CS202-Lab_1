"""Random Code from AoC problem"""

A = "ABC"
A = [list(map(int, i.split())) for i in A.splitlines()]

def is_valid(level) :
    """Checks validity of a level"""
    if level[0] == level[1] :
        return 0
    inc = (level[1] - level[0]) > 0

    for index in range(1, len(level)) :
        b = level[index] - level[index-1]
        if (b > 0) != inc :
            return 0
        if abs(b) > 3 :
            return 0
        if abs(b) < 1 :
            return 0

    return 1

def is_valid_2(level) :
    """Checks validity of a level"""
    if is_valid(level) :
        return 1
    for index in range(len(level)) :
        new_level = level[:index] + level[index+1:]
        if is_valid(new_level) :
            return 1
    return 0

S = 0
for i in A :
    S += is_valid_2(i)
print(S)
