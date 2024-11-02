import spacy
import textacy

nlp = spacy.load("en_core_web_sm")

with open('Tolkien.txt', 'r', encoding="utf8") as file:
    text = file.read()

nlp.max_length = 2913402
doc = nlp(text)

svo_list = list(textacy.extract.subject_verb_object_triples(doc))
vo_list = []
for svo in svo_list:
    v = svo[1][-1].lemma_
    objects = " ".join(str(x) for x in svo[2])
    o_list = list(nlp(objects).noun_chunks)
    if len(o_list) > 0:
        o = o_list[0].root.text
        vo_list.append((v, o))

verbs_and_nouns = dict()
for v, o in vo_list:
    verbs_and_nouns.setdefault(v, []).append(o)

with open('verbs_and_nouns.txt', 'w', encoding="utf8") as file:
    for v, o in verbs_and_nouns.items():
        o_string = ' '.join(o)
        file.write(f'{v}: {o_string}\n')
