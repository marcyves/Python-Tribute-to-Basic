#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Awari
    =====

    The ancient African Game

    Freely inspired from Basic code at https://www.atariarchives.org/basicgames/showpage.php?page=6 

(c) 2019 Marc Augier m.augier@me.com

"""

class Awari :
    def __init__(self):
        self.board = [3,3,3,3,3,3,
                      0,
                      3,3,3,3,3,3,
                      0]

    def printBoard(self):
        print("   ", end='')
        for i in range(12,6,-1):
            print(self.board[i], end=' ')
        print("")
        print("{}              {}".format(self.board[13],self.board[6]))
        print("   ", end='')
        for i in range(0,6):
            print(self.board[i], end=' ')
        print("")

if __name__ == "__main__":
    print("AWARI")
    game = Awari()

    game.printBoard()