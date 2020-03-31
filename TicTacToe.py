import random
board =['x','o','o',
        'o','x','o',
        'o','o','x']    
j=i=random.randint(2,3)

def display_board():
    global board
    print('\n'*100)
    print(" " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("---------------")
    print(" " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("---------------")
    print(" " + board[0] + "  |  " + board[1] + "  |  " + board[2])

def clear_board():
    for i in range(len(board)):
        board[i] = ' '

def get_input(player_no):
    position = int(input(f"Player {player_no}  - Please enter the position: "))
    check_valid_ip(player_no,position)
        
def check_valid_ip(player_no,position):
    if position < 1 or position > 9:
        print("please enter numbers in the range 1 to 9 only")
        get_input(player_no)
    elif board[position-1] != " ":
        print("Position marked already")
        get_input(player_no)
    else:
        update_board(player_no,position)

def update_board(player_no,position):
    if player_no==1:
        board[position-1]="x"
    else:
        board[position-1]="o" 

def check_win():
    if ((board[0]==board[1]==board[2]!=" ") or 
        (board[3]==board[4]==board[5]!=" ") or
        (board[6]==board[7]==board[8]!=" ") or
        (board[0]==board[3]==board[6]!=" ") or
        (board[1]==board[4]==board[7]!=" ") or
        (board[2]==board[5]==board[8]!=" ") or
        (board[0]==board[4]==board[8]!=" ") or
        (board[2]==board[4]==board[6]!=" ")) :
        return True
    else:
        return False
        
def initialize():
    clear_board()
    display_board()
    print("Welcome to tic tac toe")
    return random.randint(2,3)

def once_more():
    play_again =''
    while play_again != int(1) and play_again != int(0):
        play_again = int(input("Enter 1 to play again or  0 to quit : "))
    
    if play_again == int(0) : 
        return False
    else:
        return True
    

j = i = initialize()

while True: 
    while i<9+j:
        if i%2==0:
            player_no = 1
        else:
            player_no = 2

        get_input(player_no)
        display_board()
        if check_win():
            print( f"\nPlayer {player_no} Won \n")
            if not once_more():
                break
            else:
                j=i = initialize()
            
        else:
            i+=1
    else:
        print ("game tied")
        if not once_more():
            break
        else:
            j=i= initialize()
