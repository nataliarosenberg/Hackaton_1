"""
Program, będący implementacją gry "wisielec".

Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.
"""

import random


words = 'monkey zebra dog cat swan ball pen fox panda yellow purple rose outdoor computer spider smile lemon apple work department logic'.split()


def check_win(word,quessed_letters):
    for letter in word:
        if not letter in quessed_letters:
            return False
    return True

def print_word(word, quessed_letters):
    for letter in word:
        if letter in quessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def main():
    chosen_word = random.choice(words)
    quessed_letters = []
    round = 5
    i = 0
    while True:
        print_word(chosen_word,quessed_letters)
        if check_win(chosen_word, quessed_letters):
            print("You win")
            return

        if i >= round: break
        i +=1

        quess = input("Enter your letter or whole word: ")
        if len(quess) > 1 and quess == chosen_word:
            print("You win")
            return
        elif len(quess)> 1 and not quess == chosen_word:
            print("Wrong, try again")
            continue
        elif len(quess) ==1:
            if quess in chosen_word:
                quessed_letters.append(quess)
                print("You quessed a letter")
                if check_win(chosen_word,quessed_letters):
                    print("You win")
                    return
            else:
                print("Try again")
    print(f"The word was: {chosen_word}")
main()



