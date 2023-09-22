arr = input()
zero_count = 0 # 0 뭉텅이 개수
one_count = 0 # 1 뭉텅이 개수

#첫번쨰 문자 확인하기
if arr[0] == "0" :
    zero_count += 1
else:
    one_count += 1

flag = arr[0]

#두번쨰 문자부터 끝까지 하나씩 확인
for i in range(1,len(arr)):

 if flag != arr[i]:# 앞에 문자랑 다른게 나왔을 경우
    if arr[i] == "0": # 0이 새롭게 나오면 zero_count 증가
         zero_count += 1
         flag = "0"
    else : # 1이 새롭게 나오면 one_count 증가
        one_count += 1
        flag = "1"
                


print(zero_count) if zero_count<one_count else print(one_count)

# 메모리: 31388 KB, 시간: 40 ms