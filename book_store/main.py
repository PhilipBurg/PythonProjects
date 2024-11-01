def main():
    
    try:
        #initialize my books list
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(",")
            )
            line = infile.readline() 
        infile.close()

    except FileNotFoundError:
        print("the <bookslist.txt> file is not found")
        print("Starting a new books list")
        booksList = [] #re-initialize books list

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1. Add a book")
        print("2. Lookup a book")
        print("3. Display all books")
        print("4. Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book")
            bookName = input("Enter the name of the book >>>")
            bookAuthor = input("Enter the name of the author >>>")
            bookPages = input("Enter the number of pages >>>")
            booksList.append([bookName, bookAuthor, bookPages])

        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter Searche Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)

        elif choice == 3: 
            print("Displaying all books in the store...")
            for i in range(len(booksList)):
                print(booksList[i])

        elif choice == 4:
            print("Quitting Program")
    print("Program terminated")

    #Saving to a simple txt file:
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()

if __name__ == "__main__":
    main()