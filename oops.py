class Dog():

    bark_text = "Woof!\n"

    def __init__ (self,name,breed="lab"):   #default value for breed 
        self.name = name.capitalize()
        self.breed = breed 
    
    def bark(self,number):
        print(Dog.bark_text *number + f"\n The name of the dog is : {self.name}")

my_dog = Dog('niThin','pug')

# print(my_dog.bark(5))

#derived class and inhertienace

class Animal():

    def __init__ (self):
        print("\nAnimal object created")
    
    def who_am_i(self):
        print("\nI am an Animal")

    def what_am_i_doing(self):
        print("\nI am eating")
    

class Dog(Animal):              #Dog class inherting from Animal class
    bark_text = "Woof!\n"
    
    def __init__(self):           #optional
        Animal.__init__(self)
        print("\nDog created")

    def who_am_i(self):
        print("\nI am a Dog")   #when same function name is used, for this instance, this function would run instead of the inherited function

    def bark(self,number):
        print(Dog.bark_text *number)   # there can be unique functions inside this class, just like anyother class

my_dog = Dog()

print(my_dog.what_am_i_doing())
print(my_dog.bark(3))



#polymorphism   - when same method is present in two or more different classes, objects can be iterated upon and the same method could be applied to different objects


class FileOpen():

    def __init__(self,filename):
        self.filename = filename
        print(f"File name is: {self.filename} ")
    
    def openfile(self):
        raise NotImplementedError ("subclass must impliment this abstract method") 

class Excel(FileOpen):

    def openfile(self):
        print(f"opening Excel file {self.filename}")

class Word(FileOpen):

    def openfile(self):
        print(f"opening Word file {self.filename}")
        

newfile = Word('testFile')

# newfile.openfile()



#special methods - use user built-in functions on user defined functions

class Book():
    def __init__(self,title,author,pages):
        self.title =title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"the book name is {self.title}. Authored by {self.author}"

    def __len__(self):              #inbuilt python function
        return self.pages

b= Book("new book","Roshan",409)

print(len(b))
