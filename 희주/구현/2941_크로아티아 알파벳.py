import sys

alph = sys.stdin.readline().strip()

# ALPH = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
i = 0
L = len(alph)

while i < L:
    if i+1 < L: # 다음 알파벳이 있는지 확인
        if alph[i] == 'c': # c=, c-
            if alph[i+1] == '=' or alph[i+1] == '-':
                i += 2
            else: # 해당 안되는 경우는 한 글자
                i += 1
        elif alph[i] == 'd': # d-, dz=
            if alph[i+1] == '-':
                i += 2
            elif i+2 < L: # 다음 알파벳이 있는지 확인
                if alph[i+1] == 'z' and alph[i+2] == '=':
                    i += 3
                else:
                    i += 1
            else: 
                i += 1
        elif alph[i] == 'l': # lj
            if alph[i+1] == 'j':
                i += 2
            else:
                i += 1
        elif alph[i] == 'n': # nj
            if alph[i+1] == 'j':
                i += 2
            else:
                i += 1
        elif alph[i] == 's': # s=
            if alph[i+1] == '=':
                i += 2
            else:
                i += 1
        elif alph[i] == 'z': # z=
            if alph[i+1] == '=':
                i += 2
            else:
                i += 1
        else:
            i += 1
        answer += 1 
        
    else: # 다음 알파벳이 없다면 (끝)
        answer += 1
        break
        
print(answer)

## 다른 풀이 / 속도 똑같이 40ms
# word = input()
# croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# count = 0

# for croatia in croatia_alphabet:
#     count += word.count(croatia)
#     word = word.replace(croatia,' ')

# word = word.replace(' ','')
# print(count+len(word))