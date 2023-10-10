alphabet = input()

croatia_alphabet_1= ['c=','c-','d-','lj','nj','s=','z=']
croatia_alphabet_2 = ['dz=']
count = 0

while len(alphabet) != 0:
    if alphabet[:2] in croatia_alphabet_1:
        count += 1
        alphabet = alphabet[2:]
    elif alphabet[:3] in croatia_alphabet_2:
        count += 1
        alphabet = alphabet[3:]
    else:
        count += 1
        alphabet = alphabet[1:]
print(count)
