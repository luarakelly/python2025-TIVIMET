# Superclass
class Publication:
    def __init__(self, name):
        self.name = name

# Subclass Book
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_details(self):
        print(f"Book: {self.name}")
        print(f" Author: {self.author}")
        print(f" Pages: {self.pages}")

# Subclass Magazine
class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_details(self):
        print(f"Magazine: {self.name}")
        print(f" Editor-in-chief: {self.editor}")

# Main program
publications = []
publications.append(Magazine("Aku Ankka", "Aki Hyyppä"))
publications.append(Book("Hytti n:o 6", "Rosa Liksom", 200))

for pub in publications:
    pub.print_details()
