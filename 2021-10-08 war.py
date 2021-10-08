import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cardp_1 = []
cardp_2 = []
orderOfWonCards = []
rounds = 0
cardsForTheWinner = []
cardsForTheWinner1 = []
cardsForTheWinner2 = []
cardOrder = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "10":9, "J":11, "Q":12, "K":13, "A":14}
pat = 0

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2.append(input())  # the m cards of player 2

def card_value(card):
    if card[0] != "1":
        return cardOrder[card[0]]
    else:
        return cardOrder[card[:2]]

def wars(recur):
    global cardp_1, cardp_2, pat
    if len(cardp_1) < 4 or len(cardp_2) < 4:
        print("PAT")
        pat = 1
    else:
        card1 = cardp_1[recur]
        card2 = cardp_2[recur]
        for i in range(recur + 1):
            cardsForTheWinner1.append(cardp_1.pop(0))
        for i in range(recur + 1):
            cardsForTheWinner2.append(cardp_2.pop(0))
        if card_value(card1) == card_value(card2):
            wars(3)
        elif card_value(card1) > card_value(card2):
            cardsForTheWinner = cardsForTheWinner1
            cardsForTheWinner.extend(cardsForTheWinner2)
            cardp_1.extend(cardsForTheWinner)
        else:
            cardsForTheWinner = cardsForTheWinner1
            cardsForTheWinner.extend(cardsForTheWinner2)
            cardp_2.extend(cardsForTheWinner)

while(len(cardp_1) > 0 and len(cardp_2) > 0 and pat != 1):
    if card_value(cardp_1[0]) == card_value(cardp_2[0]):
        wars(4)
        cardsForTheWinner.clear()
        cardsForTheWinner1.clear()
        cardsForTheWinner2.clear()
    elif card_value(cardp_1[0]) > card_value(cardp_2[0]):
        cardp_1.extend([cardp_1.pop(0)])
        cardp_1.extend([cardp_2.pop(0)])
    else:
        cardp_2.extend([cardp_1.pop(0)])
        cardp_2.extend([cardp_2.pop(0)])
    
    rounds += 1

if pat != 1:
    winner = "2 " if len(cardp_1) == 0 else "1 "
    print(winner + str(rounds))
