PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, pitch_note, duration=False, octave=None):
        self.pitch_note = pitch_note
        self.octave = octave
        self.is_long = duration
        self.octave = octave

    def __str__(self):
        if self.is_long:  # Можно сократить условие
            if self.pitch_note == 'до':
                return f'{self.pitch_note}-о'
            elif self.pitch_note == 'ре':
                return f'{self.pitch_note}-Э'
            elif self.pitch_note == 'ми':
                return f'{self.pitch_note}-и'
            elif self.pitch_note == 'фа':
                return f'{self.pitch_note}-а'
            elif self.pitch_note == 'ля':
                return f'{self.pitch_note}-а'
            elif self.pitch_note == 'си':
                return f'{self.pitch_note}-и'
            elif self.pitch_note == 'соль':
                return f'{self.pitch_note[:1]}-оль'
            else:
                return f'{self.pitch_note}-{self.pitch_note[-1]}'
        elif self.octave != None and self.is_long:
            if self.pitch_note == 'до':
                return f'{self.pitch_note}-о ({self.octave})'
            elif self.pitch_note == 'ре':
                return f'{self.pitch_note}-э {self.octave}'
            elif self.pitch_note == 'ми':
                return f'{self.pitch_note}-и ({self.octave})'
            elif self.pitch_note == 'фа':
                return f'{self.pitch_note}-а ({self.octave})'
            elif self.pitch_note == 'ля':
                return f'{self.pitch_note}-а ({self.octave})'
            elif self.pitch_note == 'си':
                return f'{self.pitch_note}-и ({self.ocatve})'
            elif self.pitch_note == 'соль':
                return f'{self.pitch_note[:1]}-оль ({self.octave})'
            else:
                return f'{self.pitch_note}-{self.pitch_note[-1]}'
        else:
            return self.pitch_note


class LoudNote(Note):
    def __init__(self, pitch_note, is_long=False):
        self.pitch_note = pitch_note
        self.is_long = is_long
        super().__str__

    def __str__(self):
        return self.pitch_note.upper()


class DefaultNote(Note):
    def __init__(self, pitch_note='до', is_long=False):
        self.octave = None
        self.pitch_note = pitch_note
        self.is_long = is_long
        super().__str__


class NoteWithOctave(Note):
    def __init__(self, pitch_note, octave, is_long=False):
        self.pitch_note = pitch_note
        self.is_long = is_long
        self.octave = octave
        super().__str__()


print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))


