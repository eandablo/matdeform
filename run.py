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
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.floor = floor

    def assign_value(self,x,y,user):
        self.floor_squares[x][y] = user

    def print_floor(self):
        print(f'{self.floor} floor')
        i=0
        for row in self.floor_squares:
            print(f' {row[0]} ¦ {row[1]} ¦ {row[2]}')
            if i<2:
                print('-----------') 
            i+=1
        return ""


def start_game():
    """
    Writes the initial message of the site
    calculates the first move given by the computer using a random generator
    """
    print('This is a 3D tic tac toe game, it consist of three floors of the classic game')
    print('You need to win conventianally 2 of the 3 floors or connecting the 3 floors with a vertival line, by choosing a move 1 floor at the time')
    print('You will play against the machine')
    print('The machine moves are marked as M, your moves are marked as Y. Machine moves first')
    input('Press enter to start')
    random_machine_move()

def random_machine_move():
    """
    creates a random move from the machine
    """
    floor_random=np.random.randint(3,size=3)
    update_floor(floor_random,'M')

def update_floor(data,mover):
    """
    update floor with either machine or user move
    variable data is a list of numbers for [floor,vertical,horizontal]
    mover variable takes either M  or Y
    finally prints the layout
    """
    floors[data[0]].assign_value(data[1],data[2],mover)
    if mover=='M':
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
    raises a ValueError if entry is not a number or number outside scope
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
    data is a list of numbers for [floor,vertical,horizontal]
    """
    if floors[data[0]].floor_squares[data[1]][data[2]] == ' ':
        return True
    else:
        return False

def machine_intel_move():
    """
    Decides the next move from the machine by analising the floors 
    """
#    win_move=find_critical_spot('M')  #winning move
#    if win_move:
#        update_floor(win_move,'M')
#        return
    block_move=find_critical_spot('Y')  #blocking move
    if block_move:
        update_floor(block_move,'M')
        return
    move=machine_kernel_move()
    update_floor(move,'M')
    
def find_critical_spot(mover):
    """
    Find rows and lines with two spaces marked by the same user
    """ 
    if mover=='M':
        contender='Y'
    else:
        contender='M'
    floor_num=0
    for floor in floors:
        lines_sum=summarize_floor(floor.floor_squares,mover)
        ver_sum=lines_sum[:3]
        hor_sum=lines_sum[3:6]
        trace=lines_sum[6]
        antitrace=lines_sum[7]
        lines_sum_contender=summarize_floor(floor.floor_squares,contender)
        ver_sum_contender=lines_sum_contender[:3] #sum of columns
        hor_sum_contender=lines_sum_contender[3:6]  #sum of rows
        trace_contender=lines_sum_contender[6]
        antitrace_contender=lines_sum_contender[7]
        if 2 in ver_sum:
            index_mover=np.where(ver_sum==2)[0]
            for index_2 in index_mover:
                if ver_sum_contender[index_2]==0:
                    for i in range(3):
                        if floor.floor_squares[i][index_2]==" ":
                            next_move=[floor_num,i,index_2]
                            break
                    return next_move
        if 2 in hor_sum:
            index_mover=np.where(hor_sum==2)[0]
            for index_1 in index_mover:
                if hor_sum_contender[index_1]==0:
                    for i in range(3):
                        if floor.floor_squares[index_1][i]==" ":
                            next_move=[floor_num,index_1,i]
                            break
                    return next_move
        if trace==2:
            if trace_contender==0:
                for i in range(3):
                    if floor.floor_squares[i][i]==" ":
                        next_move=[floor_num,i,i]
                        break
                return next_move
        if antitrace==2:
            if antitrace_contender==0:
                for i in range(3):
                    if floor.floor_squares[i][2-i]==" ":
                        next_move=[floor_num,i,2-i]
                        break
                return next_move
        floor_num+=1

    return False

def summarize_floor(data,user):
    """
    converts data variable containing a floor into a numpy matrix
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
    return sum_row

def sumarize_columns(user):
    """
    sums columns and return values for the user
    """
    column_sum=np.zeros((3,3),dtype=int)
    for i in range(3):
        for j in range(3):
            addition=0
            for floor in floors:
                if floor.floor_squares[i][j]==user:
                    addition+=1
            column_sum[i,j]=addition
    return column_sum

def machine_kernel_move():
    """
    uses kernels to calculate the probability matrices
    """
    max_val=[]
    max_val_coor=[]
    for floor in floors:
        machine_multiplier=np.zeros((3,3),dtype=int)
        user_multiplier=np.zeros((3,3),dtype=int)
        
        for i in range(3):
            for j in range(3):
                if floor.floor_squares[i][j]=='M':
                    machine_multiplier[i,j]=1
                if floor.floor_squares[i][j]=='Y':
                    user_multiplier[i,j]=1
        prob_matrix=np.add(np.matmul(machine_multiplier,machine_kernel),
                           np.matmul(user_multiplier,user_kernel))
        prob_matrix=np.add(prob_matrix,np.random.rand(3,3))
        merge_matrix=np.add(machine_multiplier,user_multiplier)
        for i in range(3):
            for j in range(3):
                if merge_matrix[i,j]==1:
                    prob_matrix[i,j]=0
        max_val.append(prob_matrix.max())
        v_max=np.argmax(prob_matrix)//3
        h_max=np.argmax(prob_matrix)-v_max*3
        max_val_coor.append([v_max,h_max])
    max_global=max_val[0]
    max_global_coor=max_val_coor[0]
    max_floor=0
    for i in range(1,3):
        if max_val[i]>max_global:
            max_global=max_val[i]
            max_global_coor=max_val_coor[i]
            max_floor=i
    return [max_floor,max_global_coor[0],max_global_coor[1]]

#variable floors is a structure containing all three separated floors
#each floor structure is obtained by assigning a class GameFloor
floors=[GameFloor('Bottom'),GameFloor('Mid'),GameFloor('Top')]

#define kernels as random matrix for both machine and user 
machine_kernel=np.random.rand(3,3)
user_kernel=np.random.rand(3,3)

def main():
    start_game()
    while True:
        get_user_move()
        machine_intel_move()
        column_count=sumarize_columns('Y')
        if 3 in column_count:
            break
        floor_count=summarize_floor(floors[0].floor_squares,'Y')
        if 3 in floor_count:
            break
#    machine_intel_move()
    

main()