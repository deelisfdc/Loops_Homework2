
# List we'll use for all of the books in library

books = ["Dune", "Pride and Prejudice"]

# Print welcome title

print "Brighticorn's Books"
print "-------------------"

use_library = True

while use_library:

    print "You can add, view, check or exit"

    command = raw_input("Action > ")

    command = command.lower()

    print "Action:", command

    if command == "exit":

        print "Goodbye!"

        use_library = False

    elif command == "add":
        print "Add books"

        add_book = raw_input("What book do you want to add? > ")

        books.append(add_book)

        print "Added:", add_book

    elif command == "view":

        print "View books"

        for book in books:
            print book

        #for some reason this for book in books: didn't work the first
        #few times...couldn't figure out why
        

        # num_books = len(books)
        # i = 0

        # while i < num_books:
        #     print books[i]
        #     i = i + 1

        print "End of Listing"

    elif command == "check":
        print "Check for a book"

        book_name = raw_input("Which book do you want to check? > ")
        # book_name = book_name.lower() this lower() doesn't work
        # because python is looking for an exact match.

        if book_name in books:
            print "We found:", book_name

        else:
            print book_name, "not found."

    else:
        print "Sorry, that's not an option!"
