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

def filter_words_by_difficulty(word_list, difficulty):
    if difficulty == "EASY":
        return [w for w in word_list if len(w) <= 6]
    elif difficulty == "MEDIUM":
        return [w for w in word_list if 7 <= len(w) <= 10]
    elif difficulty == "HARD":
        return [w for w in word_list if len(w) > 10]
    return word_list