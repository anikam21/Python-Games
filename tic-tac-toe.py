import random 

class tic_tac_toe: 
    def __init__(self, response, rows):
        self.board = []
        self.response = response 
        self.rows = rows
                   
    
    def user_response(self, response):
        if user_ready == 'Y': 
            print("Lets get started!")
        else: 
            print("Okay let's play later")
        return response
    

    def the_board(self): 
        the_board = {'1': '', '2': ' ', '3': ' ',
                     '4': ' ',  '5': ' ', '6': ' ',
                     '7': ' ',  '8': ' ', '9': ' '}
        return the_board
    
    def create_board(board):
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print(board[7] + ' | ' + board[8] + ' | ' + board[9])
        
    def player_letter():
        letter = ''
        letter = input("Do you want to be X or O? \n").upper()
        

    def the_game():
        player_turn = 'O'
        
        


user_ready = input("Are you ready to play? Type (y/n)").upper()  
rows = int(input("How many rows do you want? \nType the number: "))                
start_game = tic_tac_toe(user_ready, rows)





