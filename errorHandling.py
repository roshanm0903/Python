# try:
#     f = open('myfilafse.txt','r')
#     f.write = ("try catch funtion ran. file opened")
# except TypeError:
#     print ("There was a type error")
# except OSError:
#     print("there was as OS error")
# except:
#     print("All other exceptions/ erros")
# finally:
#     print ("i always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Enter an integer: "))
        except:
            print("that was not an integer:")
            continue
        else:
            print("thank you")
            break
        finally:
            print("I will always run, no matter what")

ask_for_int()