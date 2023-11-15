def clockwise(gear):
    tmp = gear[7]
    for j in range(7,0,-1):
        gear[j] = gear[j-1]
    gear[0] = tmp

def counter_clockwise(gear):
    tmp = gear[0]
    for j in range(7):
        gear[j] = gear[j+1]
    gear[7] = tmp

def right_distinguish(gear1, gear2, direction):
    old_gear = gear2
    if(direction == 1):    # clockwise
        if(gear1[2] != gear2[6]): # differ
            counter_clockwise(gear2)
            return old_gear, -1
        else:
            return old_gear, 0
    elif(direction == -1): # counter clockwise
        if(gear1[2] != gear2[6]): # differ
            clockwise(gear2)
            return old_gear, 1
        else:
            return old_gear, 0
    else:                  # stop
        return old_gear, 0
    
def left_distinguish(gear1, gear2, direction):
    old_gear = gear1
    if(direction == 1):    # clockwise
        if(gear1[2] != gear2[6]): # differ
            counter_clockwise(gear1)
            return old_gear, -1
        else:
            return old_gear, 0
    elif(direction == -1): # counter clockwise
        if(gear1[2] != gear2[6]): # differ
            clockwise(gear1)
            return old_gear, 1
        else:
            return old_gear, 0
    else:                  # stop
        return old_gear, 0
        
def score(gear1, gear2, gear3, gear4):
    score = 0
    if(gear1[0] == '1'):
        score += 1
    if(gear2[0] == '1'):
        score += 2
    if(gear3[0] == '1'):
        score += 4
    if(gear4[0] == '1'):
        score += 8
    return score

gear = []

for i in range(4):
    gear.append(list(input()))

k = int(input())

for _ in range(k):
    location, direction = map(int, input().split())
    origin_direction = direction

    if(location == 1):
        old_gear1, direction = right_distinguish(gear[0], gear[1], direction)
        old_gear2, direction = right_distinguish(old_gear1, gear[2], direction)
        right_distinguish(old_gear2, gear[3], direction)
    elif(location == 2):
        left_distinguish(gear[0], gear[1], direction)
        old_gear2, direction = right_distinguish(gear[1], gear[2], direction)
        right_distinguish(old_gear2, gear[3], direction)
    elif(location == 3):
        right_distinguish(gear[2], gear[3], direction)
        old_gear1, direction = left_distinguish(gear[1], gear[2], direction)
        left_distinguish(gear[0], old_gear1, direction)
    else:
        old_gear2, direction = left_distinguish(gear[2], gear[3], direction)
        old_gear1, direction = left_distinguish(gear[1], old_gear2, direction)
        left_distinguish(gear[0], old_gear1, direction)
    
    if(origin_direction == 1):
        clockwise(gear[location-1])
    else:
        counter_clockwise(gear[location-1])

print(score(gear[0], gear[1], gear[2], gear[3]))