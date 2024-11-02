import spacy
import textacy
import pandas as pd
from pypdf import PdfReader

def pdf_to_text_file(file_path, output_path):
    reader = PdfReader(file_path)
    with open(output_path, "w", encoding="utf-8") as output_file:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                output_file.write(text)

file_path = "Tolkien.pdf"
output_path = "Tolkien.txt"
pdf_to_text_file(file_path, output_path)

print("Text successfully saved to", output_path)


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

