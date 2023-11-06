N = int(input())

map_list = [[float('inf')]*N for _ in range(N)]

while True :
  a, b = map(int, input().split())
  if a == b == -1 :
    break
  map_list[a-1][b-1] = map_list[b-1][a-1] = 1

for i in range(N):
  map_list[i][i] = 0


for k in range(N):
  for i in range(N):
    for j in range(N) :
      if map_list[i][j] > map_list[i][k] + map_list[k][j] :
        map_list[i][j] = map_list[i][k] + map_list[k][j]

dist_list = [ max(map_list[i]) for i in range(N) ]

chairman_val = min(dist_list)
chairman_list = list()

for i in range(N):
  if dist_list[i] == chairman_val :
    chairman_list.append(i+1)

print(chairman_val, len(chairman_list))
print(*chairman_list)