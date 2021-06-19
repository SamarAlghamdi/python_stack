class Library:
    def __init__(self):
        self.books=[Book("Architect","M. Morris Mano","Technology"), Book("oop","Stephen Schach","Technology"),Book("Chemistry","Peter Atkins","Science"),Book("Wave","Rajpal Sirohi","Science"),
        Book("Clinical","David Greenberg","Medical"),Book("Pathophysiology","Leonard Lilly","Medical")]

    def addBook(self,book_name,auther_name,book_catugry):
        self.books.append(Book(book_name,auther_name,book_catugry))
        return self

    def showCatugry(self):
        print("-"*80)
        print("Categories:")
        print("   1-Technology\n   2-Science\n   3-Medical")
        print("-"*80)

    def showBooks(self):
        print("-"*80)
        print("Here is All the library books:")
        for x in range(len(self.books)):
            print(f"{x+1}- {self.books[x].book_name}, Book Author: {self.books[x].auther_name}, Book Category: {self.books[x].book_catugry}\n")
        print("-"*80)

    def booksInCategory(self,category_name):
        for i in range(len(self.books)):
            if self.books[i].book_catugry == category_name:
                print(f"Book name {self.books[i].book_name}")

    def get_book(self, book_name):
        print("*"*80)
        for i in range(len(self.books)):
            if self.books[i].book_name == book_name:
                print(f"Book Name:{self.books[i].book_name}, Book Author: {self.books[i].auther_name}, Book Category: {self.books[i].book_catugry}\n")
                return self.books[i]
        print("*"*80)

    def showallBooksInCat(self,num):
        if num ==1:
            print("\nBooks are: ")
            for x in range(len(self.books)):
                if self.books[x].book_catugry =="Technology":
                    print(f"   - {self.books[x].book_name} by {self.books[x].auther_name}")
        elif num ==2:
            print("Books are: ")
            for x in range(len(self.books)):
                if self.books[x].book_catugry =="Science":
                    print(f"   - {self.books[x].book_name} by {self.books[x].auther_name}")
        elif num ==3:
            print("books are: ")
            for x in range(len(self.books)):
                if self.books[x].book_catugry =="Medical":
                    print(f"   - {self.books[x].book_name} by {self.books[x].auther_name}")

class Book:
    def __init__(self,book_name,auther_name,book_catugry):
        self.book_name=book_name
        self.auther_name= auther_name
        self.book_catugry=book_catugry

    def showBook(self,book_name):
        print(book_name,auther_name,book_catugry)

class User:
    def __init__(self,name):
        self.name=name
        self.books_list=[]
        # self.book=Library()

    def addBook(self, book):
        if len(self.books_list)==0:
            self.books_list.append(book)
            print("    your Book added succssfuly! \nyour new list is:")
        else:
            for x in range(len(self.books_list)):
                if self.books_list[x].book_name==book.book_name:
                    print(f"{book.book_name} is already exists!")
                else:
                    self.books_list.append(book)
                    print("\n    your Book added succssfuly! \nyour new list is:")

    def show_user_book(self):
        if len(self.books_list)==0:
            print("     Your list is empty")
        for i in range(len(self.books_list)):
            print(f"{i+1}- {self.books_list[i].book_name}")

            

name = str(input("Enter your name: "))
user1=User(name)
library=Library()
# book=Book()
while True:
    print("*"*80)
    number = int(input("   1- Show all books\n   2- Show all categories\n   3- Show my books list \n   4- Exit\n"))
    if number==1:
        library.showBooks()
        book_name=str(input("Enter book name to show the detieles: "))
        choosen=library.get_book(book_name)
        check=str(input("Do you want to add this book to your list? 'y' for Yes 'n' for No: "))
        if check=="y":
            user1.addBook(choosen) 
            user1.show_user_book()
        elif check=="n":
            pass
        
    if number ==2:
        library.showCatugry()
        check1=int(input("Choose category number:"))
        library.showallBooksInCat(check1)
        book_name=str(input("Enter book name to show the detieles: "))
        choosen=library.get_book(book_name)
        check=str(input("Do you want to add this book to your list? 'y' for Yes 'n' for No: "))
        if check=="y":
            user1.addBook(choosen) 
            user1.show_user_book()
        elif check=="n":
            pass
    

    if number==3:
        print(f"{user1.name}'s books:")
        user1.show_user_book()
    if number==4:
        break





