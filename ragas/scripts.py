
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

def populate_janya():
    janya_list = open('./janya_ragas.txt', 'r').readlines()
    formatted_list = []

    curr_raga_count = 73
    curr_melakartha_id = 0

    for raga in janya_list:
        if raga == '\n':
            continue
        attributes = raga.split('|')
        if len(attributes) == 2:
            curr_melakartha_id = attributes[0]
        else:
            pk = curr_raga_count
            name = attributes[0].strip()
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
                    "melakarta": int(curr_melakartha_id)
                }
            }
            formatted_list.append(ragaobj)
            curr_raga_count += 1

    format_file = open('./fixtures/janya_ragas.json', 'w')
    with format_file as fout:
        json.dump(formatted_list, fout)

    format_file.close

def populate_chords():
    chord_list = open('./chord_list.txt', 'r').readlines()
    chord_count = 1
    formatted_list = []

    for chord in chord_list:
        if chord == '\n':
            break
        attributes = chord.split('|')
        pk = chord_count
        name = attributes[0].strip()
        formula = attributes[1].strip()
        affix = attributes[2].strip()
        description = attributes[3].strip()
        chord_obj = {
            "model": "ragas.chord",
            "pk": pk,
            "fields": {
                "name": name,
                "formula": formula,
                "affix": affix,
                "description": description
            }
        }
        chord_count += 1
        formatted_list.append(chord_obj)

    format_file = open('./fixtures/chords.json', 'w')
    with format_file as fout:
        json.dump(formatted_list, fout)

    format_file.close


if __name__ == '__main__':
    # populate_melakarta()
    # populate_janya()
    populate_chords()
