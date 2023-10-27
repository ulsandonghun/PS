import sys

N = int(sys.stdin.readline())

deck=[i  for i in range(1,N+1)]
#1에서 N 까지 리스트에 저장


while(len(deck)>1):
    deck.pop(0);
    # deck.insert(len(deck)-1,deck.pop())
    deck.append(deck.pop(0))
print(deck.pop())

