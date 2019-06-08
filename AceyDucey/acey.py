#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Acey Ducey
==========

Simulation of the Acey Ducey card game.

Freely inspired from Basic code at https://www.atariarchives.org/basicgames/showpage.php?page=2 

(c) 2019 Marc Augier m.augier@me.com

"""
from random import randint

class AceyDucey:

    def __init__(self, money):
        print("\aAcey Ducey Card Game")
        print("====================\n")
        print("Acey-Ducey is played in the following manner")
        print("The computer deals 2 cards face up")
        print("You have an option to bet or not depending")
        print("on whether or not you feel the card will have")
        print("a value between the first 2.\n")

        self.money_init = money
        self.money = money
        self.game_over = False

        self.card1 = 0
        self.card2 = 0

    def bet(self):
        bet = -1

        print("\nYou now have {} euros".format(self.money))
        while bet < 0 or bet > self.money:
            try:
                bet = int(input("\nWhat is your bet? (0 to pass) => "))
            except ValueError:
                bet = -1

        if bet > self.money:
            print("Sorry my friend, but you bet too much")
            print("You have only {} euros to bet".format(self.money))
        elif bet == 0:
            print("Chicken!!")

        return bet

    def gameOver(self):
        if self.money <= 0:
            self.game_over = True
            self.money = 0
            print("\nSorry friend, but you run out of cash")
        return self.game_over

    def displayCard(self, card):
        
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
        
        self.card1 = randint(2,14)
        self.card2 = randint(2,14)

        if self.card1 > self.card2:
            self.card1, self.card2 = self.card2, self.card1

        self.displayCard(self.card1)
        self.displayCard(self.card2)

    def checkResult(self, card, bet):
        if card > self.card1 and card < self.card2:
            print("You win!!!")
            self.money += bet
        else:
            print("Sorry, you lose")
            self.money -= bet
    
    def newGame(self):

        if self.money == 0:
            answer = ""
            while  answer.upper()[0:1] != "Y" and  answer.upper()[0:1] != "N":
                answer = input("\nTry again? (yes or no) => ")

            if  answer.upper()[0:1] == "Y":
                self.money = self.money_init
                self.game_over = False
                return True
            else:
                return False
        else:
            return True

if __name__ == "__main__":
    game = AceyDucey(100)
    
    while game.newGame():
        while not game.gameOver():
            game.draw()
            my_bet = game.bet()
            if my_bet != 0:
                my_card = randint(2,14)
                game.displayCard(my_card)
                game.checkResult(my_card, my_bet)

    print("ok, hope you had fun")



