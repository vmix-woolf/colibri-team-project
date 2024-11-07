class Note:
    """Клас для створення об'єкту записки"""
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.tag = set()  # Порожня множина для тегів

    def __str__(self):
        # Перевизначення методу str для красивого виведення
        return f"Title: {self.title}\nContent: {self.content}\nTags: {', '.join(self.tag) if self.tag else 'No tags'}"

    def add_tag(self, tag):
        """Додавання тегу до нотатки"""
        self.tag.add(tag)

    def edit(self, title=None, content=None):
        """Редагування нотатки"""
        if title:
            self.title = title
        if content:
            self.content = content

    def to_dict(self):
        """Конвертує нотатку в словник для серіалізації в JSON"""
        return {
            "title": self.title,
            "content": self.content,
            "tag": list(self.tag)  # Теги перетворюємо на список для збереження в JSON
        }

    @staticmethod
    def from_dict(data):
        """Конвертує словник в об'єкт Note"""
        note = Note(data['title'], data['content'])
        note.tag = set(data['tag'])  # Відновлюємо множину тегів
        return note