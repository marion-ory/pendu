from ui import drawer
from domain import word_manager

def main():
    answer = word_manager.word_choice()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        drawer.display_man(wrong_guesses)
        drawer.display_hint(hint)
        guess = input("Enter a letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input , only one letter")
            continue

        if guess in guessed_letters :
            print(f'{guess} is already guessed')
            continue

        guessed_letters.add(guess)    

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else :
            wrong_guesses += 1


        if "_" not in hint :
            drawer.display_man(wrong_guesses)
            drawer.display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(drawer.hangman_art) - 1:
            drawer.display_man(wrong_guesses)
            drawer.display_answer(answer)
            print("YOU LOSE")
            is_running = False

if __name__ == "__main__":
    main()