# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from numpy import random

def start_game():
    """
    Writes the initial message of the site
    calculates the first move given by the computer using a random generator
    """
    print('This is a 3D tic tac toe game, it consist of three floors of the classic game')
    print('You need to win conventianally 2 of the 3 floors or connecting the 3 floors with a vertival line, by choosing a move 1 floor at the time')
    print('You will play against the machine, empty spots are marked as O')
    print('The machine moves are marked as M, your moves are marked as Y. Machine moves first')
    first_machine_move()

def first_machine_move():
    """
    creates a random move from the machine
    assigns the 
    prints the first outline with the first move from the computer
    """
    floor_random=random.randint(3,size=3)
    floors[floor_random[0]].assign_value(floor_random[1],floor_random[2],'M')
    for floor in floors:
        print(floor.print_floor())

def get_user_move():
    """
    gets the user entries for positions
    asks for floor number, x position and y position
    later validates the entries
    """
    print('Please chose your move, providing 3 numbers from 1 to 3')
    while True:
        floor = input('Enter floor number, 1 for Bottom, 2 for mid or 3 for top:\n')
        if validate_number(floor):
            break
    while True:
        horizontal = input('Enter the horizontal position:\n')
        if validate_number(horizontal):
            break
    while True:
        vertical = input('Enter the vertical position:\n')
        if validate_number(vertical):
            break

def validate_number(num):
    """
    Checks that entry is a number between 1 and 3
    """
    try:
        int(num)
        if int(num)<1 or int(num)>3:
            raise ValueError('Value must be a number between 1 and 3')
    except ValueError as e:
        print(f'Invalid position:{e}')
        return False
    return True


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
    start_game()
    get_user_move()

main()
