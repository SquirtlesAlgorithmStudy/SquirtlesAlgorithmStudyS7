import sys 
from collections import deque

wheel = [[0]*8 for _ in range(4)] # 톱니바퀴 4개 리스트 
result = 0 # 결과값

for i in range(4):
    number = sys.stdin.readline().rstrip()
    wheel[i] =deque([ int(n) for n in number]) # 각각 deque 에 저장

K = int(sys.stdin.readline().rstrip()) # 회전 횟수

for _ in range(K):
    n, d = sys.stdin.readline().rstrip().split(' ')
    n, d = int(n), int(d)
    
    before_d = d # 이전에 톱니바퀴의 회전 방향 
    
    if n == 1: # n이 첫 번째 톱니바퀴일 경우
        check =wheel[n-1][2] # 첫 번째 톱니바퀴의 오른쪽 두번째 바퀴
    
        for i in range(1, 4): # 두 번째 톱니바퀴부터 마지막 톱니바퀴까지
            if wheel[i][-2] != check: # 서로 같은 극을 가지는 지 
                check = wheel[i][2] # 우선 현재 상태 저장 (중요)
                if before_d == 1: # 바로 앞의 바퀴의 회전방향과 반대로 움직임
                    tmp = wheel[i].popleft()
                    wheel[i].append(tmp)
                elif before_d == -1:
                    tmp = wheel[i].pop()
                    wheel[i].appendleft(tmp)
                
                before_d *= (-1) # 회전 방향을 반대로 바꾸면서 다음 바퀴로 진행
            else: # 같은 극이면 이후의 바퀴들 모두 변경사항 없음 
                break

    elif n == 4: # n이 마지막 톱니바퀴일 경우
        check = wheel[n-1][-2] # 마지막 톱니바퀴의 왼쪽 두번째 바퀴
        
        for i in range(2, -1, -1): # 세 번째 톱니바퀴부터 첫 번째 톱니바퀴까지 
            if wheel[i][2] != check: 
                check = wheel[i][-2] 
                if before_d == 1:
                    tmp = wheel[i].popleft()
                    wheel[i].append(tmp)
                elif before_d == -1:
                    tmp = wheel[i].pop()
                    wheel[i].appendleft(tmp)
                
                before_d *= (-1) 
            else:
                break
    else:
        if n == 2: # n이 두 번쨰 톱니바퀴일 경우
            check = wheel[n-1][-2] # 첫 번째 톱니바퀴를 먼저 확인할 것이므로 두 번째 톱니바퀴의 왼쪽 두번째
            # 첫번째 톱니바퀴 먼저 바꾸기 
            if wheel[n-2][2] != check:
                if before_d == 1:
                    tmp = wheel[n-2].popleft()
                    wheel[n-2].append(tmp)
                elif before_d == -1:
                    tmp = wheel[n-2].pop()
                    wheel[n-2].appendleft(tmp)
                    
            check = wheel[n-1][2] # 이제 두 번째 톱니바퀴의 오른쪽 두번째를 확인해야 함
         
            # 3번째 톱니바퀴 부터 마지막 톱니바퀴까지 바꾸기
            for i in range(n,4):
                if wheel[i][-2] != check:
                    check = wheel[i][2] 
                    if before_d == 1:
                        tmp = wheel[i].popleft()
                        wheel[i].append(tmp)
                    elif before_d == -1:
                        tmp = wheel[i].pop()
                        wheel[i].appendleft(tmp)

                    before_d *= (-1)
                else:
                    break

        elif n == 3: # n이 세 번쨰 톱니바퀴일 경우
            check = wheel[n-1][2] # 마지막 톱니바퀴를 먼저 확인할 것이므로 세 번째 톱니바퀴의 오른쪽 두번째
            # 4번째 부터 바꾸기 
            if wheel[n][-2] != check:
                if before_d == 1:
                    tmp = wheel[n].popleft()
                    wheel[n].append(tmp)
                elif before_d == -1:
                    tmp = wheel[n].pop()
                    wheel[n].appendleft(tmp)
                    
            check = wheel[n-1][-2] # 이제 세 번째 톱니바퀴의 왼쪽 두번째를 확인해야 함
 
            # 두번째 톱니바퀴부터 첫번째 톱니바퀴까지 역순으로 바꾸기
            for i in range(1, -1, -1): 
                if wheel[i][2] != check:
                    check = wheel[i][-2] 
                    if before_d == 1:
                        tmp = wheel[i].popleft()
                        wheel[i].append(tmp)
                    elif before_d == -1:
                        tmp = wheel[i].pop()
                        wheel[i].appendleft(tmp)
         
                    before_d *= (-1)
                else:
                    break
    # 현재 톱니바퀴 값을 마지막으로 변경한다    
    if d == -1:
        tmp = wheel[n-1].popleft()
        wheel[n-1].append(tmp)
    elif d == 1:
        tmp = wheel[n-1].pop()
        wheel[n-1].appendleft(tmp)
# 결과값 계산
for i in range(4):
    score = 1
    if wheel[i][0] == 1:
        result += score *2**i

print(result)

## 실행시간: 64ms