#be able to give a user a initial amout of chips, ask for wager, 
print ('Hey there player, I\'ve started you off with 500$. Try and get as high as you can.)
money = 500
bet = input('What\'s your wager? ')
if bet <= money:
    #run blackjack game
else:
    print ('I\'m sorry but I can\'t accept that value as a bet.)


#at the end of the game
if game_outcome == win:
    print ('Congrats you beat the dealer.')
    money += money + (bet * 2)
    print ('you currently have $%s' % money)

else:
    print ('The dealer won')
    money -= money + (bet * 2)

    


