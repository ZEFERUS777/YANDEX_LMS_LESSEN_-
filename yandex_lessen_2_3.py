PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, pitch_note, duration=False):
        self.pitch_note = pitch_note
        self.duration = duration  # True if duration is not None

    def __str__(self):
        if self.duration:  # Можно сократить условие
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
        else:
            return self.pitch_note


class LoudNote(Note):
    def __init__(self, pitch_note):
        self.pitch_note = pitch_note

    def __str__(self):
        return self.pitch_note.upper()


class DefaultNote(Note):
    def __init__(self, pitch_note='до', duration=False):
        self.pitch_note = pitch_note
        self.duration = duration
        super().__str__()
