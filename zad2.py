
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.city}, {self.street}, {self.zip_code}, godziny: {self.open_hours}, tel: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, zatrudniony: {self.hire_date}, urodzony: {self.birth_date}, adres: {self.city}, {self.street}, {self.zip_code}, tel: {self.phone}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student: {self.name}, oceny: {self.marks}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka: {self.author_name} {self.author_surname}, data wydania: {self.publication_date}, liczba stron: {self.number_of_pages}\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n".join(str(book) for book in self.books)
        return f"Zamówienie z dnia: {self.order_date}\n{self.employee}\n{self.student}\nKsiążki:\n{books_description}"


library1 = Library("Katowice", "Graniczna 61", "40-018", "8:00-18:00", "123456789")
library2 = Library("Rybnik", "Rynek 10", "44-200", "9:00-17:00", "987654321")

employee1 = Employee("Jan", "Kowalski", "2020-01-10", "1990-05-15", "Katowice", "Polna 5", "40-001", "111222333")
employee2 = Employee("Anna", "Nowak", "2021-03-20", "1995-08-22", "Rybnik", "Leśna 7", "44-200", "444555666")
employee3 = Employee("Piotr", "Wiśniewski", "2022-06-15", "1988-12-10", "Katowice", "Szkolna 3", "40-002", "777888999")

student1 = Student("Antoni", [80, 90, 100])
student2 = Student("Krzysztof", [20, 30, 40])
student3 = Student("Michał", [60, 70, 80])

book1 = Book(library1, "2020-01-01", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2018-05-10", "Henryk", "Sienkiewicz", 450)
book3 = Book(library2, "2021-06-15", "Bolesław", "Prus", 500)
book4 = Book(library2, "2019-09-20", "Stefan", "Żeromski", 350)
book5 = Book(library1, "2022-11-05", "Olga", "Tokarczuk", 400)

order1 = Order(employee1, student1, [book1, book2, book3], "2026-10-25")
order2 = Order(employee2, student2, [book4, book5], "2026-10-25")

print(order1)
print()
print(order2)
