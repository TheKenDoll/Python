#going to finish the dealer's hand
#figure out how to print the list/cards not backwards
#need to add this to the final combined part
cards_chosen = ['king','4','2','7','3']
dealer_hit = 0
win_lose = 'lose'
cards_chosen_values = []
sum_of_player = 20
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':10,'queen':10,'king':10} #at this point im excluding the ace too hard to work with
for go_though_cards_chosen in cards_chosen:
        total_player_values = values[go_though_cards_chosen]
        cards_chosen_values.append(total_player_values)


#this part should be printed before the player hits or stands
print ('The dealer has a face up card: %s, and one faced down' % cards_chosen[len(cards_chosen)-1])#pick the last term in the list

while win_lose != 'win':

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
        