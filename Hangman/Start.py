#app will make small visual maybe thats a hard part ill do at the end
import random
print ('The Game Has begun')
words = ['monkeys', 'bear', 'fox', 'lizard']
word = words[random.randint(0,3)]#replace 3 with a len(words) or smthing
#print ('_ '*len(word))#probs remove
letters = []
thing = []
for i in word:
    thing.append('_ ')#could probs make it easier somehow
blanks = thing[0:len(word)]#takes a portion blanks
guesses = []
for letter in word:#needs to be outside of the loop
    letters.append(letter)

guess = input('Guess a letter of the word ')#loops
for x in blanks:#loops
    print (x, end=' ')
for i in word:#loops
    if guess == i:
        print ('filler')
        #replace blanks index with letters
print (thing)