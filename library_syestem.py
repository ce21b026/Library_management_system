class Book:
    def __init__(self, name, author, book_id):
        self.name = name
        self.author = author
        self.id = book_id
        self.next = None

class Student:
    def __init__(self, name, email, book_name, author, book_id):
        self.name = name
        self.email = email
        self.book = book_name
        self.author = author
        self.id = book_id
        self.next = None

class Library:
    def __init__(self):
        self.start_lib = None
        self.start = None

    def initialize_lib(self):
        books = [
            ("The Kite Runner", "Khaled Hosseini", 101),
            ("To Kill A Mockingbird", "Harper Lee", 102),
            ("The Alchemist", "Paulo Coelho", 103),
            ("Pride And Prejudice", "Jane Austen", 104),
            ("A Tale Of Two Cities", "Charles Dickens", 105)
        ]

        for book in books:
            self.add_book(*book)

    def add_book(self, name, author, book_id):
        new_book = Book(name, author, book_id)
        if not self.start_lib:
            self.start_lib = new_book
        else:
            ptr = self.start_lib
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_book

    def delete_book(self, book_id):
        if not self.start_lib:
            return
        if self.start_lib.id == book_id:
            self.start_lib = self.start_lib.next
            return
        ptr = self.start_lib
        while ptr.next and ptr.next.id != book_id:
            ptr = ptr.next
        if ptr.next:
            ptr.next = ptr.next.next

    def book_issue(self):
        if not self.start_lib:
            print("\n\tNo books left in the library to issue!\n\tSorry for the inconvenience!\n")
            return

        print("\n\t*************** Books Available: ****************\n")
        ptr = self.start_lib
        i = 1
        while ptr:
            print(f"\n\t_________________________________________________\n")
            print(f"\n\t Book {i}")
            print(f"\n\t Book Title: {ptr.name}")
            print(f"\n\t Name of Author: {ptr.author}")
            print(f"\n\t Book ID: {ptr.id}")
            print(f"\n\t_________________________________________________\n")
            ptr = ptr.next
            i += 1

        book_id = int(input("\n\n\t Enter the Book ID: "))
        ptr = self.start_lib
        while ptr:
            if ptr.id == book_id:
                break
            ptr = ptr.next

        if ptr:
            name = input("\n\t Enter your Name: ")
            email = input("\n\t Enter your Email: ")
            new_student = Student(name, email, ptr.name, ptr.author, ptr.id)
            if not self.start:
                self.start = new_student
            else:
                ptr2 = self.start
                while ptr2.next:
                    ptr2 = ptr2.next
                ptr2.next = new_student
            self.delete_book(ptr.id)
            print(f"\n\t Issue of Book ID {ptr.id} done successfully!\n")
        else:
            print("\n\t\t      ...Invalid Option!...\n")

    def book_return(self):
        if not self.start:
            print("\n\tNo student has issued any books yet.")
            return

        book_id = int(input("\n\n\t Enter your Book ID: "))
        ptr = self.start
        prev = None

        while ptr:
            if ptr.id == book_id:
                break
            prev = ptr
            ptr = ptr.next

        if ptr:
            print(f"\n\t_________________________________________________\n")
            print(f"\n\t Student Name: {ptr.name}")
            print(f"\n\t Student Email: {ptr.email}")
            print(f"\n\t Name of Book Issued: {ptr.book}")
            print(f"\n\t_________________________________________________\n")
            if prev:
                prev.next = ptr.next
            else:
                self.start = ptr.next
            self.add_book(ptr.book, ptr.author, ptr.id)
            print(f"\n\t Return of Book ID {ptr.id} done successfully!\n")
        else:
            print("\n\tSorry, the book doesn't exist! Please recheck the entered ID")

    def display(self):
        if not self.start:
            print("\n\tNo student details to display.")
            return
        ptr = self.start
        while ptr:
            print(f"\n\t************* Details of Students: **************\n")
            print(f"\n\t_________________________________________________\n")
            print(f"\n\t\t Student Name: {ptr.name}")
            print(f"\n\t\t Student Email: {ptr.email}")
            print(f"\n\t\t Name of Book Issued: {ptr.book}")
            print(f"\n\t\t Book ID: {ptr.id}")
            print(f"\n\t_________________________________________________\n")
            ptr = ptr.next

    def main_menu(self):
        while True:
            print("\n\n")
            print("\n\t\t\t*************************************************\n")
            print("\n\t\t\t\t      MAIN MENU: ")
            print("\n\t\t\t\t     1.ISSUE OF BOOKS ")
            print("\n\t\t\t\t     2.RETURN OF BOOKS ")
            print("\n\t\t\t\t     3.DISPLAY STUDENT DETAILS ")
            print("\n\t\t\t\t     4.EXIT\n ")
            print("\n\t\t\t*************************************************\n")
            choice = int(input("\n\t\t\t\t      Enter your choice: "))

            if choice == 1:
                self.book_issue()
            elif choice == 2:
                self.book_return()
            elif choice == 3:
                self.display()
            elif choice == 4:
                exit(1)
            else:
                print("\n\t\t\t\t      ...Invalid Option!...\n")

def greetings():
    print("\n\n")
    print("\t\t\t     ****************************************\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *     ----------------------------     *\n")
    print("\t\t\t     *      WELCOME TO STUDENT LIBRARY      *\n")
    print("\t\t\t     *     ----------------------------     *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     ****************************************\n")
    print("\n\n")
    print("\t\t\t     ****************************************\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *       ------------------------       *\n")
    print("\t\t\t     *           STUDENT LIBRARY            *\n")
    print("\t\t\t     *       ------------------------       *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     *       Mumbai,Maharashtra,India       *\n")
    print("\t\t\t     *     Email: studentlib@gmail.com      *\n")
    print("\t\t\t     *     Contact:8800991010,8800992020    *\n")
    print("\t\t\t     *                                      *\n")
    print("\t\t\t     ****************************************\n")
    input("\n\n\t\t\t             Press any key to continue: ")

if __name__ == "__main__":
    lib = Library()
    lib.initialize_lib()
    greetings()
    lib.main_menu()
