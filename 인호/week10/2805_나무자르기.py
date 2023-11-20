import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import Counter
n, m = map(int, input().split())
trees = Counter(map(int, input().split()))
start = 0
end = max(trees)
answer = 0


while start <= end:
    h = (start + end)//2
    volume = 0
    for i, cnt in trees.items():
        if i>=h:
            volume += (i-h)*cnt
    if volume < m:
        end = h-1
    else:
        start = h+1
        answer = h

print(answer)