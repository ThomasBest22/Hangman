#Cette fois-ci c'est un pendu (en anglais rip les non-bilingues)

#les imports
import time
import random
#voilà

#les variables
words_to_find = open("words.txt").read().splitlines()
word_to_find = random.choice(words_to_find)
# word_to_find = 
#fin des variables

#explication
print ("Hi, you are playing a Hangman game .\nThe word to be guessed is randomly selected in the English dictionnary.\nYou can guess 7 times wrong the word before losing.\nGood luck!")
time.sleep(1)
#début du code
banana_word = list(word_to_find)
longueur_du_mot = len(word_to_find)
guessing=longueur_du_mot * "_"
listedudevinnage = list(guessing)
banana_word_copy = banana_word.copy()
guesses=7
while banana_word_copy != listedudevinnage:
    lettre = input("Submit a letter\n")
    nbrdefoislalettre = banana_word_copy.count(lettre)
    nbrdefoislalettrepourleif = nbrdefoislalettre
    for letter in banana_word:
        if letter == lettre:
            while nbrdefoislalettre != 0:
                nbrdefoislalettre = nbrdefoislalettre - 1
                lindex = banana_word.index(letter)
                banana_word.pop(lindex)
                banana_word.insert(lindex,"_")
                listedudevinnage.pop(lindex)
                listedudevinnage.insert(lindex, letter)
        if nbrdefoislalettrepourleif == 0:
            guesses=guesses-1
            if guesses == 0:
                print("Sorry. You lost! The word was " + word_to_find + ".")
                exit()
            if guesses == 1:
                print("No, sorry. The letter " + lettre + " isn't in the word.\nYou get " + str(guesses) + " guess before getting hanged")
                break
            else:
                print("No, sorry. The letter " + lettre + " isn't in the word.\nYou get " + str(guesses) + " guesses before getting hanged")
                break
    print (" ".join(listedudevinnage) + "\n")       
else:
    time.sleep(1)
    print("Well done ! You guessed the world which was " + word_to_find)
