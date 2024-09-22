class Note:
    def __init__(self, pitch_note, dureation=False):
        self.pitch_note = pitch_note
        self.dureation = dureation  # True if dureation is not None

    def __str__(self):
        if self.dureation == True:
            if self.pitch_note == 'до':
                return self.pitch_note + '-о'
            elif self.pitch_note == 'ре':
                return self.pitch_note + '-Э'
            elif self.pitch_note == 'ми':
                return self.pitch_note + '-и'
            elif self.pitch_note == 'фа':
                return self.pitch_note + '-а'
            elif self.pitch_note == 'ля':
                return self.pitch_note + '-а'
            elif self.pitch_note == 'си':
                return self.pitch_note + '-и'
        else:
            return self.pitch_note
