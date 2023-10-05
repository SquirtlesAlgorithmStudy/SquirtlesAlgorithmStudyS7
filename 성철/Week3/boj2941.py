string = input()
ans = 0

for index,char in enumerate(string):
    # 두번째 문자 부터는 조건을 체크해줌
    if index > 0:
        if char == '=':
            if index > 1:
                # dz=를 한글자 취급하기 위해 d에서 올렸던 카운트를 빼줌
                if string[index-1] == 'z' and string[index-2] == 'd':
                    ans -= 1
            # 나머지 (c=, s=, z=)의 경우 =의 카운트를 세지 않음
        # c-, d- 두 가지 경우 모두 -를 세지 않으면 됨
        elif char == '-':
            pass
        
        elif char == 'j':
            #  lj, nj의 경우 j를 세지 않음
            if string[index-1] == 'l' or string[index-1] == 'n':
                pass
            # 나머지의 경우 j를 세줌
            else:
                ans += 1
        # j, =, -가 아닌 경우 무조건 카운트를 세줌
        else: ans += 1
    # 첫 문자
    else: ans += 1

print(ans)
