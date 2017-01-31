"""
Name:LUO JUNNAO
Date: 30/1/2017
Brief Project Description: Make a book list to check or store which book users need
GitHub URL: https://github.com/jc345932/sp53/tree/master/assessment2
"""
from booklist import BookList
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    def on_start(self):
        print("on_start is called.")
        myfile = open("books.csv", "r")
        booklists = myfile.readlines()
        print(booklists)
        myfile.close()
        temp_button = Button(text="Testing one")
        temp_button.bind(on_release=self.press)
        self.root.ids.entriesBox.add_widget(temp_button)

    def press(self, instance):
        pass

    def build(self):
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        return self.root

    def on_stop(self):
        print("calling on stop")

    def print_require_books(books_LIST):
        total_pages = 0
        total_books = 0
        for i in range(len(books_LIST)):
            # print the first line
            if books_LIST[i][-1] == 'r':
                if total_books == 0:
                    print("Required books:")
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


ReadingListApp().run()
