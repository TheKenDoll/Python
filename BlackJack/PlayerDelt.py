#program works!!!

cards_chosen = ['king','4','3','8','3']

hit = 0

while True:

    print ('Here are your cards: ')

    def print_list(x):#dont really know how this works but it works just to make it print nicer
        print('\n'.join(x))
    print_list(cards_chosen[0:2+hit])


    values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':10,'queen':10,'king':10} #at this point im excluding the ace too hard to work with

    cards_chosen_values = []

    for go_though_cards_chosen in cards_chosen:
        total_player_values = values[go_though_cards_chosen]
        cards_chosen_values.append(total_player_values)

    sum_of_player = (sum(cards_chosen_values[0:2+hit]))#just for test purposes

    if sum_of_player == 21:
        win_lose = 'win'#then print the outcome of the win_lose
        print ('21!!!')#just for testing 
        break
    elif sum_of_player > 21:
        win_lose = 'lose'#then prin teh outcome of the win_lose later
        print ('Busted')#just for test purposes
        break
    else:
        hit_stand = input('Will you hit or stand? ')
        hit_stand = hit_stand.lower()
        if hit_stand == 'hit':
            hit = hit + 1
            print (hit)
        else:
            print ('player stood stand')
            break#break probalbaly will need a while at the beggining 