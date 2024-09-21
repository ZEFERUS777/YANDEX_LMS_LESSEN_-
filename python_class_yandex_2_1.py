class Note:
    def __init__(self, pitch_note):
        self.pitch_note = pitch_note

    def play(self):
        print(self.pitch_note)