import sys
import copy

croatia_list=["c=","c-","d-",
              "lj","nj","s=","z="]

alphbets = sys.stdin.readline()

alphbets_copy=copy.deepcopy(alphbets)
count=0

for alphbet in range(len(alphbets)-2):
    if alphbets[alphbet:alphbet+2] in croatia_list:
        if alphbets[-1+alphbet:alphbet+2]=="dz=":
            alphbets_copy=alphbets_copy.replace("dz=","",1)
            count+=1
            continue
        alphbets_copy=alphbets_copy.replace(alphbets[alphbet:alphbet+2],"",1)
        count+=1

print(len(alphbets_copy.strip())+count)