import random
import os
class gametime:
    # Function to get the computer's move
    def get_computer_move():
        moves = ['rock', 'paper', 'scissors']
        return random.choice(moves)

    # Function to determine the winner
    def get_winner(player_move, computer_move):
        if player_move == computer_move:
            return 'tie'
        elif player_move == 'rock':
            if computer_move == 'paper':
                return 'computer'
            else:
                return 'player'
        elif player_move == 'paper':
            if computer_move == 'scissors':
                return 'computer'
            else:
                return 'player'
        elif player_move == 'scissors':
            if computer_move == 'rock':
                return 'computer'
            else:
                return 'player'
        else:
            return None

    # Main function to run the game
    def rock_paper_scissors():
        print('Welcome to Rock-Paper-Scissors!')
        
        while True:
            # Get player's move
            os.system('cls')
            player_move = input('Enter your move (rock, paper, or scissors): ').lower()
            while player_move not in ['rock', 'paper', 'scissors']:
                player_move = input('Invalid move. Please enter rock, paper, or scissors: ').lower()
            
            # Get computer's move
            computer_move = gametime.get_computer_move()
            print('Computer chose ' + computer_move + '.')
            
            # Determine winner
            winner = gametime.get_winner(player_move, computer_move)
            if winner == 'tie':
                print('It\'s a tie!')
            else:
                print(winner.capitalize() + ' wins!')
            
            # Ask if player wants to play again
            play_again = input('Do you want to play again? (y/n): ').lower()
            if play_again != 'y':
                break
        
        print('Thanks for playing!')
