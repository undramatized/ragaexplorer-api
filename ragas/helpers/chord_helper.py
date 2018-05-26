NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

NOTE_INTERVALS = {
    '1'  : 0,
    '2'  : 2,
    '3'  : 4,
    '4'  : 5,
    '5'  : 7,
    '6'  : 9,
    '7'  : 11,
    '8'  : 12,
    '9'  : 14,
    '10' : 16,
    '11' : 17,
    '12' : 19,
    '13' : 21,
    '14' : 23,
    '15' : 24,
}

NOTE_FEATURES = {
    'bb' : -2,
    'b'  : -1,
    '#'  : 1,
    '()' : "omitted",
}

def get_semitones(interval, omitted=False):
    if interval[0] == '(':
        return get_semitones(interval[1:-1], True)
    elif len(interval) == 1:
        return [NOTE_INTERVALS[interval], omitted]
    else:
        feature = NOTE_FEATURES[interval[:-1]]
        semitones = NOTE_INTERVALS[interval[len(interval)-1]]
        return [semitones+feature, omitted]

def semitones_to_notes(semitones, root):
    root_index = NOTES.index(root)
    notes = []
    for semitone in semitones:
        note_index = root_index + semitone[0]
        note = NOTES[note_index%12]
        notes.append({'note': note, 'omitted': semitone[1]})
    return notes

# Given a Major chord, with '1 3 5' interval formula
# Given root note as F

# Identify '1 3 5' intervals as [0, 4, 7] semitones
# Identify [0, 4, 7] as ['F', 'A', 'C']

# Returns ['F', 'A', 'C']
def get_chord_notes(chord, root):
    # '1 b3 5' => ['1', 'b3', '5']
    chord_formula = chord.formula.split()
    semitone_interval = []

    for note in chord_formula:
        semitones = get_semitones(note)
        semitone_interval.append(semitones)

    return semitones_to_notes(semitone_interval, root)


if __name__ == '__main__':
    chord = {
        'name': 'Major',
        'formula': '1 b3 5 b7 9',
        'affix': 'maj'
    }

    # print get_chord_notes(chord, 'F')
