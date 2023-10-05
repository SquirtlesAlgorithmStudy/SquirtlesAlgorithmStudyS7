import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline


n = int(input())

total_time = [list(map(int, input().split())) for _ in range(n)]
total_time.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 기준 정렬 후, 시작 시간 기준으로 다시 정렬

count = 1 # 하나는 무조건 선택(시작)
end_time = total_time[0][1] # 첫번째 회의 종료 시간

for i in range(1, n):
    if total_time[i][0] >= end_time: # 현재 회의 시작 시간이 이전 회의 종료 시간보다 늦으면(크면)
        count += 1 # 회의실 배정
        end_time = total_time[i][1] # 새로운 종료 시간 배정

print(count)