import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

def counting_tape(N,L,leaks):
    leaks.sort()
    tape = 0
    i = 0

    while i < N:
        limit = leaks[i] + L - 1 # 좌우 간격 0.5 * 2

        while i < N and leaks[i] <= limit:
            i += 1
        tape += 1
    return tape


N, L = map(int, input().split())
leaks = list(map(int, input().split()))

print(counting_tape(N,L,leaks))