from project_2.website.services.choose_random_word import random_verb, random_verb_2, random_verb_3


def generate_verb(subject, tense, number, mood, question, pronoun, noun, complement):
    verb = random_verb()

    if tense == "present_simple":
        verb = make_verb_simple(random_verb(), is_third_person(number, pronoun, noun), mood)
    elif tense == "present_continuous":
        verb = make_verb_continuous(random_verb(), get_be(pronoun, noun), mood)
    elif tense == "present_perfect":
        verb = make_verb_perfect(random_verb_3(), get_have(is_third_person(number, pronoun, noun)), mood)
    elif tense == "present_perfect_continuous":
        verb = make_verb_perfect_continuous(random_verb(), get_have(is_third_person(number, pronoun, noun)), mood)
    elif tense == "past_simple":
        verb = make_verb_past(mood)
    elif tense == "past_continuous":
        verb = make_verb_continuous(random_verb(), get_be_2(pronoun, noun), mood)
    elif tense == "past_perfect":
        verb = make_verb_perfect(random_verb_3(), "had", mood)
    elif tense == "past_perfect_continuous":
        verb = make_verb_perfect_continuous(random_verb(), "had", mood)
    elif tense == "future_simple":
        verb = make_verb_future(random_verb(), mood)
    elif tense == "future_continuous":
        verb = make_verb_future(make_verb_continuous(random_verb(), "be", True), mood)
    elif tense == "future_perfect":
        verb = make_verb_future(make_verb_perfect(random_verb_3(), "have", True), mood)
    elif tense == "future_perfect_continuous":
        verb = make_verb_future(make_verb_perfect_continuous(random_verb(), "have", True), mood)

    return f"{subject.capitalize()} {verb} {complement}."


def make_verb_simple(verb, third_person, mood):
    if not mood:
        if third_person:
            return f'does not {verb}'
        else:
            return f'do not {verb}'

    if " " in verb:
        verb, addition = verb.split(" ")
    else:
        addition = None
    if third_person:
        if verb[-1] == "y":
            verb = verb[0:-1] + "ies"
        elif verb[-1] in ("s", "z", "x", "o") or verb[len(verb) - 2:] in ("sh", "ch"):
            verb += "es"
        else:
            verb += "s"
    if addition:
        return f'{verb} {addition}'
    return verb


def make_verb_continuous(verb, be, mood):
    verb, addition = get_ing(verb)

    if not mood:
        sentence = f'{be} not {verb}'
    else:
        sentence = f'{be} {verb}'
    if addition:
        return sentence + f' {addition}'
    return sentence


def make_verb_perfect(verb, have, mood):
    if not mood:
        return f"{have} not {verb}"
    return f"{have} {verb}"


def make_verb_perfect_continuous(verb, have, mood):
    verb, addition = get_ing(verb)
    if not mood:
        sentence = f"{have} not been {verb}"
    else:
        sentence = f"{have} been {verb}"

    if addition:
        return sentence + f' {addition}'
    return sentence


def make_verb_past_continuous(verb, third_person):
    have = get_have(third_person)
    verb, addition = get_ing(verb)

    if addition:
        return f"{have} been {verb} {addition}"
    return f"{have} been {verb}"


def make_verb_past(mood):
    if not mood:
        return f"did not {random_verb()}"
    return random_verb_2()


def make_verb_future(verb, mood):
    if not mood:
        return f"will not {verb}"
    return f"will {verb}"


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


def get_be_2(pronoun, noun):
    if pronoun in ("I", "he", "she", "it", "this", "that") or noun:
        return "was"
    else:
        return "were"


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
