#1.basic postional
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a + b
result=add(2,50)
print("sum",result)
#2.student  Information
def student_info(name,roll,marks):
    print("name:",name)
    print("roll No:",roll)
    print("marks:",marks)
student_info("ravi",101,95)

#Basic Keyword Arguments
def student_info(name,age,city):
    print("Name",name)
    print("Age",age)
    print("City",city)
student_info(age=18,city="Rajkot",name="Ravi")    

#Mixing Positional and Keyword

def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
display(a=1,c=3,b=2)    

#using keyword argument
def simpale_intarest(p:float,r:int,t:float):
    si=(p*r*t)
    print("simpale_intarest:",si)
simpale_intarest(p=10000,t=2,r=1.5)
simpale_intarest(t=1.5,p=15000,r=2)    