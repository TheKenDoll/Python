#not using aces yet
#add some sleeps throughout to make it easier to read'n'stuff

import random

chips = 500

print ('You start with 500 chips')

#put the whole thing in a while statement thats as long as they have more money then 0
spades = ['2','3','4','5','6','7','8','9','10','jack','queen','king']#can't really be simplified
clubs = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
hearts = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
dimonds = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
cards_chosen = []

def pick_four_cards():
    #trying to get random cards from a list and put them into a new list
    suit = random.randint(0,3)#randomizes the suit
    #card = random.randint(0,12)#randomizes the value oF the card !!!!!WHAT HAPPENS WHEN ITS INDEX 12 BUT THERE IS NO 12? CRASHES!!!!?~~~!
        #make a common list for every suit?
    if suit == 3:
        card = random.randint(0,len(spades)-1)
        card_and_suit = spades.pop(card) #removes the card and assigns a card
    elif suit == 2:
        card = random.randint(0,len(clubs)-1)
        card_and_suit = clubs.pop(card) #removes the card and assigns a card
    elif suit == 1:
        card = random.randint(0,len(hearts)-1)
        card_and_suit = hearts.pop(card) #removes the card and assigns a card
    else:
        card = random.randint(0,len(dimonds)-1)
        card_and_suit = dimonds.pop(card) #removes the card and assigns a card
    cards_chosen.append(card_and_suit)

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

hit = 0
dealer_hit = 0
cards_chosen_values = []
sum_of_player = 0

print ('The dealer has a face up card: %s, and one faced down' % cards_chosen[len(cards_chosen)-1])#pick the last term in the list

values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':10,'queen':10,'king':10} #at this point im excluding the ace too hard to work with

while True:

    print ('Here are your cards: ')

    def print_list(x):#dont really know how this works but it works just to make it print nicer
        print('\n'.join(x))
    print_list(cards_chosen[0:2+hit])

    for go_though_cards_chosen in cards_chosen:
        total_player_values = values[go_though_cards_chosen]
        cards_chosen_values.append(total_player_values)

    sum_of_player = (sum(cards_chosen_values[0:2+hit]))#just for test purposes

    if sum_of_player == 21:
        win_lose = 'win'#then print the outcome of the win_lose
        print ('21!!!')#just for testing
        stand = False
        break
    elif sum_of_player > 21:
        win_lose = 'lose'#then prin teh outcome of the win_lose later
        print ('Busted')#just for test purposes
        stand = False
        break
    else:
        hit_stand = input('Will you hit or stand? ')
        hit_stand = hit_stand.lower()
        if hit_stand == 'hit':
            hit = hit + 1
        else:
            stand = True
            print ('player stood with a: %s' % sum_of_player)
            break#break probalbaly will need a while at the beggining 

#dealerdelt
while stand == True:

    def print_list(x):#dont really know how this works but it works just to make it print nicer
        print('\n'.join(x))
    print_list(cards_chosen[len(cards_chosen)-2-dealer_hit:len(cards_chosen)])

    sum_of_dealers_cards = (sum(cards_chosen_values[len(cards_chosen_values)-2-dealer_hit:len(cards_chosen_values)]))#takes the valuse from the end of the list
    print ('For a total of: %s' % sum_of_dealers_cards)#testing purposes
    if sum_of_player >= sum_of_dealers_cards:
        print ('Dealer must hit')
        dealer_hit = dealer_hit + 1
    elif sum_of_dealers_cards > 21:
        print('Dealer bust')
        win_lose = 'win'
        break
    else:
        print ('Dealer wins')
        win_lose = 'lose'
        break


        
