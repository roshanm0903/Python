print('hello')

# string ="dfs fdsa f fdafdfdasfaf"

# string.split()

###file
myfile = open('myfile.txt')
myfile.read() #returns the entire contents as string
myfile.seek(0) #moves the cursor to some location
myfile.readline() #returns the entire contents as a list of strings
myfile.close()

with open('myfile.txt') as my_newfile: #need not close the files
    contents = my_newfile.read()
print(contents)

with open('myfile.txt', mode="a") as f:
    f.write("\n new line")

# for loops
 
mylist =[1,1,3,3,5,6,0]

for i in mylist:
    print(i)  # prints the numbers in the list

for i in range(len(mylist)):
    print(i) # print numbers from 0 to length of the list

for letter in 'hello world':
    print (letter)     # prints of each letter in the 'hello world' string - string is an ordered list
    # works in similar way for tuples as well


#tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in mylist:
    print (a)
    print (b)

# output
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8

# for loops with dictionary

myDict = {"k1":1,"k2":10,"K3":100}

for key,value in myDict.items():
    print(value)






# While loops

x = 0

while x<5:
    print(f'the current value of x is {x}')
    x+=1
else:  # else is optional
    print('x is greater than 4')

# generating lists, list comprehension

mylist = [ x**2 for x in range(1,12) if x%2==0]


# functions

def my_function(name="default"):
    '''
    Docsctring: description about the function
    Input:
    Putput:
    '''
    return "Hello"+name


# *args - no limits on the number of arguments
def compute(*args):
    return sum(args)   #pythons treats the arguments as a tuple

comp = compute(1,2,3,)


# *kwargs - no limits on the number of arguments
def compute(**kwargs):
    if 'fruit' in kwargs:    # check for this key in the dictionary
        print('test string is {}'.format(kwargs['fruit']) )
    else:
        print("not found")

