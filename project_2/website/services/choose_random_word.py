import random


def random_noun():
    try:
        with open('website/services/words/nouns.txt', 'r', encoding='utf-8') as plik:
            noun = plik.readlines()
        if noun:
            losowa_linia = random.choice(noun).strip()
            return f"{losowa_linia}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"


def random_verb():
    try:
        with open('website/services/words/verbs.txt', 'r', encoding='utf-8') as plik:
            verb = plik.readlines()
        if verb:
            losowa_linia = random.choice(verb).strip()
            return f"{losowa_linia}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"


def random_adjective():
    try:
        with open('website/services/words/adjectives.txt', 'r', encoding='utf-8') as plik:
            adj = plik.readlines()
        if adj:
            losowa_linia = random.choice(adj).strip()
            return f"{losowa_linia}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"
