A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
count=1
num=B[0]
for i in range(A[0]):

    if num+A[1]-1>=B[i]:
        continue
    else:
        num=B[i]
        count+=1

print(count)
        
