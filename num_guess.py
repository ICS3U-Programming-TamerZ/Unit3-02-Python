#!/usr/bin/env python3
# Created by: Tamer Zreg
# Created on: Oct 08
# This program checks if a user's integer guess is correct


import random


run_game = "__True__"


def game_loop():
    max_number = int(input("what is your max number? "))
    guess_number = int(input("What is your guess? "))
    random_number = random.randint(1, max_number)

    # This line will run when the user guesses the right number.
    if guess_number == random_number:
        print("yes")

    # This line will run when the user guesses wrong.
    if guess_number != random_number:
        print("wrong it was {}.".format(random_number))


if __name__ == "__main__":
    while run_game == "__True__":
        game_loop()
