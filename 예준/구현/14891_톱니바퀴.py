gear = [list(map(int, input())) for _ in range(4)]
num = int(input())
arr = [[0 for j in range(2)] for i in range(num)]

for k in range(num):
    arr[k][0], arr[k][1] = map(int, input().split())

import copy

def gear_move(lst, n):
    if(n == 1):
        a = copy.deepcopy(lst)
        a_7 = a[7]
        del a[7]
        a.insert(0, a_7)
        return(a)
    elif (n == -1):
        a = copy.deepcopy(lst)
        a_0 = a[0]
        del a[0]
        a.insert(7, a_0)
        return(a)
    else:
        return lst

def move(gear_num, direction):
    difference=[]
    for i in range(3):
        if gear[i][2] == gear[i+1][6]:
            difference.append(0)
        else:
            difference.append(1)
    k = [1,1,1,1]
    k[gear_num-1] = direction
    
    if gear_num == 1:
        k[1] = difference[0]*k[0]*(-1)*abs(k[0])
        k[2] = difference[1]*k[1]*(-1)*abs(k[1])            
        k[3] = difference[2]*k[2]*(-1)*abs(k[2])
    elif gear_num ==2:
        k[0] = difference[0]*k[1]*(-1)*abs(k[1])
        k[2] = difference[1]*k[1]*(-1)*abs(k[1])    
        k[3] = difference[2]*k[2]*(-1)*abs(k[2])
    elif gear_num ==3:
        k[3] = difference[2]*k[2]*(-1)*abs(k[2])
        k[1] = difference[1]*k[2]*(-1)*abs(k[2])
        k[0] = difference[0]*k[1]*(-1)*abs(k[1])
    elif gear_num ==4:
        k[2] = difference[2]*k[3]*(-1)*abs(k[3])
        k[1] = difference[1]*k[2]*(-1)*abs(k[2])
        k[0] = difference[0]*k[1]*(-1)*abs(k[1])
    
    for i in range(4):
        gear[i]=gear_move(gear[i],k[i])
        
def score():
    sum = 0
    for i in range(4):
        sum += gear[i][0] * (2**i)
    return sum

for i in range(num):
    move(arr[i][0],arr[i][1])

print(str(score()))