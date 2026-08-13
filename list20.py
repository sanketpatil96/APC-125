"""20.	Create a list of books.
Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books
"""
# Book Management using List

books = []

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print(book, "added successfully.")

    elif choice == 2:
        book = input("Enter book name to search: ")
        if book in books:
            print(book, "is available.")
        else:
            print(book, "is not available.")

    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print(book, "removed successfully.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("Books in Library:", books)

    elif choice == 5:
        print("Total Books:", len(books))

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")