line = list(input())

# 1의 덩어리 갯수와 0의 덩어리 갯수 중 더 작은 값이 정답이다
cur_char = line[0] # 첫번째 덩어리가 0인지 1인지

# 0의 덩어리 갯수와 1의 덩어리 갯수를 저장할 리스트
cluster = [0,0]

# 첫번째 덩어리
cluster[int(cur_char)] += 1

for i in range(1,len(line)):
    # 현재 문자와 이전 문자가 다르다면 교체해주고 해당하는 덩어리 갯수를 늘려줌
    if cur_char != line[i]:
        cur_char = line[i]
        cluster[int(cur_char)] += 1

# 더 작은 값이 정답
print(min(cluster))