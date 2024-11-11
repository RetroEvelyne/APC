# Initialise an empty stack for books which uses the deque module
book_stack = [
    "Fifty Shades of Code",
    "A Tale of Two Cities (and Servers)",
    "The Picture of Dorian Gray Code",
    "The Hitchhiker's Guide to the API",
    "Brave New World Wide Web",
    "The Count of Monte Cristo: Version Control",
    "The Da Vinci Code: Cryptography Edition",
    "Catcher in the Loop",
    "The Phantom of the Operating System",
    "The Secret Garden of Data Structures"
]

while True:
    print("\n=== Book Stack Manager ===")
    print("1. Add book")
    print("2. Remove last book")
    print("3. Remove first book")
    print("4. View all books")
    print("5. Exit")

    choice = input("\nWhat would you like to do? (1-5): ")

    if choice == '1': # Add a book
        book = input("Enter book title: ")
        #Append the book to the stack and print which book was added
        book_stack.append(book)
        print(f"Added '{book}' to the stack")
    elif choice == '2': #Remove last book
        if book_stack:
            #Remove the last book from the stack and print which book was removed
            book = book_stack.pop()
            print(f"Removed '{book}' from the stack")
        else:
            print("Stack is empty! No books to remove")
    elif choice == '3': #Remove first book
        if book_stack:
            # Remove the first book from the stack and print which book was removed

            # Assuming book_stack is a true stack implementing LIFO
            temp_stack = []
            for _ in range(len(book_stack)):
                temp_stack.append(book_stack.pop())
            book = temp_stack.pop()
            for _ in range(len(temp_stack)):
                book_stack.append(temp_stack.pop())


            print(f"Removed '{book}' from the stack")
        else:
            print("Stack is empty! No books to remove")
    elif choice == '4': # Display all books
        if book_stack:
            print("\nBooks in stack (top to bottom):")
            #Print a list of all books in the queue
            for i, book in enumerate(book_stack):
                print(f"{i+1}: {book}")
        else:
            print("Stack is empty! No books to show")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5")
