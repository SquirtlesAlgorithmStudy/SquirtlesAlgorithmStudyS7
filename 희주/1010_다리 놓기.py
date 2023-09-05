import sys
def factorial(N):
    if N ==1:
        return 1
    elif N ==2:
        return 2
    else:
        return N * factorial(N-1)

N = int(input())

for i in range(N):
    n, m = list(map(int, sys.stdin.readline().split()))
    
    if n == m:
        print(1)
    else:
        n, m =max(n, m), min(n, m)
        print(round(factorial(n)/(factorial(m)* factorial(n-m))))