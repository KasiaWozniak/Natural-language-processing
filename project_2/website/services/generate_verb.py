from project_2.website.services.choose_random_word import random_verb


def generate_verb(subject, tense, number, pronoun, noun):
    verb = random_verb()

    if tense == "present_simple":
        verb = make_verb_simple(verb, is_third_person(number, pronoun, noun))
    elif tense == "present_continuous":
        verb = make_verb_continuous(verb, get_be(pronoun, noun))
    # elif tense == "present_perfect":
    #     verb = make_verb_perfect(verb)
    return f"{subject} {verb}"


def make_verb_simple(verb, third_person):
    if third_person:
            if verb[-1] == "y":
                return verb[0:-1] + "ies"
            return verb + "s"
    return verb


def make_verb_continuous(verb, be):
    if verb[-1] == "e":
        return be + " " + verb[0:-1] + "ing"
    else:
        return be + " " + verb + "ing"


# def make_verb_perfect(verb, third_person):


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
