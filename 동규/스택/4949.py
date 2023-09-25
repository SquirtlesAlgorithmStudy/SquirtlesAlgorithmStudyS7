import sys

result_list=[]

while True:
    sentences =sys.stdin.readline().strip()
    bracket_list=[]
    for sentence in sentences:
        if sentence=="(" | sentence=="[":
            bracket_list.append(sentence)
        if sentence==")":
            if bracket_list[-1]=="(":
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
        if sentence==".":
            result_list.append("yes")
        #print(bracket_list)

for result in result_list:
    print(result)