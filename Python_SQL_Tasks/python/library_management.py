FILE_NAME = "books.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id},{book_name},{author},Available\n")

    print("Book added successfully.")


def view_books():

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    print("\n----- Books -----")

    for book in books:
        data = book.strip().split(",")

        print("Book ID:", data[0])
        print("Book Name:", data[1])
        print("Author:", data[2])
        print("Status:", data[3])
        print("-----------------")


def search_book():

    book_id = input("Enter Book ID to search: ")

    with open(FILE_NAME, "r") as file:

        for book in file:
            data = book.strip().split(",")

            if data[0] == book_id:
                print("\nBook Found")
                print("Book ID:", data[0])
                print("Book Name:", data[1])
                print("Author:", data[2])
                print("Status:", data[3])
                return

    print("Book not found.")


def main():

    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()