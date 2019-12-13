# Developed by: Ben Muzzy
''' Program based on/references 2 sites:
Our class book: https://runestone.academy/runestone/books/published/pythonds/Graphs/TheKnightsTourProblem.html
Udemy Course: https://www.udemy.com/course/algorithmic-problems-in-python/
'''

''' Knight's Tour Program Summary:
In chess, a knight can jump in a unique way. It moves either 2 places horizontally and 1 place vertically or 2 places vertically and 1 place horizontally in each direction, So the complete movement looks like English letter "L".

In this scenario, there is an empty chess board, and a knight that can start moving from any place on the board. This program will check whether the knight can visit all the places on the board (moving to each place only once). If the knight can move to all the places on the board, then the number of moves needed to reach that location from the starting point is displayed.
'''


class KT_Board:
    '''This is a "open" style of the a Knight's Tour
    as we don't end in the same spot we started. '''
    def __init__(self, brd_size):
        self.brd_size = brd_size
        # Positve "move_x" moves to the right.
        # Negtagive "move_x" moves to the left
        self.move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        # Positve "move_y" moves to the up.
        # Negtagive "move_y" moves to the down.
        self.move_y = [1, 2, 2, 1, -1, -2, -2, -1]
        # -1 is used to keep track of the places the knight has moved to.
        self.kt_matrix = [[-1 for x in range(brd_size)] for x in range(brd_size)]
    def val_move(self, x, y):
        if x < 0 or x >= self.brd_size:
            return False
        if y < 0 or y >= self.brd_size:
            return False
        if self.kt_matrix[x][y] > -1:
            return False
        return True

    def attempt_solve(self, move_count, x, y):
        if move_count == (self.brd_size * self.brd_size):
            return True
        for index in range(self.brd_size):
            # Handles the next move
            kt_x_move = x + self.move_x[index]
            kt_y_move = y + self.move_y[index]
            # checks that the next move is a legal move.
            if self.val_move(kt_x_move, kt_y_move):
                self.kt_matrix[kt_x_move][kt_y_move] =  move_count
            # Checks if the the knight can make the next move
                if self.attempt_solve(move_count+1, kt_x_move, kt_y_move):
                    return True
            # Checks if the knight already been to the next move on the board
                self.kt_matrix[kt_x_move][kt_y_move] = -1
        return False

    def attempt_solution(self):
        # starting coordinates of the knight
        self.kt_matrix[0][0] = 0
        if self.attempt_solve(1, 0, 0):
            self.disp_kts()
        else:
            print("\nNo valid solution found!\n")

    def disp_kts(self):
        for index in range(self.brd_size):
        # Variable j is used for complex numbers instead of index.
            for j in range(self.brd_size):
        # Outputs the knight's tour move in the order they occured.
                print(self.kt_matrix[index][j],end=" "),
            print('\n')

if __name__ == "__main__":
    '''The number in KT_Board() specifies
     the size of the chess board. So a size of 4 is 4x4, etc.'''
    knightTour = KT_Board(7)
    knightTour.attempt_solution()