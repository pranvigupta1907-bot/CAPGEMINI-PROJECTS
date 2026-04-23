books = []
issued_books = []

def add_books():
    name = input("Enter the name of book:")
    books.append(name)
    print(name,"book is added")
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available Books")
        for book in books:
            print(book)
def issue_books():
    if len(books) == 0:
        print("No books available")
        return
    else:
        show_books()
        name = input("Book you want to issue")
        if name in books:
            issued_books.append(name)
            books.remove(name)
            print(name,"is issued")
        else:
            print(name,"is not available")
def return_book():
    name = input("Enter the book name")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,"is returned")
    else:
        print(name,"is not issued")

def library():
    while True:
        print("menu")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = int(input("Enter your choice"))
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid choice")
library()