import json
from flask import render_template, Blueprint, request, redirect, url_for
from project_2.website.services.generate_subject import *
from project_2.website.services.generate_verb import generate_verb

views = Blueprint('views', __name__)


@views.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        pronoun = request.form.get("pronoun_or_article")
        number = request.form.get("number")
        tense = request.form.get("tense")

        if request.form.get("noun_phrase") == "true":
            noun = True
        else:
            noun = False

        if request.form.get("adjective") == "true":
            adjective = True
        else:
            adjective = False

        arguments = {"pronoun_or_article": pronoun,
                     "adjective": adjective,
                     "number": number,
                     "noun": noun,
                     "tense": tense}
        print(arguments)

        return redirect(url_for('views.sentence', arguments=json.dumps(arguments)))

    return render_template('page.html')


@views.route('/sentence/<arguments>')
def sentence(arguments):
    arguments = json.loads(arguments)
    print(arguments)

    subject = generate_subject(arguments)
    sentence = generate_verb(subject, arguments["tense"], arguments["number"], arguments["pronoun_or_article"], arguments["noun"])

    return render_template('display.html', sentence=sentence)
