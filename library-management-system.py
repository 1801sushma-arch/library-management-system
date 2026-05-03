#build library management(oop),add book, borrow, return, store in file
class Library:
    def __init__(self,books):
        self.books=books
    
    def show_books(self):
        if not self.books:
            print("no books available")
            return
        print("Books Available:")
        for book in self.books:
            print("-",book)
    def borrow_books(self,book_name):
        book_name=book_name.strip().capitalize()
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name} borrowed successfully")
        else:
            print("not avialable")
    def return_books(self,book_name):
        book_name=book_name.strip().capitalize()
        if book_name not in self.books:
            self.books.append(book_name)
            print(f"{book_name} returned successfully")
        else:
            print("Already returned")

lib=Library(["Python","Java","C","AI"])
print("before borrowing:")
lib.show_books()

lib.borrow_books("python")

print("\n after borrowing:")
lib.show_books()

lib.return_books("python")
print("\n After returning:")
lib.show_books()
