hangman_art = {0: ("   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}


def display_man(wrong_guesses):
    print("----------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))