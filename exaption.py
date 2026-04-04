try:
    number1=int(input("Enter a number:"))
    number2=int(input("Enter another number:"))
    result=number1/number2
except ZeroDivisionError:
    print("you cannot divide by zero!")    

except ValueError:
    print("Plese enter a valid number!")

else:
    print("Division successfull rResult is:",result)

finally:
    print("This blok always runs. ")

    #Example=2
try:
    my_list = [1,2,3]
    print(my_list[1])  #this index does not exist

except IndexError:
    print("index is out of range!")

else:
    print("Element found successfully!") 

finally: 
    print("program finished.")       
