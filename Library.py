class Library:
    def __init__(self,list_of_books,name):
        self.bookslist=list_of_books
        self.name=name
        self.lendDict={} #Instance Variable which is an empty Dictionary.
    def displaybooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.bookslist:
            print("Sorry, we do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book]=user
            print("Lender book datatbase has been updated. You can take the book now.")
    def addbook(self,book):
        self.bookslist.append(book)
        print(f"{book} has been added to the book list.")
    def returnbook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("The bppk was not borrowed from us.")
if __name__=='__main__':
    books=Library([
        'Python','Shoe Dog','Rich Dad Poor Dad','Harry Potter and the Prisoner of Azkaban','C++ Basics'
    ],'Let us Updskill')
    user_name=input("Welcone to our Library! Please enter your name: ")

    while True:
        print(
            f"\n Hello {user_name}, welcome to the {books.name} library. Please choose an option:"
        )
        print(
            "1. Display books\n2. Lend a book\n3. Add a book\n4. Return a book\n5.Quit"
        )
        user_choice=input("Enter your choice to continue:")
        if user_choice not in ['1','2','3','4','5']:
            print("Please enter a valid option.")
            continue
        if user_choice=='1':
            books.displaybooks()
        elif user_choice=='2':
            book=input("Enter the name of the book you want to lend: ")
            books.lendbook(user_name,book)
        elif user_choice=='3':
            book=input("Enter the name of the book you want to add: ")
            books.addbook(book)
        elif user_choice=='4':
            book=input("Enter the name of the book you want to return: ")
            books.returnbook(book)
        elif user_choice=='5':
            print(f"Thank you using the Library {user_name}. Goodbye!")
            break



