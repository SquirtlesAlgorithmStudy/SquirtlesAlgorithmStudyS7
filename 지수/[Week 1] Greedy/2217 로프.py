N = int(input())                        # 총 로프의 개수 입력받기
ropeWeight = []

for i in range(N):
    ropeWeight.append(int(input()))     # 각 로프가 버틸 수 있는 최대 중량

ropeWeight.sort(reverse=True)           # 내림차순 정렬

num = 0                                 # 로프의 개수
output = []                             # 로프의 개수에 따른 들어올릴 수 있는 물체의 최대 중량

for w in ropeWeight:
    output.append(w * (num+1))
    num += 1

print(max(output))