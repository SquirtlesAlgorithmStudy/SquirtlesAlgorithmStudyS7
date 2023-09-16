import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

def counting_flip(S):
    changes = sum(1 for i in range(1, len(S)) if S[i] != S[i-1])
    
    return (changes +1) // 2 if changes else 0

S = input()
print(counting_flip(S))