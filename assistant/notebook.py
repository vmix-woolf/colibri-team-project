from collections import UserDict
import pickle
from assistant.note import Note
from messages.constants import Constants
import os
from prettytable import PrettyTable

class Notebook(UserDict):
    """Робота із нотатками"""
    def __init__(self, filename="notes.pkl"):
        super().__init__()
        self.filename = filename
        self.load_notes()

    def add_note(self, title, content):
        """Додавання нової нотатки"""
        key = len(self.data) + 1  # Генерація унікального ключа
        self.data[key] = Note(title, content)  # Додаємо нотатку в словник
        print(Constants.NOTE_ADDED.value)
        self.save_notes()  # Зберігаємо нотатки після зміни

    def search_text(self, text):
        """Пошук нотаток за текстом в content"""
        results = {key: note for key, note in self.data.items() if text.lower() in note.content.lower()}
        if results:
            table = PrettyTable()
            table.field_names = ["Key", "Title", "Content", "Tags"]
            for key, note in results.items():
                table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
            print(table)

        print(Constants.NO_NOTES_FOUND.value)

    def edit_note(self, key, title=None, content=None):
        """Редагування нотатки за її номером"""
        if key in self.data:
            self.data[key].edit(title, content)
            print(Constants.NOTE_NUM_EDITED.value)
            self.save_notes()  # Зберігаємо нотатки після зміни
        else:
            print(f"No note found with number {key}.")

    def remove_note(self, key):
        """Видалення нотатки за її номером"""
        if key in self.data:
            del self.data[key]
            # Перерозподіл ключів
            self.data = {i+1: note for i, (key, note) in enumerate(sorted(self.data.items()))}
            print(Constants.NOTE_REMOVED.value)
            self.save_notes()  # Зберігаємо нотатки після зміни
        else:
            print(Constants.NOTE_NOT_FOUND.value)

    def add_tag_to_note(self, title, tag):
        """Додавання тегу до нотатки за заголовком"""
        for note in self.data.values():
            if note.title.lower() == title.lower():
                note.add_tag(tag)
                print(Constants.TAG_ADDED_TO_NOTE.value)
                self.save_notes()  # Зберігаємо нотатки після зміни
                return
        print(Constants.NOTE_NOT_FOUND.value)

    def search_by_tag(self, tag):
        """Пошук нотаток за тегом"""
        results = {key: note for key, note in self.data.items() if tag in note.tag}
        if results:
            table = PrettyTable()
            table.field_names = ["Key", "Title", "Content", "Tags"]
            for key, note in results.items():
                table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
            print(table)
        else:
            print(Constants.NOTE_NOT_FOUND.value)

    def sort_by_tag(self, tag):
        """Сортування нотаток за тегом"""
        sorted_notes = sorted(self.data.items(), key=lambda x: tag in x[1].tag)
        table = PrettyTable()
        table.field_names = ["Key", "Title", "Content", "Tags"]
        for key, note in sorted_notes:
            table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])
        print(table)

    def load_notes(self):
        """Завантажує нотатки з файлу"""
        if os.path.exists(self.filename): 
            with open(self.filename, "rb") as f:
                notes_data = pickle.load(f)
                for key, note_data in notes_data.items():
                    self.data[int(key)] = Note.from_dict(note_data)
        print("Previous file not found, creating new one")

    def save_notes(self):
        """Зберігає нотатки у файл"""
        with open(self.filename, "wb") as f:
            notes_data = {key: note.to_dict() for key, note in self.data.items()}
            pickle.dump(notes_data, f)
            print(Constants.NOTES_SAVED.value)

    def show_all_notes(self):
        """Вивести всі нотатки"""
        if not self.data:
            print(Constants.NO_NOTES_AVAILABLE.value)
            return
        
        table = PrettyTable()
        table.field_names = ["Key", "Title", "Content", "Tags"]

        for key, note in self.data.items():
            table.add_row([key, note.title, note.content, ", ".join(note.tag) if note.tag else "No tags"])

        print(table)