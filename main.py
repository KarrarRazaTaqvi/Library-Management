library=[]

def Display_menu():
    print("\nlibrary managemant system ")
    print("1.Add Books")
    print("2.View All Books ")
    print("3.Issue Book")
    print("4.Return Books")
    print("5.Exit")

def add_book():
    book_id=input("Enter Book ID: ")
    title=input("Enter Book Title:")
    author=input("Enter Book Author:")
    present = False
    for book in library:
        if(book["title"] == title):
            book["count"]+=1
            present = True
            break
    if not present:
        library.append({"id":book_id, "title":title,"author":author,"status":"Available" , "count" : 1})
    print(f"book'{title}' added successfully.")

def view_books():
    if not library:
        print("no book in the library.")
    else:
        print("\nbook in the library:")
        for book in library:
            print(book)

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in library:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print(f"Book '{book['title']}' has been issued.")
                return
            else:
                print(f"Book '{book['title']}' is already issued.")
                return
    print("Book ID not found.")

def return_book():
    book_id=input("enter book ID to return:")
    for book in library:
        if book["id"]==book_id:
            if book["status"]=="Available":
                book["status"]= "Issued"
                print(f"book'{book['title']}'has been returned.")
                return 
            else:
                print(f"book'{book['title']}' is already available.")
                return
    print("book Id not Found.")
def main():
    while True:
        Display_menu()
        choice = input("enter your choice: ")
        if choice == '1':
            add_book()
        elif choice =='2':
            view_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
        
