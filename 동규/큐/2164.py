import sys

cards = int(sys.stdin.readline())
card_list=[]

for card in range(1,cards+1):
    card_list.append(card)

while True:
    if len(card_list)==1:
        break
    card_list.pop(0)
    card_list.append(card_list.pop(0))

print(card_list[0])