from ragas.helpers import chord_helper

SWARAS = ["S", "R1", "R2", "R3", "G1", "G2", "G3", "M1", "M2", "P", "D1", "D2", "D3", "N1", "N2", "N3"]

SWARA_INTERVALS = {
    'S'   : 0,
    'R1'  : 1,
    'R2'  : 2,
    'R3'  : 3,
    'G1'  : 2,
    'G2'  : 3,
    'G3'  : 4,
    'M1'  : 5,
    'M2'  : 6,
    'P'   : 7,
    'D1'  : 8,
    'D2'  : 9,
    'D3'  : 10,
    'N1'  : 9,
    'N2'  : 10,
    'N3'  : 11,
}

# Returns a list of semitone intervals that a list of swaras represent
# eg. [S, R2, G3, P, D2] => [0, 2, 4, 7, 9]
def get_semitones(swaras):
    semitones = []
    for swara in swaras:
        semitones.append(SWARA_INTERVALS[swara])

    return semitones

# Returns the western scale note for a swara, given a root note
# eg. R2 in the key D => E
def get_swara_note(swara, root):
    swara_semitone = SWARA_INTERVALS[swara]
    return chord_helper.semitone_to_note(swara_semitone, root)

# Returns a chord transposed to a particular swara's semitone position, to get it's relative position in a raaga
# eg. [0,4,7] for swara at 2 => [2,6,9]
def transpose_chord(swara_semi, chord_semi):
    transposed = []
    for note in chord_semi:
        transposed.append((note+swara_semi)%12)
    return transposed

# Arguments: All swaras, all chords, root note
# Returns a list of chords per swaras
# {
#   'S' : {'note': 'F', 'chord_ids': [1, 4, 7]},
#   'R2' : {'note': 'G', 'chord_ids': [3, 4, 5]}
# }

def get_chords_from_swaras(swaras, chords, root):
    swara_semitones = get_semitones(swaras)
    swara_semi_set = set(swara_semitones)
    swara_chords = {}

    for i in range(len(swaras)):
        note = get_swara_note(swaras[i], root)
        chords = []
        for chord in chords:
            chord_semitones = chord.get_semitones()
            transposed_semitones = transpose_chord(swara_semitones[i], chord_semitones)
            transposed_set = set(transposed_semitones)

            if transposed_set.issubset(swara_semi_set):
                chords.append(chord.id)
        swara_chord_obj = {
            'note': note,
            'chords': chords
        }
        swara_chords[swaras[i]] = swara_chord_obj

    return swara_chords




if __name__ == '__main__':
    swaras = ["S", "R1", "G2", "M1", "P", "D2", "N3"]
    # print get_swara_note("G1", "F")
