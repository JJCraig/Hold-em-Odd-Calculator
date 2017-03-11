import random

def populateDeck():
    deckOfCards = [0] * 52
    for x in range(0, 52):
        deckOfCards[x] = x
    return deckOfCards

deckOfCards = populateDeck()
print(deckOfCards)
random.shuffle(deckOfCards)
print(deckOfCards)
    
    