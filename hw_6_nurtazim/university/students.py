from hw_6_nurtazim.university.library  import Library
import os
class Students():

    def __init__(self,name):
        self.__name = name
        self.__public_key = os.environ.get("STUDENT_PUB_KEY", default=None)
        self.books_taken = []

    @property
    def public_key(self):
       return self.__public_key


    def get_book(self,Libraryclass,book_name):
        if book_name in Library.books_list() and  Library.check_student_key(self.__public_key):
            Libraryclass.give_book(book_name)
            self.books_taken.append(book_name)

        else:
            print("Ошибка ")

    def retern_book(self,Libraryclass,book_name):
        if book_name in Library.books_list():
            print("This book is in Library already")
            return False
        elif not Library.check_student_key(self.__public_key):
            print("Your public key is wrong or missing")
            return False
        else:
            Libraryclass.return_book(book_name)
            self.books_taken.remove(book_name)

