#include <string>
#include <iostream>
using namespace std;

string getComputerChoice() {
    string choices[] = {"rock", "paper", "scissors"};
    return choices[rand() % 3]; // Randomly pick one of the three choices
}

string getHumanChoice() {
    string choice;
    while (true) {
        cout << "Enter rock, paper, scissors, or quit: ";
        cin >> choice;
        if (choice == "rock" || choice == "paper" || choice == "scissors" || choice == "quit") {
            return choice;
        }
        cout << "Invalid input. Please try again.\n";
    }
}

string determineWinner(string human, string computer) {
    if (human == computer) {
        return "draw";
    } else if ((human == "rock" && computer == "scissors") || 
               (human == "scissors" && computer == "paper") || 
               (human == "paper" && computer == "rock")) {
        return "human";
    } else {
        return "computer";
    }
}

bool playRound(int &humanScore, int &computerScore) {
    string computerChoice = getComputerChoice();
    string humanChoice = getHumanChoice();

    if (humanChoice == "quit") {
        return false; // End game
    }

    cout << "Computer chose: " << computerChoice << endl;
    string winner = determineWinner(humanChoice, computerChoice);

    if (winner == "draw") {
        cout << "This round is a draw!\n";
    } else if (winner == "human") {
        cout << "You win this round!\n";
        humanScore++;
    } else {
        cout << "Computer wins this round!\n";
        computerScore++;
    }

    cout << "Score - You: " << humanScore << ", Computer: " << computerScore << "\n\n";
    return true;
}

int main() {
    srand(time(0)); // Seed random number generator
    int humanScore = 0, computerScore = 0;

    while (playRound(humanScore, computerScore)) {}

    cout << "Tournament Over!\n";
    cout << "Final Score - You: " << humanScore << ", Computer: " << computerScore << endl;

    if (humanScore > computerScore) {
        cout << "Congratulations! You won the tournament!\n";
    } else if (computerScore > humanScore) {
        cout << "Computer wins the tournament! Better luck next time!\n";
    } else {
        cout << "The tournament ended in a draw!\n";
    }

    return 0;
}

 
