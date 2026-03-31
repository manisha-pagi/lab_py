with open("atmiya.txt","r")as f1,open("student.txt","r")as f2,open("create.txt","w")as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
print("files marged successfully")    