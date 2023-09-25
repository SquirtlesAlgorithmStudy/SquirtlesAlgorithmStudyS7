S = input().split('-')

# 가장 작은 수를 만들어야됨
# 마이너스 뒤에 오는거는 다 더하면 된다?

# 100 - 10 + 20 - 30 + 40

# 식을 마이너스로 일단 쪼개고 그 안에서 더하기가 있다면 다 더해주면 됨

ans = 0
for i in S[0].split('+'):
    ans += int(i)

for i in S[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)