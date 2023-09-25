# S = list(input())

# convert_to_1=0
# convert_to_0=0

# for i in range(1,len(S)):
#     if S[i]!=S[i-1]:
#         if S[i-1]=='0':
#             convert_to_1+=1
#         else:
#             convert_to_0+=1
# if S[-1]=='0':
#     convert_to_1+=1
# else:
#     convert_to_0+=1
# print(min(convert_to_0,convert_to_1))

import sys

s = sys.stdin.readline().strip()
one = [s for s in s.split('1') if s]
zero = [s for s in s.split('0') if s]

print(min(len(one), len(zero)))