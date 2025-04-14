
import java.util.Scanner;

public class TicTacToe {
    private static final int BOARDSIZE = 3;
    private enum Status { WIN, DRAW, CONTINUE }
    private char[][] board;
    private boolean firstPlayer;
    private boolean gameOver;

    public TicTacToe() {
        board = new char[BOARDSIZE][BOARDSIZE];
        for (int i = 0; i < BOARDSIZE; i++) {
            for (int j = 0; j < BOARDSIZE; j++) {
                board[i][j] = ' ';
            }
        }
        firstPlayer = true;
        gameOver = false;
    }

    // Main gameplay loop
    public void play() {
        Scanner scanner = new Scanner(System.in);
        while (!gameOver) {
            printBoard();
            int row, col;
            do {
                printStatus(firstPlayer ? 'X' : 'O');
                System.out.print(": Enter row (0, 1 or 2): ");
                row = scanner.nextInt();
                printStatus(firstPlayer ? 'X' : 'O');
                System.out.print(": Enter column (0, 1 or 2): ");
                col = scanner.nextInt();
            } while (!validMove(row, col));

            board[row][col] = firstPlayer ? 'X' : 'O';
            Status status = gameStatus();
            if (status == Status.WIN) {
                printBoard();
                System.out.println("Player " + (firstPlayer ? 'X' : 'O') + " wins.");
                gameOver = true;
            } else if (status == Status.DRAW) {
                printBoard();
                System.out.println("Game is a draw.");
                gameOver = true;
            }
            firstPlayer = !firstPlayer;
        }
        scanner.close();
    }

    // Display the game board
    private void printBoard() {
        int count = 2;
        System.out.println(" ______________________________");
        for (int x = 0; x < 1; x++) {
            System.out.println("|         |         |         |");
            for (int i = 0; i < BOARDSIZE; i++) {
                System.out.print("|");
                for (int j = 0; j < BOARDSIZE; j++) {
                    System.out.print("    " + board[i][j] + "    |");
                }
                System.out.println("
|_________|_________|_________|");
                if (count-- > 0) {
                    System.out.println("|         |         |         |");
                }
            }
        }
    }

    // Show current player's turn
    private void printStatus(char player) {
        System.out.print("Player " + player);
    }

    // Check if a move is valid
    private boolean validMove(int row, int col) {
        if (row < 0 || row >= BOARDSIZE || col < 0 || col >= BOARDSIZE || board[row][col] != ' ') {
            System.out.println("Invalid move.");
            return false;
        }
        return true;
    }

    // Evaluate game state
    private Status gameStatus() {
        for (int i = 0; i < BOARDSIZE; i++) {
            if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2])
                return Status.WIN;
            if (board[0][i] != ' ' && board[0][i] == board[1][i] && board[1][i] == board[2][i])
                return Status.WIN;
        }
        if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2])
            return Status.WIN;
        if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0])
            return Status.WIN;

        for (int i = 0; i < BOARDSIZE; i++) {
            for (int j = 0; j < BOARDSIZE; j++) {
                if (board[i][j] == ' ')
                    return Status.CONTINUE;
            }
        }
        return Status.DRAW;
    }

    // Entry point
    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.play();
    }
}
