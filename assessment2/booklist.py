# create your BookList class in this file
class BookList:
    def __init__(self):
        self.booklists = []
    def print_require_books(books_LIST):
        total_pages = 0
        total_books = 0
        for i in range(len(books_LIST)):
            # print the first line
            if books_LIST[i][-1] == 'r':
                if total_books == 0:
                    total_books += 1
                    total_pages += int(books_LIST[i][2])
                    print(" %d. %sby %s%d pages" % (
                    i, books_LIST[i][0].ljust(41), books_LIST[i][1].ljust(21), int(books_LIST[i][2])))
        if total_books != 0:
            return True
        else:
            return False

    def print_complete_books(books_LIST):
        total_pages = 0
        total_books = 0

        for i in range(len(books_LIST)):
            # print the first line
            if books_LIST[i][-1] == 'c':
                if total_books == 0:
                    print("Completed books:")
                total_books += 1
                total_pages += int(books_LIST[i][2])
        if total_books != 0:
            return True

        else:
            return False