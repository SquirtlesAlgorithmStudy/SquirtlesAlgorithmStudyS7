import sys

N,M=map(int,sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().split()))



def binary_search(target, start, end):
    result=0
    while start<=end:
        num=0
        mid = (start + end) // 2
        for tree in trees:
            if mid<tree:
                num=num+(tree-mid)
            
        if num>=target:
            result=mid
            start=mid+1
        else:
            end=mid-1

    return result
result=binary_search(M,0,max(trees)-1)
print(result)

