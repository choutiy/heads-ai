class Record:
    def __init__(self, title, author, content, id):
        self.title = title
        self.author = author
        self.content = content
        self.internal_id = id

    def __str__(self):
        return self.author + "\t" + self.title + "\n" + self.content