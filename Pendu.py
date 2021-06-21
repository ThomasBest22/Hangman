#Cette fois-ci c'est un pendu (en français)

#les imports
import time
import random
import sys
#voilà

#les variables
words_to_find = open("mots.txt").read().splitlines()
word_to_find = random.choice(words_to_find).lower()
# word_to_find = 
#fin des variables

#explication
print ("Bonjour, on va faire un pendu .\nLe mot à trouver est sélectionné dans le dictionnaire des mots français et contient des prénoms courants\nTu peux deviner 7 lettres qui ne sont pas dans le mot avant de perdre.\nBonne chance !")
time.sleep(1)
#début du code
banana_word = list(word_to_find)
longueur_du_mot = len(word_to_find)
guessing=longueur_du_mot * "_"
listedudevinnage = list(guessing)
banana_word_copy = banana_word.copy()
guesses=7
while banana_word_copy != listedudevinnage:
    lettre = input("Propose une lettre\n")
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
                print ("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
                print("Désolé ! Tu as perdu. Le mot/nom était " + word_to_find + ".")
                time.sleep(4)
                sys.exit()
            if guesses == 1:
                print("Non, désolé. La lettre " + lettre + " n'est pas dans le mot/nom.\nIl te reste " + str(guesses) + " essai avant de perdre")
                print ("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
                break
            else:
                print("Non, désolé. La lettre " + lettre + " n'est pas dans le mot/nom.\nIl te reste " + str(guesses) + " essais avant de perdre")
                if guesses == 6:
                    print ("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
                if guesses == 5:
                    print ("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
                if guesses == 4:
                    print ("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
                if guesses == 3:
                    print ("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
                if guesses == 2:
                    print ("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
                break
    print (" ".join(listedudevinnage) + "\n")       
else:
    time.sleep(1)
    print("Bien joué ! Tu as deviné le mot/nom qui était " + word_to_find)
    time.sleep(4)
