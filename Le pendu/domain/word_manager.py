import unicodedata
import random

def load_raw_words(file_path):
    
    # Lit les mots bruts depuis un fichier .txt
    
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def clean_word(text):
    
    # Nettoie un mot :
    # - supprime les espaces et retours à la ligne
    # - transforme en minuscules
    # - supprime les accents
    
    text = text.strip().lower()
    normalized = unicodedata.normalize("NFD", text)
    without_accent = "".join(
        char for char in normalized
        if unicodedata.category(char) != "Mn"
    )
    return without_accent


def select_random_word(file_path="mots.txt"):
    
    # Sélectionne un mot aléatoire valide depuis le fichier mots.txt
    
    raw_words = load_raw_words(file_path)
    cleaned_words = []

    for word in raw_words:
        cleaned = clean_word(word)
        if "-" in cleaned or " " in cleaned:
            continue
        if cleaned.isalpha():
            cleaned_words.append(cleaned)

    if not cleaned_words:
        raise ValueError("Aucun mot valide trouvé dans la liste de mots")

    return random.choice(cleaned_words)


def append_new_word(word, file_path="mots.txt"):
    
    # Ajoute un nouveau mot valide dans le fichier mots.txt
    
    cleaned = clean_word(word)
    if cleaned.isalpha():
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(cleaned + "\n")
    else:
        raise ValueError("Le mot contient des caractères invalides")

      
         
