from random import randrange

def createDeck():
    cards=[]
    suit = ["s","h","d","c"]
    value = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	
    for i in  suit[:]:
        for j in value[:]:
            val = i+j
            cards.append(val)
    return cards

createDeck()

def shuffle (cards):
	
    for i in range ( 0 , len(cards) ):
        cards[i] = cards[randrange(0,52)]
    return cards
		
def main():
    cards = createDeck()
    print("deck of cards")
    print(cards) 

    shuffleCards = shuffle(cards)
    print("shuffle cards")
    print(shuffleCards)

if __name__ == "__main__":
    main()