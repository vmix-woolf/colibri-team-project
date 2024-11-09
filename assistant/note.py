class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.tag = set()

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTags: {', '.join(self.tag) if self.tag else 'No tags'}"

    def add_tag(self, tag):
        self.tag.add(tag)

    def edit(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content

    def to_dict(self):
        """Конвертує нотатку в словник для серіалізації в JSON"""
        return {
            "title": self.title,
            "content": self.content,
            "tag": list(self.tag)  # Теги перетворюємо на список для збереження
        }

    @staticmethod
    def from_dict(data):
        """Конвертує словник в об'єкт Note"""
        note = Note(data['title'], data['content'])
        note.tag = set(data['tag'])  # Відновлюємо множину тегів

        return note