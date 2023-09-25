arr =  input()
arr=[i for i in arr]
count_dict={"0":0,"1":0}
prev_i=arr[0]
count_dict[prev_i]+=1
for i in arr[1:]:
    if prev_i==i:
        continue
    elif prev_i!=i:
        count_dict[i]+=1
        prev_i=i
print(min(count_dict.values()))
    
