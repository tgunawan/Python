
# Management Console based app for a book store to keep track of books using txt file(data.txt).
# Concepts Used:
   #- Variable: FILE to store the name of our data file.
   #- Looping: 'while True' for the menu and 'for' for reading the file/list.
   #- Data Structure: List to store book data.
   #- File Handling: 'r' and 'w' with 'with'.
   #- Error Handling: try & except for FileNotFoundError and ValueError. So, if the file doesn't exist, it creates a new one, 
   # and if the user enters a non number for qty, it catches that error.
# Instruction: Run the code, choose 1 to see the stock, 2 to add book & qty, and lastly 3 to exit the program. 
# Data will be saved in a file named "data.txt" in the same directory.

# CODE:
FILE = "data.txt"
def load_data():
    book_list = [] #List to hold all the book data.
    try:
        with open(FILE, "r") as file:
            for line in file:
                removal = line.strip() #Remove the \n at the end of each line. So "Book Title,Author Name,Qty\n" becomes "Book Title,Author Name,Qty"
                if removal:  # Make sure the line isn't empty
                    parts = removal.split(",") # This turns the string (Book Title,Author Name,Qty) into a list ["Book Title", "Author Name", "Qty"]
                    if len(parts) == 3: # Check if we have exactly 3 parts (title, author, qty)
                        title = parts[0]
                        author = parts[1]
                        qty = int(parts[2]) # Convert the quantity from string to an integer. If this fails, it will trigger a ValueError which we catch later.
                        book_list.append([title, author, qty])
                        
    except FileNotFoundError: # If data.txt doesn't exist yet, we just return an empty list
        print("No existing file found. New one will be created.")
    except ValueError: # If the qty is not a number, we catch the error
        print("Error: Invalid quantity format. Please try again.")
    return book_list

def save_data(book_list):
    # "W to write. It will also create the file if it's doesn't exist.
    with open(FILE, "w") as file: #With automatically closes the file after we're done writing
        for book in book_list:
            file.write(f"{book[0]},{book[1]},{book[2]}\n")# Turn the list back into a string separated by commas (Book Title, Author, Qty)

def main():
    books = load_data() #Turn the function into a variable so we can use it in our menu loop. This will load the data from the file when the program starts.
    while True:
        print("\n---Welcome to Library of Ruina App---")
        print("1. View and Sort Inventory\n")
        print("2. Add a New Book\n")
        print("3. Exit Program\n")
        
        uinput = input("Choose an option (1-3): ")
        if uinput == "1":
            if len(books) == 0:
                print("It's empty! Try adding some books first.")
            else:
                books.sort() # This automatically sorts the list alphabetically by the book's title
                print("\n---Inventory---")
                for book in books:
                    title = book[0]
                    author = book[1]
                    qty = book[2]
                    print(f"Title: {title} | Author: {author} | Qty: {qty}")
        elif uinput == "2":
            n_title = input("Enter the book's title: ")
            n_author = input("Enter the author's name: ")
            try:
                n_qty = int(input("Enter how many copies you have: "))
                books.append([n_title, n_author, n_qty]) # Add the new book to our list temporarily
                save_data(books) # Save the updated list to our file
                print(f"Success! '{n_title}' was added to the inventory.")
            except ValueError:
                print("Sorry, must be a number! Try again!.")
        elif uinput == "3":
            print("Saving data...")
            print("Saving data...")
            print("Goodbye! 886!")
            break 
        else:
            print("Invalid choice. Please type 1, 2, or 3.")
main()