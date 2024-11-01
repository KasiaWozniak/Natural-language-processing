from project_2.website.services.choose_random_word import random_verb, random_verb_2, random_verb_3


def generate_verb(subject, tense, number, pronoun, noun, complement):
    verb = random_verb()

    if tense == "present_simple":
        verb = make_verb_simple(random_verb(), is_third_person(number, pronoun, noun))
    elif tense == "present_continuous":
        verb = make_verb_continuous(random_verb(), get_be(pronoun, noun))
    elif tense == "present_perfect":
        verb = make_verb_perfect(random_verb_3(), is_third_person(number, pronoun, noun))
    elif tense == "present_perfect_continuous":
        verb = make_verb_perfect_continuous(random_verb(), is_third_person(number, pronoun, noun))

    return f"{subject.capitalize()} {verb} {complement}."


def make_verb_simple(verb, third_person):
    if " " in verb:
        verb, addition = verb.split(" ")
    else:
        addition = None
    if third_person:
        if verb[-1] == "y":
            verb = verb[0:-1] + "ies"
        verb += "s"
    if addition:
        return f'{verb} {addition}'
    return verb


def make_verb_continuous(verb, be):
    verb, addition = get_ing(verb)

    if addition:
        return f'{be} {verb} {addition}'
    return f'{be} {verb}'


def make_verb_perfect(verb, third_person):
    have = get_have(third_person)
    return f"{have} {verb}"


def make_verb_perfect_continuous(verb, third_person):
    have = get_have(third_person)
    verb, addition = get_ing(verb)

    if addition:
        return f"{have} been {verb} {addition}"
    return f"{have} been {verb}"


def is_third_person(number, pronoun, noun):
    if number == "singular":
        if pronoun in ("he", "she", "it", "this", "that") or noun:
            return True
    return False


def get_be(pronoun, noun):
    if pronoun == "I":
        return "am"
    if pronoun in ("he", "she", "it", "this", "that") or noun:
        return "is"
    else:
        return "are"


def get_have(third_person):
    if third_person:
        return "has"
    else:
        return "have"


def get_ing(verb):
    if " " in verb:
        verb, addition = verb.split(" ")
    else:
        addition = None
    if verb[-1] == "e":
        verb = verb[0:-1] + "ing"
    else:
        verb += "ing"
    return verb, addition
