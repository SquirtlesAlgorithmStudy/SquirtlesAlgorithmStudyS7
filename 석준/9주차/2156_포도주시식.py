n=int(input())
array=[0]*10000
for i in range(n):
    array[i]=int(input())
    
d = [0]* 10000
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[2]+array[1], array[2]+array[0],d[1])
for i in range(3,n):
    d[i] = max(d[i-1], d[i-2] + array[i], d[i-3] + array[i-1] + array[i])

print(d[n - 1])