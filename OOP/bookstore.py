import os,time

class books:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def info(self):
        print(self.title)
        print(self.author)
        print(self.year)
        print(self.price)
        
class comics(books):
    def __init__(self, title, author, year, price, volume):
        super().__init__(title, author, year, price)
        self.volume = volume
    def info(self):
        super().info()
        print("volume "+self.volume)
        
class novels(books):
    def __init__(self, title, author, year, price, edition):
        super().__init__(title, author, year, price)
        self.edition = edition
    def info(self):
        super().info()
        print("Edition "+self.edition)
    
class magazines(books):
    def __init__(self, title, author, year, price, issuedate):
        super().__init__(title, author, year, price)
        self.issuedate = issuedate
    def info(self):
        super().info()
        print("Issue date is "+self.issuedate)


bookss = 0 
comicss = 0
novelss = 0
magaziness = 0
listofcomic = []
listofnovel = []
listofmagazines = []

text = "Welcome to Bookworms!"
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.1)
input("\nnext")
print("What brings you here today?")
print("(Any action done will not be saved when program is run again, it WILL break the code)")
while True:
    print("1. Add a book\n2. See the books\n3. Edit the books\n4. Remove a book\n5. Buy a book(coming soon maybe)")
    answer1 = input("")
    if answer1 == "1":
        classification = input("Is it:\n1. Comic\n2. Novel\n3. Magazine")
        if classification == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            price = input("Price: ")
            volume = input("Volume: ")
            bookss+=1
            comicss+=1
            # idk how to add it
            o = comics(title, author, year, price, volume)
            listofcomic.append(o)
        elif classification == "2":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            price = input("Price: ")
            edition = input("Edition: ")
            bookss+=1
            novelss+=1
            o1 = novels(title, author, year, price, edition)
            listofnovel.append(o1)
        elif classification == "3":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            price = input("Price: ")
            issuedate = input("Issue Date: ")
            bookss+=1
            magaziness+=1
            o2 = magazines(title, author, year, price, issuedate)
            listofmagazines.append(o2)
    elif answer1 == "2":
        if bookss==0:
            print("You have no books to view, please add books")
        elif 0<bookss:
            print("1. Comics\n2. Novels\n3. Magazines")
            answer2 = input("")
            if answer2 == "1":
                if comicss==0:
                    os.system("clear")
                    print("You have no comics to view, please add comics")
                elif 0<comicss:
                    os.system("clear")
                    for i in range(len(listofcomic)):
                        listofcomic[i].info()
                    input("next")
            elif answer2 == "2":
                if novelss==0:
                    os.system("clear")
                    print("You have no novels to view, please add novels")
                elif 0<novelss:
                    os.system("clear")
                    for i in range(len(listofnovel)):
                        listofnovel[i].info()
                    input("next")
            elif answer2 == "3":
                if magazines==0:
                    os.system("clear")
                    print("You have no magazines to view, please add magazines")
                elif 0<magaziness:
                    os.system("clear")
                    for i in range(len(listofmagazines)):
                        listofmagazines[i].info()
                    input("next")
    elif answer1 == "3":
        os.system("clear")
        print("1. Comics\n2. Novels\n3. Magazines")
        answer3 = input("")
        if answer3 == "1":
            if comicss==0:
                os.system("clear")
                print("You have no comics to view, please add comics")
            elif 0<comicss:
                os.system("clear")
                for i in range(len(listofcomic)):
                    print(i+1,".",listofcomic[i])
                input("next")
        elif answer3 == "2":
            if novelss==0:
                os.system("clear")
                print("You have no novels to view, please add novels")
            elif 0<novelss:
                os.system("clear")
                for i in range(len(listofnovel)):
                    print(i+1,".",listofnovel[i])
        elif answer3 == "3":
            if magazines==0:
                os.system("clear")
                print("You have no magazines to view, please add magazines")
            elif 0<magaziness:
                os.system("clear")
                for i in range(len(listofmagazines)):
                    print(i+1,".",listofmagazines[i])
                # for i in range(len(listofmagazines)):
                #     listofmagazines[i].info()
                #     print("-------")
                for i in range(len(listofmagazines)):
                        print(i+1, ".")
                        listofmagazines[i].info()
                input("next")
        

        
    
    



