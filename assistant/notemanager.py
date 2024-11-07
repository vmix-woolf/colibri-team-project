from collections import UserDict
import json
from assistant.note import Note

class NoteManager(UserDict):
    """Робота із нотатками"""
    def __init__(self, filename="notes.json"):
        super().__init__()
        self.filename = filename
        self.load_notes()  # Завантажуємо нотатки з файлу при ініціалізації

    def add_note(self, title, content):
        """Додавання нової нотатки"""
        key = len(self.data) + 1  # Генерація унікального ключа
        self.data[key] = Note(title, content)  # Додаємо нотатку в словник
        print(f"Note '{title}' added with key {key}.")
        self.save_notes()  # Зберігаємо нотатки після зміни

    def search_text(self, text):
        """Пошук нотаток за текстом в content"""
        results = {key: note for key, note in self.data.items() if text.lower() in note.content.lower()}
        if results:
            for key, note in results.items():
                print(f"Found Note with key {key}:")
                print(note)
        else:
            print("No notes found with the given text.")

    def edit_note(self, key, title=None, content=None):
        """Редагування нотатки за її номером"""
        if key in self.data:
            self.data[key].edit(title, content)
            print(f"Note number {key} has been edited.")
            self.save_notes()  # Зберігаємо нотатки після зміни
        else:
            print(f"No note found number {key}.")

    def remove_note(self, key):
        """Видалення нотатки за її номером"""
        if key in self.data:
            del self.data[key]
            # Перерозподіл ключів
            self.data = {i+1: note for i, (key, note) in enumerate(sorted(self.data.items()))}
            print(f"Note with key {key} has been removed.")
            self.save_notes()  # Зберігаємо нотатки після зміни
        else:
            print(f"No note found with number {key}.")

    def add_tag_to_note(self, title, tag):
        """Додавання тегу до нотатки за заголовком"""
        for note in self.data.values():
            if note.title.lower() == title.lower():
                note.add_tag(tag)
                print(f"Tag '{tag}' added to note '{title}'.")
                self.save_notes()  # Зберігаємо нотатки після зміни
                return
        print(f"No note found with title '{title}'.")

    def search_by_tag(self, tag):
        """Пошук нотаток за тегом"""
        results = {key: note for key, note in self.data.items() if tag in note.tag}
        if results:
            for key, note in results.items():
                print(f"Found Note number {key}:")
                print(note)
        else:
            print(f"No notes found with tag '{tag}'.")

    def sort_by_tag(self, tag):
        """Сортування нотаток за тегом"""
        sorted_notes = sorted(self.data.items(), key=lambda x: tag in x[1].tag)
        for key, note in sorted_notes:
            print(f"Note number {key}:")
            print(note)

    def load_notes(self):
        """Завантажує нотатки з файлу"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                notes_data = json.load(f)
                for key, note_data in notes_data.items():
                    self.data[int(key)] = Note.from_dict(note_data)
                print(f"Loaded {len(self.data)} notes from '{self.filename}'.")
        except FileNotFoundError:
            print("No existing notes found, starting fresh.")

    def save_notes(self):
        """Зберігає нотатки у файл"""
        with open(self.filename, "w", encoding="utf-8") as f:
            notes_data = {key: note.to_dict() for key, note in self.data.items()}
            json.dump(notes_data, f, ensure_ascii=False, indent=4)
            print(f"Notes saved to '{self.filename}'.")

    def show_all_notes(self):
        """Вивести всі нотатки"""
        if not self.data:
            print("No notes available.")
        else:
            for key, note in self.data.items():
                print(f"Note number {key}:")
                print(note)  # Викликається метод __str__ класу Note
                print("-" * 40)  # Для розділення нотаток виведенням лінії