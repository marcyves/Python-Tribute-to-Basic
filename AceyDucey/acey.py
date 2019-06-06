#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Acey Ducey
==========

simulation of the Acey Ducey card game.

Freely inspired from Basic code at https://www.atariarchives.org/basicgames/showpage.php?page=2 

(c) 2019 Marc Augier m.augier@me.com

"""
from random import randint

class AceyDucey:

    def __init__(self, money):
        print("Acey Ducey Card Game")
        print("====================\n")
        print("Acey-Ducey is played in the following manner")
        print("The computer deals 2 cards face up")
        print("You have an option to bet or not depending")
        print("on whether or not you feel the card will have")
        print("a value between the first 2.\n")

        self.money = money
        self.current_bet   = 0
        self.game_over = False

        self.card1 = 0
        self.card2 = 0

    def bet(self):
        bet = -1

        print("\nYou now have {} euros".format(self.money))
        while bet < 0 or bet > self.money:
            try:
                bet = int(input("\nWhat is your bet? (0 to end) => "))
            except ValueError:
                bet = -1

        if bet > self.money:
            print("Sorry my friend, but you bet too much")
            print("You have only {} euros to bet".format(self.money))
        elif bet == 0:
            print("Chicken!!")
            self.game_over = True
        else:
            self.current_bet = bet
            self.money -= bet

    def over(self):
        if self.money == 0:
            self.game_over = True
        return self.game_over

    def display(self, card):
        
        if card < 11:
            print(card)
        elif card == 11:
            print("Jack")
        elif card == 12:
            print("Queen")
        elif card == 13:
            print("King")
        elif card == 14:
            print("Ace")

    def draw(self):
        print("\nHere are your next 2 cards")
        
        self.card1 = randint(1,14)
        self.card2 = randint(1,14)

        self.display(self.card1)
        self.display(self.card2)

if __name__ == "__main__":
    game = AceyDucey(100)
    
    while not game.over():
        game.draw()
        game.bet()

