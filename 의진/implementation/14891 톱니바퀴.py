import sys
input = sys.stdin.readline

gear_states = [0] + [input().rstrip() for _ in range(4)]
K = int(input())
commands = [tuple(map(int, input().split())) for _ in range(K)]


def rotate_gear(gear_state, direction):
    if direction == 1:
        new_gear_state = gear_state[-1] + gear_state[:-1]
    else:
        new_gear_state = gear_state[1:] + gear_state[0]
    return new_gear_state


for command in commands:
    planner = [command]
    gear_num = command[0]
    direction = command[1]
    if gear_num == 1:
        for i in range(1, 4):
            if gear_states[i][2] == gear_states[i+1][6]:
                break
            direction = -direction
            planner.append((i+1, direction))
    elif gear_num == 4:
        for i in range(4, 1, -1):
            if gear_states[i][6] == gear_states[i-1][2]:
                break
            direction = -direction
            planner.append((i-1, direction))
    elif gear_num == 2:
        if gear_states[1][2] != gear_states[2][6]:
            planner.append((1, -direction))
        for i in range(2, 4):
            if gear_states[i][2] == gear_states[i+1][6]:
                break
            direction = -direction
            planner.append((i+1, direction))
    elif gear_num == 3:
        if gear_states[3][2] != gear_states[4][6]:
            planner.append((4, -direction))
        for i in range(3, 1, -1):
            if gear_states[i][6] == gear_states[i-1][2]:
                break
            direction = -direction
            planner.append((i-1, direction))

    for plan in planner:
        gear_states[plan[0]] = rotate_gear(gear_states[plan[0]], plan[1])

score = 0
for i, gear_state in enumerate(gear_states[1:]):
    score += (2 ** i) * int(gear_state[0])
print(score)
