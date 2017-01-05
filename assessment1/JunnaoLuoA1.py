"""
 Name: LUO　JUNNAO
 Date: 1/6/2016
 Details: This program can show the list of books, and provide users who can save the new book to the list and mark which book already be read.
 Github link:  https://github.com/jc345932/sp53/tree/master/assessment1
"""


def display_welcome():
    
    '''() -> NoneType
    Display welcome.

    '''
    print("Reading List 1.0 - by Lindsay Ward")
    
def display_memu():
    
    '''() -> NoneType
    Display memu.

    '''
    print("""Menu:
R - List required books 
C - List completed books
A - Add new book
M - Mark a book as completed
Q - Quit""")

def print_books(books_LIST,flag):
    '''(list) -> bool
    Print the needed books.

    '''
    total_pages = 0
    total_books = 0

    if flag == 1:
        print("Required books:")
        
        for i in range(len(books_LIST)):
            if books_LIST[i][-1] == 'r':   
                total_books += 1
                total_pages += int(books_LIST[i][2])
                print(" %d. %sby %s%d pages"%(i,books_LIST[i][0].ljust(41),books_LIST[i][1].ljust(21),int(books_LIST[i][2])))
    else:
        print("Completed books:")
        for i in range(len(books_LIST)):
            if books_LIST[i][-1] == 'c':
                total_books += 1
                total_pages += int(books_LIST[i][2])
                print(" %d. %sby %s%d pages"%(i,books_LIST[i][0].ljust(41),books_LIST[i][1].ljust(21),int(books_LIST[i][2])))
                
    if total_books != 0:
        #when no require books
        print("Total pages for %d books: %d"%(total_books, total_pages))
        return True
        
    else:
        print("No books")
        return False

def print_require_books(books_LIST):
    '''(list) -> bool
    Print require books.

    '''
    total_pages = 0
    total_books = 0
    for i in range(len(books_LIST)):
        #print the first line
        if books_LIST[i][-1] == 'r':
            if total_books == 0:
                print("Required books:")
            total_books += 1
            total_pages += int(books_LIST[i][2])
            print(" %d. %sby %s%d pages"%(i,books_LIST[i][0].ljust(41),books_LIST[i][1].ljust(21),int(books_LIST[i][2])))
    if total_books != 0:
        #when no require books
        print("Total pages for %d books: %d"%(total_books, total_pages))
        return True
    
    else:
        print("No required books")
        return False

def print_complete_books(books_LIST):
    '''(list) -> bool
    Print complete books.

    '''
    total_pages = 0
    total_books = 0
    for i in range(len(books_LIST)):
        #print the first line
        if books_LIST[i][-1] == 'c':
            if total_books == 0:
                print("Completed books:")
            total_books += 1
            total_pages += int(books_LIST[i][2])
            print(" %d. %sby %s%d pages"%(i,books_LIST[i][0].ljust(41),books_LIST[i][1].ljust(21),int(books_LIST[i][2])))
    if total_books != 0:
        #when no complete books
        print("Total pages for %d books: %d"%(total_books, total_pages))
        return True
    
    else:
        print("No completed books")
        return False
    
def load_books():

    '''() -> list
    Load books from books.csv.

    pseudocode:
    function load_books()
        fp <- open books.csv
        
        for line in fp do
            
            
            messages = line.strip().split(',')

            books_LIST.append(list(messages))
        books_LIST.sort(key=lambda book: book[1],book[2])
        return books_LIST
    '''
    fp = open("books.csv")
    books_LIST = []

    for line in fp:
        m = line.strip().split(',')
        books_LIST.append(m)
    books_LIST.sort(key=lambda book: (book[1],book[2]))  #sort by author and pages


    return books_LIST

def complete_a_book(books_LIST):

    '''(list) -> NoneType
    Complete a book from require books list.

    pseudocode:
    function complete_a_book()

        hasReq = print_require_books(books_LIST)
        if not hasReq:
            return
        while True:
            try:
                c = input()
                c = int(c)
            except Exception as e:
                print('Invalid input; enter a valid number')
                continue

            if c < 0 or c >= len(books_LIST):
                print('Invalid input; enter a valid number')
                continue

            if books_LIST[c][-1] == 'c':

                print('That book is already completed')
                return
            else:

                print("%s by %s marked as completed"%(books_LIST[c][0],books_LIST[c][1]))
                books_LIST[c][-1] = 'c'
                return
        
    '''
    hasReq = print_require_books(books_LIST)
    if not hasReq:
        return
    print("Enter the number of a book to mark as completed")
    while True:
        try:
           
            c = input('>>> ')
            c = int(c)
        except Exception as e:    #check the input
            print('Invalid input; enter a valid number')
            continue

        if c < 0 or c >= len(books_LIST):  #check the input
            print('Invalid input; enter a valid number')
            continue

        if books_LIST[c][-1] == 'c': #check the input

            print('That book is already completed')
            return
        else:

            print("%s by %s marked as completed"%(books_LIST[c][0],books_LIST[c][1]))
            books_LIST[c][-1] = 'c'
            return

def add_new_book(books_LIST):
    '''(list) -> None
    Add a new book.

    '''
    #add title
    while True:

        t = input('Title: ')    
        if t == '':
            print('Input can not be blank')
            continue
        else:
            break
        
    #add Author
    while True:

        a = input('Author: ')    
        if a == '':
            print('Input can not be blank')
            continue
        else:
            break
        
    #add Pages  
    while True:

        p = input('Pages: ')
        try:
            p = int(p)
        except Exception as e:
            print('Invalid input; enter a valid number')
            continue

        if p < 0:
            
            print('Number must be >= 0')
            continue
        else:
            break
    print("%s by %s, (%d pages) added to reading list"%(t,a,p))
    books_LIST.append([t,a,str(p),'r'])

def quit(books_LIST):
    '''(list) -> None
    Save the books.

    '''
    fp = open("books.csv",'w')
    #loop to save the books
    for b in books_LIST:

        fp.write(",".join(b)+'\n')

    fp.close()
    print('%d books saved to books.csv'%(len(books_LIST)))
    print('Have a nice day :)')

def main():

    books_LIST = load_books()
    func_list = ['R','C','A','M','Q']
    display_welcome()
    
    while True:
        #loop to show memu and wait the user input the command
        display_memu()
        c = input(">>> ")

        if c.upper() not in func_list:
            print("Invalid menu choice")
        else:
            
            if c.upper() == 'R':

                 print_books(books_LIST,1)

            elif c.upper() == 'C':
                print_books(books_LIST,2)

            elif c.upper() == 'A':
                add_new_book(books_LIST)

            elif c.upper() == 'M':
                complete_a_book(books_LIST)
            
            elif c.upper() == 'Q':   #quit the program
                quit(books_LIST)
                return

main()
