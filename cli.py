import os
import argparse

from FileReader.FileOperator import FileOperator
from Translator.Translator import Translator


def validate_path(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid file path.")
    if not path.endswith('.pot'):
        raise argparse.ArgumentTypeError(f"'{path}' is not a POT file.")
    return path


def translate_and_save(path, lang):
    file = FileOperator(path)
    translator = Translator()

    for entry in file.pot_file:
        if entry.msgid:
            entry.msgstr = translator.translate(entry.msgid, lang)
        elif entry.msgid_plural:
            translated_plurals = {}
            for plural_key, plural_value in entry.msgid_plural.items():
                translated_plurals[plural_key] = translator.translate(plural_value, lang)
            entry.msgstr_plural = translated_plurals

    file.save(lang)


def main():
    parser = argparse.ArgumentParser(description='Translate a POT file and save it as a PO file.')
    parser.add_argument('--path', type=validate_path, required=True, help='Path to the POT file')
    parser.add_argument('--lang', required=True, help='Language code for translation (e.g., es, fr)')

    args = parser.parse_args()
    translate_and_save(args.path, args.lang)


if __name__ == '__main__':
    main()
