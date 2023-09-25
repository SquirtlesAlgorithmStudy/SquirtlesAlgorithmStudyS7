number_of_meetings = int(input())
meetings_list = list()

for _ in range(number_of_meetings):
    meeting = list(map(int, input().split()))
    meetings_list.append(meeting)
    
# 람다 함수를 사용하여 오른쪽 원소를 기준으로 정렬
sorted_meetings = sorted(meetings_list, key=lambda x: (x[1], x[0]))

count = 0
count += 1
meeting_end = sorted_meetings[0][1]
for i in range(1, len(sorted_meetings)):
    if sorted_meetings[i][0] >= meeting_end:
        count += 1
        meeting_end = sorted_meetings[i][1]
print(count)
