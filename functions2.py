###print number of primes until the given number

def check_primes(n):

    if n<2:
        return 0
    
    set_primes =[2]
    i=3

    while i<=n:
        for j in range(3,i,2):
            if i%j ==0 :
                i+=2
                break
        else:
            set_primes.append(i)
            i=i+2
        
    print(set_primes)
    return len(set_primes)

# print(check_primes(20))


def print_big(string):

    pattern = { 1: '  *  ', 2:' *** ', 3:'*   *', 4:'*****', 5:'**** ', 6:"*    ",7:'    *'}
    alphabet = {'A':[2,3,4,3,3],'B':[5,3,4,3,5],'C':[4,6,6,6,4],'D':[5,3,3,3,5],'E':[4,6,5,6,4]}

    for letter in string:
        for j in alphabet[letter.upper()]:
            # print (j)
            print (pattern[j])
        print("\n")

# print_big("ABC")

######################################################################################33

# map and filter functions

def square_num(num):
    return num**2

list_nums = [1,2,3,4,5]
# print(list(map(square_num,list_nums)))

def check_even(num):
    return num%2 == 0
# print(list(filter(check_even,list_nums)))   #filter the list based on the boolean that the function returns



#lamda functions

# def square(num): return num**2

# print(list(map(lambda num: num**2,list_nums)))


# nested functions
name ="nithin"
def greet():
    name ="roshan"

    def hello():
        print("Hello " + name)
    
    hello()

greet()