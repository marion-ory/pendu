from ui.constants import SCORES_FILE_PATH

def save_player_score(name, score):
    """
    Sauvegarde le score du joueur dans scores.txt
    Args:
        name (str): Nom du joueur
        score (int): Score à sauvegarder
    """
    try:
        with open(SCORES_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"{name};{score}\n")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du score : {e}")


def load_top_scores(top_n=5):
    """
    Charge les scores depuis scores.txt et retourne les top_n meilleurs.
    Args:
        top_n (int): Nombre de scores à retourner (défaut 5)
    Returns:
        List[Tuple[str, int]]: Liste de tuples (nom, score)
    """
    scores = []

    try:
        with open(SCORES_FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if ";" not in line:
                    continue
                name, score_str = line.split(";")
                try:
                    score = int(score_str)
                    scores.append((name, score))
                except ValueError:
                    continue  # ignore les lignes corrompues
    except FileNotFoundError:
        # Si le fichier n'existe pas encore, renvoyer une liste vide
        return []

    # Trier par score décroissant
    scores.sort(key=lambda x: x[1], reverse=True)

    # Retourner uniquement les top_n scores
    return scores[:top_n]

