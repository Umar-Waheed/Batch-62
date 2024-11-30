# Library Management System

# Data Structures
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "status": "Available"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "status": "Checked Out"},
    {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "status": "Available"},
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": [2]},  # Alice borrowed "1984"
    {"id": 2, "name": "Bob", "borrowed_books": [5]},   # Bob borrowed "The Catcher in the Rye"
]

# Helper Functions
def display_books(filter_status=None):
    """Display books based on their status (Available/Checked Out)."""
    print("\nAll Books:")
    for book in books:
        if filter_status and book["status"] != filter_status:
            continue
        print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    print("-" * 40)

def search_books(query, search_by="title"):
    """Search for books by title, author, or genre."""
    print(f'\nSearch Results for "{query}" ({search_by.capitalize()}):')
    results = [book for book in books if query.lower() in book[search_by].lower()]
    if results:
        for book in results:
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    else:
        print("No books found.")
    print("-" * 40)

def borrow_book(user_id, book_id):
    """Allow a user to borrow a book if available."""
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if not user:
        print("Invalid User ID.")
        return
    if not book:
        print("Invalid Book ID.")
        return

    if book["status"] == "Available":
        if book["id"] not in user["borrowed_books"]:  # Prevent duplicates
            book["status"] = "Checked Out"
            user["borrowed_books"].append(book["id"])
            print(f'Book "{book["title"]}" has been checked out successfully!')
        else:
            print(f'Book "{book["title"]}" is already in your borrowed list.')
    else:
        print(f'Sorry, the book "{book["title"]}" is currently checked out.')

def return_book(user_id, book_id):
    """Allow a user to return a book."""
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if not user:
        print("Invalid User ID.")
        return
    if not book:
        print("Invalid Book ID.")
        return

    if book_id in user["borrowed_books"]:  # Ensure the book is actually borrowed
        book["status"] = "Available"
        user["borrowed_books"].remove(book_id)  # Remove from user's borrowed list
        print(f'Book "{book["title"]}" has been returned successfully!')
    else:
        print(f'This book was not borrowed by user {user["name"]}.')

def view_users():
    """Display all users and their borrowed books."""
    print("\nAll Users:")
    for user in users:
        borrowed = ", ".join([str(book_id) for book_id in user["borrowed_books"]]) or "None"
        print(f'{user["id"]}. {user["name"]} (Borrowed books: {borrowed})')
    print("-" * 40)

def borrowed_books_summary():
    """Display a list of borrowed books and their respective borrowers."""
    print("\nBorrowed Books and Borrowers:")
    found = False
    for book in books:
        if book["status"] == "Checked Out":
            found = True
            # Find the user who borrowed this book
            borrower = next((user for user in users if book["id"] in user["borrowed_books"]), None)
            if borrower:
                print(f'"{book["title"]}" by {book["author"]} is borrowed by {borrower["name"]}.')
    if not found:
        print("No books are currently borrowed.")
    print("-" * 40)

def add_user():
    """Add a new user to the library system."""
    try:
        new_id = int(input("Enter a unique User ID: "))
        if any(user["id"] == new_id for user in users):
            print("User ID already exists. Please try a different ID.")
            return

        name = input("Enter the user's name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            return

        users.append({"id": new_id, "name": name, "borrowed_books": []})
        print(f"User '{name}' has been successfully added with ID {new_id}!")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

def add_book():
    """Add a new book to the library."""
    try:
        new_id = len(books) + 1  # Auto-generate a new ID based on current book count

        title = input("Enter the book title: ").strip()
        if not title:
            print("Title cannot be empty. Please try again.")
            return

        author = input("Enter the book author: ").strip()
        if not author:
            print("Author cannot be empty. Please try again.")
            return

        genre = input("Enter the book genre: ").strip()
        if not genre:
            print("Genre cannot be empty. Please try again.")
            return

        # Add the new book to the books list
        books.append({"id": new_id, "title": title, "author": author, "genre": genre, "status": "Available"})
        print(f'Book "{title}" by {author} has been successfully added to the library!')
    
    except ValueError:
        print("Invalid input. Please try again.")

# Main Program
def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("-" * 40)
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Add a user")
        print("7. View borrowed books and borrowers")
        print("8. Exit")
        print("9. Add a new book")  # New option to add books

        choice = input("\nEnter your choice (1-9): ")
        if choice == "1":
            display_books()
        elif choice == "2":
            query = input("Enter the title, author, or genre to search: ")
            search_by = input("Search by (title/author/genre): ").lower()
            if search_by in ["title", "author", "genre"]:
                search_books(query, search_by)
            else:
                print("Invalid search criteria.")
        elif choice == "3":
            try:
                user_id = int(input("Enter your User ID: "))
                book_id = int(input("Enter the Book ID you want to borrow: "))
                borrow_book(user_id, book_id)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")
        elif choice == "4":
            try:
                user_id = int(input("Enter your User ID: "))
                book_id = int(input("Enter the Book ID you want to return: "))
                return_book(user_id, book_id)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")
        elif choice == "5":
            view_users()
        elif choice == "6":
            add_user()
        elif choice == "7":
            borrowed_books_summary()  # Display borrowed books with their borrowers
        elif choice == "8":
            print("Thank you for using the Community Library System. Goodbye!")
            break
        elif choice == "9":
            add_book()  # Call the function to add a new book
        else:
            print("Invalid choice. Please select a number between 1 and 9.")

# Run the program
main_menu()