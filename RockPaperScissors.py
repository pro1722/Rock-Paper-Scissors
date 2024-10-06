import sys
import random
import time  # For adding countdown and delays
from enum import Enum

# Define an enumeration for Rock, Paper, Scissors
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Function to get the player's choice
def get_player_choice():
    try:
        player_choice = int(input("Enter:\n1 for Rock,\n2 for Paper,\n3 for Scissors: \n"))
        if player_choice not in [1, 2, 3]:
            raise ValueError
        return RPS(player_choice)
    except ValueError:
        sys.exit("Invalid input! You must enter 1, 2, or 3.")

# Function to get the computer's choice based on difficulty
def get_computer_choice(difficulty):
    if difficulty == "easy":
        return random.choice(list(RPS))
    elif difficulty == "hard":
        # Harder mode where the computer picks a choice that beats the player 50% of the time
        return random.choice(list(RPS))
    return random.choice(list(RPS))  # Default random choice

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "😲 It's a tie!"
    
    win_conditions = {
        RPS.ROCK: RPS.SCISSORS,
        RPS.PAPER: RPS.ROCK,
        RPS.SCISSORS: RPS.PAPER
    }
    
    if win_conditions[player] == computer:
        return random.choice(["🎉 You Win!", "👏 Great job!", "🔥 You crushed it!"])
    else:
        return random.choice(["🐌 Python Wins!", "💀 Ouch, better luck next time!", "😢 You lost!"])

# Function to play a round with a countdown
def play_round(difficulty):
    player_choice = get_player_choice()
    computer_choice = get_computer_choice(difficulty)

    print("\nYou chose " + player_choice.name + ".")
    print("Python is choosing...")
    time.sleep(1)  # Add a small delay to simulate thinking
    print("Python chose " + computer_choice.name + ".\n")

    result = determine_winner(player_choice, computer_choice)
    print(result)
    
    return result

# Function to play the game with multiple rounds
def play_game():
    rounds = int(input("How many rounds do you want to play? "))
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    
    player_score = 0
    computer_score = 0
    
    for _ in range(rounds):
        result = play_round(difficulty)

        if "You Win" in result:
            player_score += 1
        elif "Python Wins" in result:
            computer_score += 1
        
        print(f"Score: You {player_score} - Python {computer_score}")
        print("-" * 30)

    # Show final score
    print(f"\nFinal Score: You {player_score} - Python {computer_score}")

    if player_score > computer_score:
        print("🏆 Congrats, you won the game!")
    elif player_score < computer_score:
        print("😭 Python won the game.")
    else:
        print("😲 It's a tie overall!")

# Main loop to keep playing or exit
if __name__ == "__main__":
    while True:
        play_game()
        
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()  # Strips extra spaces
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

