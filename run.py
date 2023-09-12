# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def welcome_message():
    """
    Writes the initial message of the site
    """
    print('Welcome to 3Dtic')


class GameFloor:
    """
    3 x 3 square game floor
    """
    def __init__(self,floor):
        self.floor_squares=[
            ['O','O','O'],
            ['O','O','O'],
            ['O','O','O']
        ]
        self.floor=floor 

    def assign_value(self,x,y,user):
        self.floor_squares[x][y] = user

    def print_floor(self):
        print(f'{self.floor} floor')
        for row in self.floor_squares:
            print(row)


def main():
    welcome_message()
    upper_floor=GameFloor('upper')
    upper_floor.print_floor()
    upper_floor.assign_value(0,1,'A')
    upper_floor.print_floor()


main()
