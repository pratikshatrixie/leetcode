#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool isValidSudoku(vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
        unordered_set<char> rowSet;
        unordered_set<char> colSet;
        unordered_set<char> boxSet;

        for (int j = 0; j < 9; j++) {
            // Check Row
            if (board[i][j] != '.' && rowSet.count(board[i][j]))
                return false;
            rowSet.insert(board[i][j]);

            // Check Column
            if (board[j][i] != '.' && colSet.count(board[j][i]))
                return false;
            colSet.insert(board[j][i]);

            // Check 3x3 Sub-boxes
            int boxRow = 3 * (i / 3) + j / 3;
            int boxCol = 3 * (i % 3) + j % 3;
            if (board[boxRow][boxCol] != '.' && boxSet.count(board[boxRow][boxCol]))
                return false;
            boxSet.insert(board[boxRow][boxCol]);
        }
    }

    return true;
}

int main() {
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    bool isValid = isValidSudoku(board);
    if (isValid) {
        cout << "The Sudoku board is valid." << endl;
    } else {
        cout << "The Sudoku board is not valid." << endl;
    }

    return 0;
}
