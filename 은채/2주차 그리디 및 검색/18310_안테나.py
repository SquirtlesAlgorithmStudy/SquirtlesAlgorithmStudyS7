N = input()
homes = sorted(list(map(int, input().split())))

if len(homes) % 2 == 0:
    answer = homes[(len(homes) // 2) - 1]
else:
    answer = homes[(len(homes) // 2)]

print(answer)
