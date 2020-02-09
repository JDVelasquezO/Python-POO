class Book:
    def __init__(self, name, edition):
        self.name = name
        self.edition = edition

class User:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

class Student(User):
    def __init__(self, name, license):
        User.__init__(self, name)
        self.license = license

u = Student("Daniel", "201800722")
b1 = Book('Java POO', 8)
b2 = Book('Python desde 0', 3)

u.add_book(b1)
u.add_book(b2)

print(f"Los libros de {u.name} - {u.license} son: ")
counter = 1
for u_book in u.books:
    print(f"{counter} Libro {u_book.name} - Edicion {u_book.edition}")
    counter = counter + 1