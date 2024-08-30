import random

def game():
    
    choices = ['paper','rock','scissors']
    
    while True:
        
        computer_word = random.choice(choices) # the computer word
        computer_score = 0
        user_score = 0
        result = ""

        for i in range(3) :
            user_word =input("pleas enter a word from ['paper','rock','scissors'] : ").lower()
            if user_word not in ['paper','rock','scissors'] :
                print("""please enter a word from ['paper','rock','scissors']""" )

            if user_word == computer_word:
                print("The two Words tied")

            elif user_word == 'paper':
                if computer_word == 'rock':
                    print('paper beats Rock, you\'ve win :) ')
                    user_score += 1 
                else: #computer_word = 'scissors'
                    print('Scissors beats paper, you\'ve Lost :(')
                    computer_score += 1
            elif user_word == 'rock':
                if computer_word =='paper':
                    print('paper beats Rock, you\'ve Lost :(')
                    computer_score += 1
                else: #computer_word = 'Scissors'
                    print('Rock beats Scissors, you\'ve Win :)')
                    user_score += 1 
            elif user_word == 'scissors':
                if computer_word == 'paper':
                    print('Scissors beats Paper, you\'ve win :) ')
                    user_score += 1 
                else: #computer_word = 'Rock'
                    print('Rock beats Scissors, you\'ve Lost :(')
                    computer_score += 1
        print()
        if computer_score == user_score:
            result = ('No one win the game tied')
        elif computer_score > user_score:
            result = (f"""you lost the game
                |---| 
                |   0 
                |  /|\  
                |  / \ """)
        elif computer_score < user_score:
            result = (f"""You Win The Game Congratulation ------ :)""")

        print('-'*50)
        print(f"""your score is = {user_score}\nThe computer score is = {computer_score}\n{result}""")



        play_again = input('Do you want to play again - - (y/n):').lower()
        print()
        if play_again == 'n':
            print("Game Over!")
            break
        
        
        
game()