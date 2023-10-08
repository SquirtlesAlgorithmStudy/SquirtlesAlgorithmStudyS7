import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

# 100x100 도화지 초기화
empty_matrix = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())  # 색종이 수 입력
recs = [list(map(int, input().split())) for _ in range(N)]  # 색종이 위치 입력

for rec in recs:
    x, y = rec  # 왼쪽 변과 아래쪽 변의 거리
    for i in range(x, x + 10):  # 가로 범위
        for j in range(y, y + 10):  # 세로 범위
            empty_matrix[j][i] = 1  # 해당 영역을 1로 표시

# 색칠한 영역의 넓이 계산
area = sum(row.count(1) for row in empty_matrix)
print(area)  # 결과 출력