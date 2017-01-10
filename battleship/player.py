from board import Board

class Player:

    def __init__(self):
        set_name()
        self.board = [{'x': x, 'y': y, 'status': 0} for x in range(1,11) for y in list(map(chr, range(97, 107)))]
        self.arsenal = Arsenal()

    def set_name(self):
        self.name = input("Enter your name.")

    def setup(self):


    def check_hit(self, position):
    #check and return hit,miss,or 'name of ship'

    def ship_destroyed(self):

    def place_ships(self):
    #take input from player and place ships
