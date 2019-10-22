#--check-- to dos: just confirm that the card randomizer on lines 21, 25, 29, 33 check
#extra curricular make it so that the cards get chosen when needed not just a large supply hoping the demand is less

#Note could reset the deck by creating a while statement at the beggining ie. while user_has_money: or a if would work too i think
#black jack/21, take bet from player, choose cards for dealer, determain to hit or stay, choose cards for player, prompt player to hit/stay, figure out who wins,
#create list of cards, remove cards randomly, reset deck,
#lets just get it to work!!!
import random

spades = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']#can't really be simplified
clubs = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
hearts = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
dimonds = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
cards_chosen = []

def pick_four_cards():
    #trying to get random cards from a list and put them into a new list
    suit = random.randint(0,3)#randomizes the suit
    #card = random.randint(0,12)#randomizes the value oF the card !!!!!WHAT HAPPENS WHEN ITS INDEX 12 BUT THERE IS NO 12? CRASHES!!!!?~~~!
        #make a common list for every suit?
    if suit == 3:
        card = random.randint(0,len(spades)-1)
        card_and_suit = spades.pop(card) #removes the card and assigns a card
        print ('spades') #jsut to check it randomizes
    elif suit == 2:
        card = random.randint(0,len(clubs)-1)
        card_and_suit = clubs.pop(card) #removes the card and assigns a card
        print ('clubs')#jsut to check it randomizes
    elif suit == 1:
        card = random.randint(0,len(hearts)-1)
        card_and_suit = hearts.pop(card) #removes the card and assigns a card
        print ('hearts')#jsut to check it randomizes
    else:
        card = random.randint(0,len(dimonds)-1)
        card_and_suit = dimonds.pop(card) #removes the card and assigns a card
        print ('dimonds')#jsut to check it randomizes
    cards_chosen.append(card_and_suit)
    print (cards_chosen[len(cards_chosen)-1])

    #dictionaries dont have a index so make a list of lists? nope
    #SO IM GOING TO HAVE TO make a list find a number in the list with a name then retreve the value by useing a dictionary
    #(list_of_cards)
    #i think a dicionalry wud be better cuz it we can have the same values, but then we'd have to make sure we don't get the same cards.
    #i think we should random to find the suit, then random to find number, and confirm that the next cards are not previesly chosen
    #i think its better to use a dictionary
    #or should i just remove the key for the list and write something that gives those keys values ie. 'jack' = 11
    
    #just for testing purpose
while len(cards_chosen) < 10:
    pick_four_cards()

else:
    print (spades)#just to confirmed they are removed
#runs the deck list
    
