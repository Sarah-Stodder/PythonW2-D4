from random import choice
import os
        # Get a word to Guess
class LetterBoard():
    MAX_MOVES = 7
    WORD_BANK = ("cookie", "shortcake", "cheesecake", "tiramisu",
             "donut", "cupcakes", "baklava", "cannoli", "chocotaco")

    def __init__(self):
        self.word = choice(LetterBoard.WORD_BANK)
        self.guessed_letters = []
        self.number_of_moves = 0


    def show_word(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        board = ["_ " if letter not in self.guessed_letters else letter for letter in self.word]
        for letter in board:
            print(letter, end=" ")
        print()
        print("Guessed Letters: ", end=" ")
        if self.guessed_letters:
            for letter in self.guessed_letters:
                print(letter, end=" ")
        else:
            print("You haven't guessed a letter yet")
        print()
        print(f"You have {LetterBoard.MAX_MOVES - self.number_of_moves} moves left")



    def guess_letter(self, letter):
        if len(letter) > 1:
            print('Invalid guess, must be a single character')
            return
        if letter in self.word:
            count = self.word.count(letter)
            print(f"you found {count} {letter}{'s' if count > 1 else ''}")
        else:
            print(f"{letter} is not in the word")
            self.number_of_moves+=1
        self.guessed_letters.append(letter)


    def check_if_all_letters_guessed(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True


    def user_won(self):
        print(f"Congrats You Solved the Puzzle with {LetterBoard.MAX_MOVES - self.number_of_moves} move{'s' if self.number_of_moves > 1 else ''} left")

            
    def guessed_word_correct(self, word):
        if word == self.word:
            return True
        return False

    def has_guesses_left(self):
        if self.number_of_moves < LetterBoard.MAX_MOVES:
            return True
        return False
    
    def user_lost(self):
        print("I AM SOOO SORRYYYY YOU ARE SOO BAD AT THIISSS GAME,  WHY DON'T YOU HANG YOURSELF!!!  ")

class UI():

    letter_board = LetterBoard()

    @classmethod
    def main(cls):
        while True:
            # Show Game Board
            cls.letter_board.show_word()
            # Ask for a letter
            letter = input("What letter would you like to guess? ").lower()

            # Tell User is the letter is on the board; if the guess was wrong take away a move
            cls.letter_board.guess_letter(letter)

            # Display the letter on the board /Show board again
            cls.letter_board.show_word()

            # Check make sure they didn't already solve the puzzle
            if cls.letter_board.check_if_all_letters_guessed():
                cls.letter_board.user_won()
                break
            # Let them guess a word
            word_guess = input("Would you like to guess the word? (Y/Yes) ".lower())
            if word_guess == "y" or word_guess =="yes":
                word = input("What is your guess for the word? ").lower()
                if cls.letter_board.guessed_word_correct(word):
                    cls.letter_board.user_won()
                    break
            # If user is out of moves Game Over
            if not cls.letter_board.has_guesses_left():
                cls.letter_board.user_lost()
                break
            # Repeat until solved using a while loop



if __name__ == "__main__":
    # Driver Code
    UI.main()