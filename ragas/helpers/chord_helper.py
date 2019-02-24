import re

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

# Converts the chord formula interval to semitones from root
# ie. b3 => 3
def get_semitone(interval):
    if interval[0] == '(':
        return get_semitone(interval[1:-1])
    elif interval.isdigit():
        return NOTE_INTERVALS[interval]
    else:
        feature_strip = re.sub(r'\d+', '', interval)
        int_strip = re.sub(r'\D+', '', interval)
        print interval, feature_strip, int_strip
        feature = NOTE_FEATURES[feature_strip]
        semitones = NOTE_INTERVALS[int_strip]
        return semitones+feature

# Converts the chord formula interval to semitones from root, including omitted detail
# ie. b3 => [3, False]
def get_semitone_with_omitted(interval, omitted=False):
    if interval[0] == '(':
        return get_semitone_with_omitted(interval[1:-1], True)
    elif len(interval) == 1:
        return [NOTE_INTERVALS[interval], omitted]
    else:
        feature = NOTE_FEATURES[interval[:-1]]
        semitones = NOTE_INTERVALS[interval[len(interval)-1]]
        return [semitones+feature, omitted]

# Converts single semitone to a note, given a root note
def semitone_to_note(semitone, root):
    root_index = NOTES.index(root)
    note_index = root_index + semitone
    note = NOTES[note_index%12]
    return note

# Converts semitones to notes, given a root note
def semitones_to_notes(semitones, root):
    root_index = NOTES.index(root)
    notes = []
    for semitone in semitones:
        note_index = root_index + semitone[0]
        note = NOTES[note_index%12]
        notes.append({'note': note, 'omitted': semitone[1]})
    return notes

# Takes a Major chord, eg. '1 3 5' interval formula
# Takes root note eg. F

# Identify '1 3 5' intervals as [0, 4, 7] semitones
# Identify [0, 4, 7] as ['F', 'A', 'C']

# Returns [{'note': 'F', 'omitted': False}, {'note': 'A', 'omitted': False}, {'note': 'C', 'omitted': False}]
def get_chord_notes(chord, root):
    # '1 b3 5' => ['1', 'b3', '5']
    chord_formula = chord.formula.split()
    semitone_interval = []

    for note in chord_formula:
        semitones = get_semitone_with_omitted(note)
        semitone_interval.append(semitones)

    return semitones_to_notes(semitone_interval, root)

def get_chord_semitones(chord):
    # '1 b3 5' => ['1', 'b3', '5']
    chord_formula = chord.formula.split()
    semitones = []

    for note in chord_formula:
        semitone = get_semitone(note)
        semitones.append(semitone)

    return semitones

if __name__ == '__main__':
    chord = {
        'name': 'Major',
        'formula': '1 b3 5 b7 9',
        'affix': 'maj'
    }

    # print get_chord_notes(chord, 'F')
