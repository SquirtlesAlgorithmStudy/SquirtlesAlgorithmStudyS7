import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline


N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 상태 초기화
dice = [0] * 7

# 주사위를 굴리는 함수
def roll_dice(dice, direction):
    
    # 상단(1), 북쪽(2), 동쪽(3), 서쪽(4), 남쪽(5), 하단(6)
    if direction == 1: 
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif direction == 2: 
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif direction == 3: 
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif direction == 4: 
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]


for command in commands:
    if command == 1 and y + 1 < M:  # 동쪽
        y += 1
    elif command == 2 and y - 1 >= 0:  # 서쪽
        y -= 1
    elif command == 3 and x - 1 >= 0:  # 북쪽
        x -= 1
    elif command == 4 and x + 1 < N:  # 남쪽
        x += 1
    else:
        continue  
    
    # 주사위 굴리기
    dice = roll_dice(dice, command)

    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    
    print(dice[1]) # 주사위의 윗면
