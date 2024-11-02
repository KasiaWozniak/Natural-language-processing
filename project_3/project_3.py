import spacy
import textacy
import json

nlp = spacy.load("en_core_web_sm")

with open('Tolkien.txt', 'r') as file:
    text = file.read()
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

with open('file.txt', 'w') as file:
    file.write(json.dumps(verbs_and_nouns))
