import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

nums = input()

segments = nums.split('-')

# 첫 번째 부분은 양수이므로 '+'로 나눈 뒤 더하기
result = sum(int(value) for value in segments[0].split('+'))

# 남은 부분은 모두 음수로 처리할 수 있으므로 '+'로 나눈 뒤 더하고 뺴기
for segment in segments[1:]:
    result -= sum(int(value) for value in segment.split('+'))

print(result)

