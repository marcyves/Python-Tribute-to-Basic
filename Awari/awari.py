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
        print("\aAWARI")
        print("=====\n")
        self.board = [3,3,3,3,3,3,
                      0,
                      3,3,3,3,3,3,
                      0]

#        for i in range(14):
#            self.board[i] = i

    def clearPit(self, pit):
        self.board[pit - 1] = 0

    def getBeans(self, pit):
        return self.board[pit-1]

    def dropOneBean(self, pit):
        self.board[pit - 1] += 1

    def dropBeans(self, pit, beans):
        self.board[pit - 1] += beans


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

    def playerMove(self):
        pit = 0
        while pit < 1 or pit > 6:
            try:
                pit = int(input("\nYour move? => "))
                if self.getBeans(pit) == 0:
                    pit = 0
                    print("Illegal move")
                    print("Again")
            except ValueError:
                pit = 0
                print("Again")
        home = 7

        k = pit

        # take all beans from pit played
        beans = self.getBeans(pit)
        self.clearPit(pit)

        # place beans in pits anticlockwise, starting on the next pit on the right
        for i in range(beans, 0, -1):
            pit += 1
            if pit > 13:
                pit = pit - 14
            self.dropOneBean(pit)

        # the last bean was dropped in an empty pit (now contains 1)
        # beans from the opposite side are taken and placed in player's 'wari'
        if self.getBeans(pit) == 1 and pit != 7 and pit != 14 and self.getBeans(14-pit) != 0:
            self.dropBeans(home, self.getBeans(14-pit)+1)
            self.clearPit(pit)
            self.clearPit(14-pit)
 



if __name__ == "__main__":
    game = Awari()

    while(True):
        game.printBoard()

        game.playerMove()

