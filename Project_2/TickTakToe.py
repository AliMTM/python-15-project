class Board:
    def __init__(self):
        self.board = []
        self.init_board()

    def init_board(self, winner=False):
        enum = 0
        for i in range(3):
            row = []
            for j in range(3):
                if winner:
                    row.append(" ")
                else:
                    row.append(f"{enum + 1}")
                    enum += 1
            self.board.append(row)

    def draw_board(self):
        print("+-------+")
        print(f"| {self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]} |")
        print("|--+-+--|")
        print(f"| {self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]} |")
        print("|--+-+--|")
        print(f"| {self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]} |")
        print("+-------+")

    def check_winner(self):
        winner = ""
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] \
                and self.board[0][0] == self.board[0][2] and not self.board[0][0].isdigit():

            winner = self.board[0][0]
            self.reset_board(True)
            self.board[0][0] = winner
            self.board[0][1] = winner
            self.board[0][2] = winner

        elif self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] \
                and self.board[1][0] == self.board[1][2] and not self.board[1][0].isdigit():

            winner = self.board[1][0]
            self.reset_board(True)
            self.board[1][0] = winner
            self.board[1][1] = winner
            self.board[1][2] = winner

        elif self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] \
                and self.board[2][0] == self.board[2][2] and not self.board[2][0].isdigit():

            winner = self.board[2][0]
            self.reset_board(True)
            self.board[2][0] = winner
            self.board[2][1] = winner
            self.board[2][2] = winner

        elif self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] \
                and self.board[0][0] == self.board[2][0] and not self.board[0][0].isdigit():

            winner = self.board[0][0]
            self.reset_board(True)
            self.board[0][0] = winner
            self.board[1][0] = winner
            self.board[2][0] = winner

        elif self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] \
                and self.board[0][1] == self.board[2][1] and not self.board[0][1].isdigit():

            winner = self.board[0][1]
            self.reset_board(True)
            self.board[0][1] = winner
            self.board[1][1] = winner
            self.board[2][1] = winner

        elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] \
                and self.board[0][2] == self.board[2][2] and not self.board[0][2].isdigit():

            winner = self.board[0][2]
            self.reset_board(True)
            self.board[0][2] = winner
            self.board[1][2] = winner
            self.board[2][2] = winner

        elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] \
                and self.board[0][0] == self.board[2][2] and not self.board[0][0].isdigit():

            winner = self.board[0][0]
            self.reset_board(True)
            self.board[0][0] = winner
            self.board[1][1] = winner
            self.board[2][2] = winner

        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] \
                and self.board[0][2] == self.board[2][0] and not self.board[0][2].isdigit():

            winner = self.board[0][2]
            self.reset_board(True)
            self.board[0][2] = winner
            self.board[1][1] = winner
            self.board[2][0] = winner

        if winner == "":
            return False
        else:
            self.draw_board()

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j].isdigit():
                    return False
        return True

    def reset_board(self, win=False):
        self.board = []
        self.init_board(win)

    def read_location(self, location):
        i = 0
        j = 0
        if 1 <= location <= 3:
            if location == 2:
                j = 1
            elif location == 3:
                j = 2
        elif 4 <= location <= 6:
            i = 1
            if location == 5:
                j = 1
            elif location == 6:
                j = 2
        elif 7 <= location <= 9:
            i = 2
            if location == 8:
                j = 1
            elif location == 9:
                j = 2
        return i, j

    def check_location(self, location):
        i, j = location
        if self.board[i][j] != "X" and self.board[i][j] != "O":
            return True
        return False

    def ask_for_input(self, player):
        while True:
            location = input("Please Enter The location you want or Q to quit\n")
            if location.isdigit():

                location = int(location)
                if 0 < location < 10:

                    location = self.read_location(location)

                    if self.check_location(location):

                        i, j = location

                        if player:
                            self.board[i][j] = "X"
                        else:
                            self.board[i][j] = "O"

                        break

                    else:
                        print("please chose non occupied location")

                else:
                    print("your number is not within the board range")

            elif location.lower() == 'q':
                quit()

            else:
                print("Invalid input please only enter a Number or Q to quit")


print("Welcome to Tik Tak Toe")

player = True

while True:
    q = input("Please chose Your Symbol X or O\n")
    if q.lower() == "x":
        break
    elif q.lower() == "o":
        player = False
        break
    elif q.lower() == 'q':
        quit()
    else:
        print("Invalid input please only enter X or O or Q to quit")

board = Board()

while True:

    board.draw_board()

    if board.check_winner() or board.check_draw():
        q = input("if you want to restart press Y otherwise press any other button\n")
        if q.lower() == "y":
            board.reset_board()
            continue
        else:
            break

    if player:
        print("Player X Turn")
    else:
        print("Player O Turn")

    board.ask_for_input(player)

    player = not player
