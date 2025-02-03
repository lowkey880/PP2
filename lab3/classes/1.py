class str:
    def __init__(self):

        self.text = ""

    def get(self):

        self.text = input("Write a text: ")

    def out(self):

        print(self.text)
    

string = str()

string.get()

string.out()