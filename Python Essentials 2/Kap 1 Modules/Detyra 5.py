#ush1

from random import randint
Shortest = 7
Longest = 10
Min_ASCII = 33
Max_ASCII = 126

def random_pass():
    length = randint(Shortest,Longest+1)
    result = ""
    for i in range(length +1):
        randomChar = chr(randint (Min_ASCII,Max_ASCII+1))
        result = result + randomChar
	    
    return result
	
def main():
	print(random_pass())
if __name__ == "__main__":
    main()

#*******************************************
#ush 2

from random import randrange

Min_num = 1
Max_num = 49
Num_nums = 6

Ticket_nums = []

while len(Ticket_nums) < Num_nums:
    rand = randrange(Min_num, Max_num + 1)  
    if rand not in Ticket_nums:
        Ticket_nums.append(rand)

print(sorted(Ticket_nums))

#***********************************************************
#ush 3 

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