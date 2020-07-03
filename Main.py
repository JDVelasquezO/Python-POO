from Student import Student
from Book import Book

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