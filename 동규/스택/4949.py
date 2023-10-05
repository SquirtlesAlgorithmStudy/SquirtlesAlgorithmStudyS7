import sys

result_list=[]

while True:
    sentences =sys.stdin.readline().rstrip()
    if sentences==".":
        break
    bracket_list=["."]
    for sentence in sentences:
        if sentence=="(" or sentence=="[":
            bracket_list.append(sentence)
        if sentence==")":
            if bracket_list[-1] =="(" :
                bracket_list.pop()
                continue
            else:
                result_list.append("no")
                break
        elif sentence=="]":
            if bracket_list[-1]=="[":
                bracket_list.pop()
                continue
            else:
                result_list.append("no")
                break
        if len(bracket_list)==1 and sentence==".":
            result_list.append("yes")
            continue
        elif len(bracket_list)!=1 and sentence==".":
            result_list.append("no")
            break

for result in result_list:
    print(result)
