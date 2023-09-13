# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from numpy import random

def run_game():
    """
    Writes the initial message of the site
    """
    print('Welcome to 3Dtic')
    print('This is a 3D tic tac toe game, it consist of three floors of the classic game')
    print('In order to win you need to form a straight line in any direction')
    print('You will play against the machine, empty spots are marked as O')
    print('The machine moves are marked as M, Your moves are marked as Y, Machine moves first')
    first_machine_move()

def first_machine_move():
    """
    creates a random move from the machine
    """
    floor_random=random.randint(3,size=3)
    floors[floor_random[0]].assign_value(floor_random[1],floor_random[2],'M')
    for floor in floors:
        print(floor.print_floor())

def get_user_move():
    """
    gets the user entries for positions
    asks for floor, x and y
    later validates
    """
    print('Please chose your move')
    print('Start with the floor number')
    print('0 for Bottom, 1 for mid or 2 for top')
    floor = input('Enter floor:/n')

class GameFloor:
    """
    accomodates a 3 x 3 square game floor
    contains two functions
    the first one updates the floor with the computer and user choices
    the second prints the floor
    """
    def __init__(self,floor):
        self.floor_squares=[
            ['O','O','O'],
            ['O','O','O'],
            ['O','O','O']
        ]
        self.floor = floor

    def assign_value(self,x,y,user):
        self.floor_squares[x][y] = user

    def print_floor(self):
        print(f'{self.floor} floor')
        for row in self.floor_squares:
            print(row)
        return ""

#data structure for the floors information
floors=[GameFloor('Top'),GameFloor('Mid'),GameFloor('Bottom')]


def main():
    run_game()

    
main()
