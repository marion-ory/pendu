import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def check_letter(letter_typed, word_to_guess, found_letters):
    if letter_typed in word_to_guess:
        if letter_typed not in found_letters:
            found_letters.append(letter_typed)
            return True
    return False

def display_word(word_to_guess, found_letters):
    result = ""
    for letter in word_to_guess:
        if letter in found_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()

def get_difficulty(word_to_guess):
    length = len(word_to_guess)
    if length <= 6: return "Easy", 5
    elif 6 < length < 12: return "Medium", 10
    else: return "Hard", 15