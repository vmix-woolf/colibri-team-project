from collections import UserDict
import pickle
from assistant.note import Note
from messages.constants import Constants

class Notebook(UserDict):
    """Робота із нотатками"""
    def __init__(self, filename="notes.json"):
        super().__init__()
        self.filename = filename
        self.load_notes()  # Завантажуємо нотатки з файлу при ініціалізації

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
            for key, note in results.items():
                print(f"Found Note with key {key}:")
                print(note)
        else:
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
            for key, note in results.items():
                print(Constants.SEARCH_RESULTS.value)
                print(note)
        else:
            print(Constants.NOTE_NOT_FOUND.value)

    def sort_by_tag(self, tag):
        """Сортування нотаток за тегом"""
        sorted_notes = sorted(self.data.items(), key=lambda x: tag in x[1].tag)
        for key, note in sorted_notes:
            print(f"Note number {key}:")
            print(note)

    def load_notes(self):
        """Завантажує нотатки з файлу"""
        try:
            with open(self.filename, "rb") as f:
                notes_data = pickle.load(f)
                for key, note_data in notes_data.items():
                    self.data[int(key)] = Note.from_dict(note_data)
                print(f"Loaded {len(self.data)} notes from '{self.filename}'.")
        except FileNotFoundError:
            print(Constants.NO_NOTES_START_FRESH.value)

    def save_notes(self):
        """Зберігає нотатки у файл"""
        with open(self.filename, "wb") as f:
            notes_data = {key: note.to_dict() for key, note in self.data.items()}
            pickle.dump(notes_data, f, ensure_ascii=False, indent=4)
            print(Constants.NOTES_SAVED.value)

    def show_all_notes(self):
        """Вивести всі нотатки"""
        if not self.data:
            print(Constants.NO_NOTES_AVAILABLE.value)
        for key, note in self.data.items():
            print(f"Note number {key}:")
            print(note)  # Викликається метод __str__ класу Note
            print("-" * 40)  # Для розділення нотаток виведенням лінії