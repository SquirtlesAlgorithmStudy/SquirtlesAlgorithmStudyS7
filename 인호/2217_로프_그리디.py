import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

def max_weight(N,ropes):
    ropes.sort(reverse=True)
    
    return max(ropes[i] * (i +1) for i in range(N))

N = int(input())
ropes = [int(input()) for _ in range(N)]
print(max_weight(N,ropes))