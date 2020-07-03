class User:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def presentation(self):
        return f"Estudiante {self.name}"