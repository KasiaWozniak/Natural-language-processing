import spacy
import textacy
import pandas as pd
from pypdf import PdfReader


def pdf_to_string(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# file_path = "Tolkien.pdf"
# pdf_text = pdf_to_string(file_path)
# print(pdf_text)

nlp = spacy.load("en_core_web_sm")

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

svo_list = list(textacy.extract.subject_verb_object_triples(doc))
vo_list = []
for svo in svo_list:
    v = svo[1][-1].lemma_
    objects = " ".join(str(x) for x in svo[2])
    o = list(nlp(objects).noun_chunks)[0].root.text
    vo_list.append((v, o))

for x in vo_list:
    print(x)

