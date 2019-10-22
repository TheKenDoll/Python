#game is going to go threw a list of potential words that can be easily added to, should have a feture where you can add your own word and it will save it for future play threws
import random as ran
#while should be here to repeat the whole thing
words = ['bat', 'ape', 'monkey', 'hippo', 'dog', 'cat', 'apple', 'fruit', 'theme', 'tree', 'clock', \
'chemistry', 'bracket', 'computer', 'gas', 'fuel', 'pencil', 'laptop', 'outside','sheet','applebees' \
'me', 'jazz']#to add a word use the following formatting "'___wordhere____'," like seen in the words list
word = words.pop(len(words)-1)#ran.randint(0,
guesses = []#checks to see if the letter has already been guessed needs to be reset after each game tho
lives_list = []#need to work on this
lives = 5
win = False
live_numbers = 0#any value will be changed
start = True

print ('You start with 5 lives.')
for i in word:
    print (end='_ ')
print ('')
#it would be ezer if you just made a list somehow for the word hmm maybe i should think like a gui

while lives>0:
 
    word_print = []#has to be reset after each function

    def guess():
        input_guess = input('What is your guess? ')

        for guess in guesses:

            if input_guess == guess:
                print ('That letter has already been guessed')#repeats too many times should fix
                
        else:
            guesses.append(input_guess)
            #runs the blanks function
            print ('Guesses:',end=' ')
            for i in guesses:
                print (i, end=' ')
            print('')
            #blanks()
        return

    def blanks():

        for letter in word:
            if letter in guesses:
                word_print.append(letter.upper())
                
            elif letter not in guesses:
                word_print.append('_')

    def print_word():
        global word_print #don't know if i really need this
        for j in word_print:
            print (j, end=' ')
        print('')
        return

    def lives_numbers_set():#sets the first value of live_numbers should be used just once at the beginning of the word
        global start#makes this varible usable in this function
        global word_print #don't know if i really need this
        global live_numbers
        if start == True:
            live_numbers = len(word_print)
            start = False
        return #lives_number_test

    def lives_number_test(): #still having issues with lives maybe on teh counting or smthing
        global lives
        global live_numbers
        global word_print
        if live_numbers == word_print.count('_'):#!!!!!!!!!!!!!somthing is going on with the lives!!!!!!!!!!!idk the problem
            lives -= 1
        print ('Lifes: ' + str(lives))
        live_numbers = word_print.count('_')

    def win_test():
        global win
        if '_' not in word_print:
            win = True
        return 
    
    if win != False:
        break
    
    #if start == True:
    guess()
    blanks()
    print_word()
    lives_numbers_set()
    lives_number_test()
    win_test()
    
if win == True:
    print ('You win!')
else:
    print ('You lose.')

#programmed by jade FjestaD
                    
