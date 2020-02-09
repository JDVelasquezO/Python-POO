from User import User

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