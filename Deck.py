import random

def populateDeck():
    deckOfCards = [0] * 52
    for x in range(0, 52):
        deckOfCards[x] = x
    return deckOfCards

def printCard(cardNumber):
    if cardNumber < 0 or cardNumber > 51:
        print('card number our of bounds')
        return
        
    #get suit
    suitTemp = cardNumber/13
    if suitTemp == 0:
        cardSuit = 'Diamonds'
    elif suitTemp == 1:
        cardSuit = 'Hearts'
    elif suitTemp == 2:
        cardSuit = 'Spades'
    elif suitTemp == 3:
        cardSuit = 'Clubs'
    
    #get card number
    numberTemp = cardNumber%13
    choices = {0:'Ace', 1:'Two', 2:'Three', 3:'Four', 4:'Five', 5:'Six', 
               6:'Seven', 7:'Eight', 8:'Nine', 9:'Ten', 10:'Jack', 11:'Queen', 12:'King'}
    result = choices.get(numberTemp)
    print(result + ' of ' + cardSuit)
    return

deckOfCards = populateDeck()
print(deckOfCards)

random.shuffle(deckOfCards)
print(deckOfCards)

printCard(6)

    
    #get card Number


    