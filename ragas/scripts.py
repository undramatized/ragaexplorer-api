
# Script to extract melakarta ragas from melakarta_list.py and populate database
import json, datetime

def format_name(name):
    clean_name = ""
    for c in name:
        if c.isalpha():
            clean_name += c.lower()
    return clean_name.capitalize()

def populate_melakarta():
    melakarta_list = open('./melakarta_ragas.txt', 'r').readlines()

    formatted_list = []
    for raga in melakarta_list:
        attributes = raga.split('|')
        pk = int(attributes[0].strip())
        name = attributes[1].strip()
        arohanam = attributes[2].strip()
        avarohanam = attributes[3].strip()
        ragaobj = {
            "model": "ragas.raga",
            "pk": pk,
            "fields": {
                "created": datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
                "name": name,
                "format_name": format_name(name),
                "arohanam": arohanam,
                "avarohanam": avarohanam,
                "melakarta": None
            }
        }

        formatted_list.append(ragaobj)

    format_file = open('./fixtures/melakarta_ragas.json', 'w')
    with format_file as fout:
        json.dump(formatted_list, fout)

    format_file.close


if __name__ == '__main__':
    populate_melakarta()
