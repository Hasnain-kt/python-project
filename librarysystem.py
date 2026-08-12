

class libraryManagement :
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter id:"))
        title = input("Enter title : ")
        author = input("Enter Author : ")

        book = {
            "book_id" : book_id,
            "title" : title,
            "author" : author,
            "available" : True
        }
        self.books.append(book)

        with open("library.txt" , "a") as f:
            f.write(str(book) + "\n")
        print("successfullly added ")


    def delete_book(self):
        book_id = int(input("Enter book ID : "))
        
        found = False 

        for book in self.books:
            if book_id == book["book_id"]:
                self.books.remove(book)
                found = True
                break

        if not found:
            print("book not exist")

    def search_book(self):
        while True:
            print("1:search by title")
            print("2: search by id")
            print("3:exit")

            choice = int(input("Enter choice "))

            if choice == 1:
                
                title = input("Enter title : ")
                
                found = False

                for book in self.books:
                    if title == book["title"]:
                        if book["available"] == True:
                            print(book)
                        elif book["available"] == False:
                            print("book not available")
                        found = True
                        break

                if not found:
                    print("book not found")

            elif choice == 2:
                
                book_id = int(input("Enter id : "))
                
                found = False

                for book in self.books:
                    if book_id == book["book_id"]:
                        if book["available"] == True:
                            print(book)
                        elif book["available"] == False:
                            print("book not available")
                       
                        found = True
                        break

                if not found:
                    print("book not found")    

            elif choice == 3:
                break            
    

    def issue_book(self):
        while True:
            print("1:search by title")
            print("2: search by id")
            print("3:exit")

            choice = int(input("Enter choice "))

            if choice == 1:
                
                title = input("Enter title : ")
                
                found = False

                for book in self.books:
                    if title == book["title"]:
                        if book["available"] == True:
                            book["available"] = False
                        elif book["available"] == False:
                            print("book not available")
                        found = True
                        break

                if not found:
                    print("book not found")

            elif choice == 2:
                
                book_id = int(input("Enter id : "))
                
                found = False

                for book in self.books:
                    if book_id == book["book_id"]:
                        if book["available"] == True:
                            book["available"] = False
                        elif book["available"] == False:
                            print("book not available")
                       
                        found = True
                        break

                if not found:
                    print("book not found")        
            elif choice == 3:
                break

    def return_book(self):
        title = input("Enter title: ")

        found = False

        for book in self.books:
            if title == book["title"]:
                found = True

                if book["available"] == False:
                    book["available"] = True
                    print("Book returned successfully")
                else:
                    print("Book is already available")
                break

        if not found:
            print("Book not found")
    
    
    
    def save_book(self):
        with open("library.txt" , "w") as f:
            for book in self.books:
                f.write(str(book) + "\n")   



library = libraryManagement()


import ast

with open("library.txt" , "r") as f:
    for line in f:
        book = ast.literal_eval(line.strip())
        library.books.append(book)
   


while True:
    print("1:add_book")
    print("2:delete_book")
    print("3:search_book")
    print("4:issue_book")
    print("5:return_book")
    print("6:exit")

    choice = int(input("Enter choice : "))

    match choice:
        case 1:
            library.add_book()
        case 2:
            library.delete_book()
        case 3:
            library.search_book()
        case 4:
            library.issue_book()
        case 5:
            library.return_book()
        case 6:
            library.save_book()
            break

