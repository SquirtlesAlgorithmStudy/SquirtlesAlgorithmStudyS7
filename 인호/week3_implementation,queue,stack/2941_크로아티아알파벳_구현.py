import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input().strip()  

#대체 문자로 변경
for alphabet in alphabets:
    word = word.replace(alphabet, '0')  

print(len(word))