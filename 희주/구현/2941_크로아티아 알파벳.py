import sys

alph = sys.stdin.readline().strip()
# print(alph)

ALPH = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
i = 0
L = len(alph)
while i < L:
    # print(i)
    if i+1 < L:
        if alph[i] == 'c':
            if alph[i+1] == '=' or alph[i+1] == '-':
                # print(alph[i+1])
                i += 2
            else:
                i += 1
        elif alph[i] == 'd':
            if alph[i+1] == '-':
                i += 2
            elif i+2 < L:
                if alph[i+1] == 'z' and alph[i+2] == '=':
                    i += 3
                else:
                    i += 1
        elif alph[i] == 'l':
            if alph[i+1] == 'j':
                i += 2
            else:
                i += 1
        elif alph[i] == 'n':
            if alph[i+1] == 'j':
                i += 2
            else:
                i += 1
        elif alph[i] == 's':
            if alph[i+1] == '=':
                i += 2
            else:
                i += 1
        elif alph[i] == 'z':
            if alph[i+1] == '=':
                i += 2
            else:
                i += 1
        else:
            i += 1
        answer += 1
    else:
        answer += 1
        break
        
print(answer)