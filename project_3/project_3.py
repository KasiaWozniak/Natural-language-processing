import spacy
import textacy

nlp = spacy.load("en_core_web_sm")

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

with open('Tolkien.txt', 'r', encoding="utf8") as file:
    text = file.read()

nlp.max_length = 2913402
doc = nlp(text)

svo_list = list(textacy.extract.subject_verb_object_triples(doc))
vo_list = []
for svo in svo_list:
    v = svo[1][-1].lemma_
    objects = " ".join(str(x) for x in svo[2])
    o = list(nlp(objects).noun_chunks)[0].root.text
    vo_list.append((v, o))

# vo_list.append(('start', 'game'))
for x in vo_list:
    print(x)

verbs_and_nouns = dict()
for v, o in vo_list:
    verbs_and_nouns.setdefault(v, []).append(o)
print(verbs_and_nouns)

with open('verbs_and_nouns.txt', 'w') as file:
    for v, o in verbs_and_nouns.items():
        o_string = ' '.join(o)
        file.write(f'{v}: {o_string}\n')
