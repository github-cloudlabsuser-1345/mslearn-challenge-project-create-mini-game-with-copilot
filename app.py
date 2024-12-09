import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def main():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        if result == 'win':
            print("You win!")
            player_score += 1
        elif result == 'lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score: Player {player_score} - Computer {computer_score}")
    
    print("Game over!")
    print(f"Final Score: Player {player_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()