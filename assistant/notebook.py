import pickle
import os
from prettytable import PrettyTable
from collections import UserDict

from assistant.note import Note
from messages.constants import Constants

class Notebook(UserDict):
    def __init__(self, filename="notes.pkl"):
        super().__init__()
        self.filename = filename
        self.load_notes()

    def add_note(self, title, content):
        key = len(self.data) + 1  # unique key generation
        self.data[key] = Note(title, content)
        self.save_notes()

    def search_text(self, text):
        results = {key: note for key, note in self.data.items() if text.lower() in note.content.lower()}

        if results:
            table = PrettyTable()
            table.field_names = ["Key", "Title", "Content", "Tags"]
            for key, note in results.items():
                table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
            return table
        else:
            return Constants.NO_NOTES_FOUND.value

    def edit_note(self, key, title=None, content=None):
        if key in self.data:
            self.data[key].edit(title, content)
            self.save_notes()
        else:
            return(f"No note found with number {key}.")

    def remove_note(self, key):
        if key in self.data:
            del self.data[key]
            # key reallocation
            self.data = {i+1: note for i, (key, note) in enumerate(sorted(self.data.items()))}
            self.save_notes()

        return Constants.NOTE_NOT_FOUND.value

    def add_tag_to_note(self, title, tag):
        for note in self.data.values():
            if note.title.lower() == title.lower():
                note.add_tag(tag)
                print(Constants.TAG_ADDED_TO_NOTE.value)
                self.save_notes()
                return
        print(Constants.NOTE_NOT_FOUND.value)

    def search_by_tag(self, tag):
        results = {key: note for key, note in self.data.items() if tag in note.tag}

        if results:
            table = PrettyTable()
            table.field_names = ["Key", "Title", "Content", "Tags"]
            for key, note in results.items():
                table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
            return table
        else:
            return Constants.NOTE_NOT_FOUND.value

    def sort_by_tag(self, tag):
        sorted_notes = sorted(self.data.items(), key=lambda x: tag in x[1].tag)
        table = PrettyTable()
        table.field_names = ["Key", "Title", "Content", "Tags"]

        for key, note in sorted_notes:
            table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
        print(table)

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                notes_data = pickle.load(f)
                for key, note_data in notes_data.items():
                    self.data[int(key)] = Note.from_dict(note_data)

    def save_notes(self):
        with open(self.filename, "wb") as f:
            notes_data = {key: note.to_dict() for key, note in self.data.items()}
            pickle.dump(notes_data, f)
            print(Constants.NOTES_SAVED.value)

    def show_all_notes(self):
        if not self.data:
            return Constants.NO_NOTES_AVAILABLE.value

        table = PrettyTable()
        table.field_names = ["Key", "Title", "Content", "Tags"]

        for key, note in self.data.items():
            table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])

        return table