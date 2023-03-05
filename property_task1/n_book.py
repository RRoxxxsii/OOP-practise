class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        yield *self._notes, '\n'




