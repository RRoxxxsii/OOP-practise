class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        return *self._notes, '\n'




