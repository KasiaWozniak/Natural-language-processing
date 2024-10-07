import csv
import string
from string import digits
import codecs
from prettytable import PrettyTable
from pypdf import PdfReader


def prepare_words(text):
    text = " ".join(text.split())
    text = text.translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', digits))

    words = "".join(list([val for val in text if val.isalpha() or val in ('’', ' ')]))
    return words.lower().split()


def zipf_to_csv(sorted_dict):
    data_csv = []
    for rank, (word, count) in enumerate(sorted_dict.items()):
        zipf = (rank + 1) * count
        row = {'word': word, 'rank': rank + 1, 'count': count, 'constant': zipf}
        data_csv.append(row)

    with open('results/prawo_zipfa.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'rank', 'count', 'constant']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_csv)


def zipf_to_txt(sorted_dict):
    data = []
    for rank, (word, count) in enumerate(sorted_dict.items()):
        zipf = (rank + 1) * count
        # print('{:>15}'.format(rank + 1), '{:>15}'.format(word), '{:>15}'.format(count), '{:>15}'.format(zipf))
        row = [word, rank + 1, count, zipf]
        data.append(row)

    table = PrettyTable()
    table.title = 'Zipf\'s law'
    table.field_names = ['word', 'rank', 'count', 'constant']
    table.add_rows(data)
    with open('results/prawo_zipfa.txt', 'w', encoding='utf-8') as outputfile:
        outputfile.write(str(table))


def most_popular_words(sorted_dict, percent):
    words_amount = sum(sorted_dict.values())
    current_amount = 0
    words = []

    for word, count in sorted_dict.items():
        current_amount += count
        words.append(word)
        if current_amount / words_amount >= percent:
            break

    return words


def write_popular_words_to_file(sorted_dict, percent):
    words = most_popular_words(sorted_dict, percent)

    with open('results/most_popular_words.txt', 'a+', encoding='utf-8') as file:
        file.write(f"Słowa potrzebne, aby zrozumieć {percent * 100}% tekstu w języku francuskim:\n")
        for word in words:
            file.write(f"{word}\n")


def words_connection(text):
    words_for_connection = "".join(list([val for val in text if val.isalpha() or val in ('’', ' ', '.')]))
    words_for_connection = words_for_connection.lower().split()
    dict_connection = {}

    for index, current_word in enumerate(words_for_connection):
        if index == len(words_for_connection) - 1:
            break
        if '.' in current_word:
            continue

        word_to_add = words_for_connection[index + 1].replace('.', '')
        if dict_connection.get(current_word):
            dict_connection[current_word].add(word_to_add)
        else:
            dict_connection[current_word] = {word_to_add}

        if dict_connection.get(word_to_add):
            dict_connection[word_to_add].add(current_word)
        else:
            dict_connection[word_to_add] = {current_word}

    sorted_dict_connection = dict(sorted(dict_connection.items(), key=lambda item: len(item[1]), reverse=True))
    with open('results/rdzenie.txt', 'w', encoding='utf-8') as file:
        for word, connections in sorted_dict_connection.items():
            # print(f'{word}: {connections}')
            file.write(f'{word}: {len(connections)}\n{connections}\n')


if __name__ == '__main__':
    # read text from files
    with codecs.open(r'resources/source1.txt', encoding='utf-8') as file1:
        text = file1.read()

    reader = PdfReader('resources/source2.pdf')
    for page in reader.pages:
        text += " "
        text += page.extract_text()

    words = prepare_words(text)

    # ranking of words
    dictionary = {}
    for current_word in words:
        if dictionary.get(current_word):
            dictionary[current_word] += 1
        else:
            dictionary[current_word] = 1

    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    # Zipf's law
    zipf_to_txt(sorted_dict)
    zipf_to_csv(sorted_dict)

    # Most popular words
    write_popular_words_to_file(sorted_dict, 0.1)
    write_popular_words_to_file(sorted_dict, 0.2)
    write_popular_words_to_file(sorted_dict, 0.3)
    write_popular_words_to_file(sorted_dict, 0.4)
    write_popular_words_to_file(sorted_dict, 0.5)

    # The most connected words
    words_connection(text)
