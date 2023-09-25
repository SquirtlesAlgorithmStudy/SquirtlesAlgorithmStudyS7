number_of_houses = input()
houses_list = list(map(int,input().split(' ')))

houses_list.sort()
# 홀수인 경우
if len(houses_list)%2 == 1:
    print(houses_list[len(houses_list)//2])
else:
    print(houses_list[len(houses_list)//2 -1])