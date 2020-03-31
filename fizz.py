for i in range(1,101):
    if i%3 ==0:
        print("fizz")
      
    if i%5 ==0:
        print("buzz")
    elif i%3 ==0:
        continue
    else:
        print(i)