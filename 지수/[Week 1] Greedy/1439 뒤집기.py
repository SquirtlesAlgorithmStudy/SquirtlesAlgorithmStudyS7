s = input()

cnt = 0
flag = s[0]

for i in range(len(s)):
    if flag != s[i]:
        cnt += 1
        flag = s[i]

print(int(cnt/2 + cnt%2))