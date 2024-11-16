class Publication:
    def __init__(self,name):
        self.name=name


class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author=author
        self.page_count=page_count

    def print_information(self):
        print(f"Book name is {self.name}")
        print(f"Author is {self.author}")
        print(f"Page count is {self.page_count}")


class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor=chief_editor

    def print_information(self):
        print(f"Magazine name is {self.name}")
        print(f"Chief editor is {self.chief_editor}")


# main program

def main():
    magazine=Magazine("Donald Duck","Aki Hyyppa")
    book=Book("Compartment No.6","Rosa Liksom",192)

    magazine.print_information()
    book.print_information()

if __name__=="__main__":
    main()