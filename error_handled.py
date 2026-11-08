#result = 10/0
#print(result)
 try :
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero is no allowed")    
