word = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

for croatia in croatia_alphabet:
    count += word.count(croatia)
    word = word.replace(croatia,' ')

word = word.replace(' ','')
print(count+len(word))