
def function_one(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max (a,b)

# print (function_one(2,5))

def animal_cracker(animals):
    ani = animals.lower().split()
    return ani[0][0] == ani[1][0]

# animal_cracker("lion ling")


def makes_twenty(a,b):
    if (a + b) ==20 or a==20 or b==20:
        return True
    else:
        return False

# print(makes_twenty(1,1))


def old_mcdonald(string):
    first = string[0]
    second = string[1:3]
    third = string[3]
    fourth = string[4:]
    return first.upper() +second +third.upper() + fourth

# print (old_mcdonald("oldtrump"))

def reverse_list(string):
    words = string.split()
 
    # reverse_string = ''
    # for i in words[::-1]:
    #     reverse_string += i
    #     reverse_string += " "
    # return reverse_string

    reverse = words[::-1]

    return ' '.join(reverse)
    
# print ( reverse_list("This is my country"))

def almost_there(num):
    return abs(num-100) < 10 or abs(num-200)< 10

# print ( almost_there(21))

#level 2        

def find_33(list):
    for i in range(len(list)-1):
        if list[i]==3 and list[i+1]==3:
            return True
            break
    return False

# print ( find_33([1,3,3]))

def paper_doll(text):
    new_string=''
    for i in text:
        new_string += i*3
    return new_string

# print (paper_doll("abc"))

def black_jack(*args):
    if sum(args) <=21 :
        return sum(args)
    elif sum(args) <= 31 and 11 in args:
        return sum(args)-10
    else:
        return "Bust"

# print(black_jack(5,6,7))
# print(black_jack(9,9,9))
# print(black_jack(9,9,11 ))

def summer_69(arr):
    total =0
    add =True

    for num in arr:
        while add:
            if num !=6:
                total += num
                break
            else:
                add=False
            
        while not add:
            if num !=9:
                break
            else:
                add=True
                break
            
    return total

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11])) 


