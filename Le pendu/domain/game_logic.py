import unicodedata


def is_valid_input(char):
   
   # Vérifie si l'entrée est une lettre valide   (a-z), 
    # en retirant les accents et normalisant Unicode.
    
    if not char or len(char) != 1:
        return False

    # Normalisation Unicode pour enlever les accents
    normalized = unicodedata.normalize("NFD", char.lower())
    clean_char = "".join(
        c for c in normalized
        if unicodedata.category(c) != "Mn"
    )

    # Vérifie si c'est une lettre alphabétique
    return clean_char.isalpha()


def check_letter(letter, secret_word):
    
    # Vérifie si la lettre est présente dans le mot secret.

    return letter in secret_word


def get_display_word(secret_word, found_letters):
    
    # Génère le mot affiché avec lettres trouvées et tirets
    # Exemple : "p _ n d _" pour "pendu"
    
    return " ".join([char if char in found_letters else "_" for char in secret_word])


def is_game_over(errors, max_attempts):
    
    # Détermine si la partie est perdue (nombre d'erreurs >= max_attempts)
    
    return errors >= max_attempts


def is_victory(secret_word, found_letters):
    
    # Détermine si toutes les lettres du mot
    
    return all(char in found_letters for char in secret_word)
