import polib
import os


class FileOperator:
    def __init__(self, path_of_pot_file):
        self.path_of_pot_file = path_of_pot_file
        self.pot_file = polib.pofile(path_of_pot_file)

    def save(self, lang):
        directory = os.path.dirname(self.path_of_pot_file)
        self.pot_file.save(f"{directory}/{lang}.po")
