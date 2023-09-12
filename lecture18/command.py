class Document:
    def __init__(self):
        self.content = ""

    def insert_text(self, text, position):
        self.content = self.content[:position] + text + self.content[position:]

    def delete_text(self, start, end):
        self.content = self.content[:start] + self.content[end:]


class Command:
    def execute(self):
        pass


class InsertCommand(Command):
    def __init__(self, document, text, position):
        self.document = document
        self.text = text
        self.position = position

    def execute(self):
        self.document.insert_text(self.text, self.position)


class DeleteCommand(Command):
    def __init__(self, document, start, end):
        self.document = document
        self.start = start
        self.end = end

    def execute(self):
        self.document.delete_text(self.start, self.end)


document = Document()

insert_command = InsertCommand(document, "Hello, ", 0)
insert_command.execute()

delete_command = DeleteCommand(document, 5, 7)
delete_command.execute()

print(document.content)
