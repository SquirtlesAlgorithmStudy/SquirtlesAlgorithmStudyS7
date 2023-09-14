import sys
input = sys.stdin.readline

S = input().rstrip()
current_value = S[0]
count = 0

for char in S:
    if char != current_value:
        count += 1
        current_value = char

print((count + 1) // 2)
