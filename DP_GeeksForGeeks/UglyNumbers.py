# print nth number who's prime factors are 2,3, or 5
# eg
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,

def prime(n):

    ugly_no = [0]*(n)
 
    ugly_no[0] = 1

    u2 = u3 = u5 = 0
    i=1

    ugly_no_two = (1)*2
    ugly_no_three = (1)*3
    ugly_no_five = (1)*5

    while i < n :

        check_num = min(ugly_no_two,ugly_no_three,ugly_no_five)

        ugly_no[i] = check_num
        
        if ugly_no_two == check_num:
            u2 +=1
            ugly_no_two = ugly_no[u2]*2
        if ugly_no_three == check_num:
            u3 +=1
            ugly_no_three = ugly_no[u3]*3
        if ugly_no_five == check_num:
            u5 +=1
            ugly_no_five = ugly_no[u5]*5
    
        i+=1


    print(ugly_no)


prime(150)



