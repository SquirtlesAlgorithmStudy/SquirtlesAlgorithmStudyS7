n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort()
print(meeting)