import random


def get_computer_choice():
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    return choices[random.randint(1, 3)]


def get_human_choice():
    valid_choices = ["rock", "paper", "scissors", "quit"]
    while True:
        choice = input("Enter rock, paper, scissors, or quit: ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please try again.")


def determine_winner(human, computer):
    if human == computer:
        return "draw"
    elif (human == "rock" and computer == "scissors") or \
         (human == "scissors" and computer == "paper") or \
         (human == "paper" and computer == "rock"):
        return "human"
    else:
        return "computer"


def play_round():
    computer_choice = get_computer_choice()
    human_choice = get_human_choice()

    if human_choice == "quit":
        return None, None

    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(human_choice, computer_choice)

    if winner == "draw":
        print("This round is a draw!")
        return 0, 0
    elif winner == "human":
        print("You win this round!")
        return 1, 0
    else:
        print("Computer wins this round!")
        return 0, 1


def main():
    human_score, computer_score = 0, 0

    while True:
        human_points, computer_points = play_round()

        if human_points is None:
            break

        human_score += human_points
        computer_score += computer_points

        print(f"Score - You: {human_score}, Computer: {computer_score}\n")

    print("Tournament Over!")
    print(f"Final Score - You: {human_score}, Computer: {computer_score}")

    if human_score > computer_score:
        print("Congratulations! You won the tournament!")
    elif computer_score > human_score:
        print("Computer wins the tournament! Better luck next time!")
    else:
        print("The tournament ended in a draw!")


if __name__ == "__main__":
    main()
