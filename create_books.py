import book_pb2

def create_books():
    books = []

    books.append(book_pb2.Book())
    books[0].id = 1
    books[0].title = "Solaris"
    books[0].author = "Stanislaw Lem"
    books[0].price = 7.54

    books.append(book_pb2.Book())
    books[1].id = 2
    books[1].title = "Dune"
    books[1].author = "Frank Herbert"
    books[1].price = 9.87

    books.append(book_pb2.Book())
    books[2].id = 3
    books[2].title = "Foundation"
    books[2].author = "Isaac Asimov"
    books[2].price = 5.07

    return books
