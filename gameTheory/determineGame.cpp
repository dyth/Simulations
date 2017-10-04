#include <iostream>
using namespace std;

int play_game(int playerMove) {
	/*
	 * Randomly generate opponents move
	 * return incremental scores from result of both
	 */
	int opponentMove = rand() % 2;
	
	int playerScore[2][2] = {{-1, 0}, {0, -2}};
	int opponentScore[2][2] = {{-1, 0}, {0, -2}};
	
	int playerInc = playerScore[playerMove][opponentMove];
	int playerInc = playerScore[playerMove][opponentMove];

	return 0;	
}

int main() {
	int input_var = 0;
	do {
		cout << "Enter a number (-1 = quit): ";
		if (!(cin >> input_var)) {
			cout << "You entered a non-numeric. Exiting..." << endl;
			break;
		}
		if (input_var != -1) {
			cout << "You entered " << input_var << endl;
		}
	} while (input_var != -1);
	cout << "All done." << endl;
	return 0;
}
