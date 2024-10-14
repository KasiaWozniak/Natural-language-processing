from project_2.website.services.choose_random_word import *


def generate_subject(arguments):
    if arguments["noun"]:
        noun = random_noun()
        adjective = random_adjective()
        article = arguments["pronoun_or_article"]
        if article == "indefinite_article":
            if arguments["adjective"]:
                article = get_article(adjective)
            else:
                article = get_article(noun)
        if arguments["adjective"]:
            subject = f'{article} {adjective} {noun}'
        else:
            subject = f'{article} {noun}'

    else:
        subject = arguments["pronoun_or_article"]

    return subject


def get_article(word):
    if word[0] in ('a', 'o', 'e', 'i', 'u', 'y'):
        return "An"
    else:
        return "A"
