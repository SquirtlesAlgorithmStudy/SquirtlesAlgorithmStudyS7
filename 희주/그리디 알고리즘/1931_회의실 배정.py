import sys
N = int(input())

s_e_list =[]
count =1

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    
    s_e_list.append([s, e])

s_e_list.sort(key=lambda x: [x[1], x[0]])

now =s_e_list.pop(0)
while len(s_e_list):
    
    if (s_e_list[0][0] >= now[1]):
        count +=1
        now =s_e_list[0]

    s_e_list.pop(0)

print(count)