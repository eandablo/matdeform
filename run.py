# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import numpy as np

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


def start_game():
    """
    Writes the initial message of the site
    calculates the first move given by the computer using a random generator
    """
    print('This is a 3D tic tac toe game, it consist of three floors of the classic game')
    print('You need to win conventianally 2 of the 3 floors or connecting the 3 floors with a vertival line, by choosing a move 1 floor at the time')
    print('You will play against the machine, empty spots are marked as O')
    print('The machine moves are marked as M, your moves are marked as Y. Machine moves first')
    random_machine_move()

def random_machine_move():
    """
    creates a random move from the machine
    assigns the 
    prints the first outline with the first move from the computer
    """
    floor_random=np.random.randint(3,size=3)
    update_floor(floor_random,'M')

def update_floor(data,mover):
    floors[data[0]].assign_value(data[1],data[2],mover)
    for floor in floors:
        print(floor.print_floor())

def get_user_move():
    """
    gets the user entries for positions
    asks for floor number, x position and y position
    validates the entries
    if data is valid updates floors array with user entry
    otherwise asks again for data
    """
    while True:
        print('Please chose your move, providing 3 numbers from 1 to 3')
        user_move=[]
        while True:
            move = input('Enter floor number, 1 for Bottom, 2 for mid or 3 for top:\n')
            if validate_number(move):
                break
        user_move.append(int(move)-1)
        while True:
            move = input('Enter the vertical position:\n')
            if validate_number(move):
                break
        user_move.append(int(move)-1)
        while True:
            move = input('Enter the horizontal position:\n')
            if validate_number(move):
                break
        user_move.append(int(move)-1)
        if empty_point(user_move):
            break
        else:
            print('Space is not free, please choose a free point')
    update_floor(user_move,'Y')

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

def empty_point(data):
    """
    validates if user entry is already busy
    """
    if floors[data[0]].floor_squares[data[1]][data[2]]=='O':
        return True
    else:
        return False

def check_individual_floor(data,user):
    """
    converts data into a numpy matrix to perform math
    data takes a floor class and user takes either 'M' or 'Y'
    """
    floor_matrix=np.zeros((3,3),dtype=int)
    floor_matrix_mirror=np.zeros((3,3),dtype=int)
    for i in range(3):
        for j in range(3):
            if data[i][j] == user:
                floor_matrix[i,j]=1
                floor_matrix_mirror[i,2-j]=1
    sum_row=np.append(np.sum(floor_matrix,axis=0),np.sum(floor_matrix,axis=1))
    sum_row=np.append(sum_row,np.trace(floor_matrix))
    sum_row=np.append(sum_row,np.trace(floor_matrix_mirror))
    return 3 in sum_row

"""
variable floors is a structure containing all three separated floors
each floor structure is obtained by assigning a class GameFloor
"""
floors=[GameFloor('Bottom'),GameFloor('Mid'),GameFloor('Top')]

def main():
    start_game()
    while True:
        get_user_move()
        if check_individual_floor(floors[0].floor_squares,'Y'):
            break

main()
