class Record:
    def __init__(self, title, author, content, external_id, namespace="TC"):
        self.title = title
        self.author = author
        self.content = content
        self.namespace = namespace
        self.internal_id = namespace + "_" + external_id
