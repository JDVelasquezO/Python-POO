class User:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def presentation(self):
        return f"Estudiante {self.name}"

class Student(User):
    def __init__(self, name, license):
        User.__init__(self, name)
        self.license = license
        
    def showBook(self):
        print(f"Estudiante {self.name} - {self.license}")
        counter = 1
        for book in self.books:
            print (f"{counter} {book.name} - Edicion {book.edition}")
            counter = counter + 1
        print("\n")
    
    def presentation(self):
        return f"Estudiante {self.name} - {self.license}"

class Book:
    def __init__(self, name, edition):
        self.name = name
        self.edition = edition

s1 = Student("Daniel", "201800722")
s2 = Student("Bryan", "201700523")

b1 = Book('Java POO', 8)
b2 = Book('Python desde 0', 3)
b3 = Book('TYPESCRIPT', 2)
b4 = Book('Node desde cero', 11)

s1.add_book(b1)
s1.add_book(b3)
s2.add_book(b2)
s2.add_book(b4)

s1.showBook()
s2.showBook()