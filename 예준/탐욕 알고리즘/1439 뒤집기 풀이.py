s=input()

length = len(s)
num=1
for i in range(length-1):
    if(s[i]!=s[i+1]):
        num+=1

print(num//2)
