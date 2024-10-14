import random

def random_noun():
    try:
        with open('nouns.txt', 'r', encoding='utf-8') as plik:
            noun = plik.readlines()
        if noun:
            losowa_linia = random.choice(noun).strip()
            return f"{losowa_linia}"
        else:
            return "Plik jest pusty."
    except FileNotFoundError:
        return f"Plik o nazwie nouns.txt nie został znaleziony."
    except Exception as e:
        return f"Wystąpił błąd: {e}"

noun = random_noun()
print(noun)


def random_verb():
    try:
        with open('verbs.txt', 'r', encoding='utf-8') as plik:
            verb = plik.readlines()
        if verb:
            losowa_linia = random.choice(verb).strip()
            return f"{losowa_linia}"
        else:
            return "Plik jest pusty."
    except FileNotFoundError:
        return f"Plik o nazwie verbs.txt nie został znaleziony."
    except Exception as e:
        return f"Wystąpił błąd: {e}"

verb = random_verb()
print(verb)


def random_adj():
    try:
        with open('adjectives.txt', 'r', encoding='utf-8') as plik:
            adj = plik.readlines()
        if adj:
            losowa_linia = random.choice(adj).strip()
            return f"{losowa_linia}"
        else:
            return "Plik jest pusty."
    except FileNotFoundError:
        return f"Plik o nazwie adjectives.txt nie został znaleziony."
    except Exception as e:
        return f"Wystąpił błąd: {e}"

adj = random_adj()
print(adj)
