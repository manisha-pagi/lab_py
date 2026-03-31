f=open("student.txt","w")
f.write("hello!\n")
f.write("welcome to python file\n")
f.write("lerning is fun!\n")
f.close()

f=open("atmiya.txt","w")
f.write("new content only\n")
f.close()

f=open("atmiya.txt","a")
f.write("this line is addad at the end.\n")
f.close()

f=open("atmiya.txt","w")
lines=[
  "python programming\n"
  "file handling\n"
  "error handling\n"
  "exception handling\n"
 ]
f.writelines(lines)
f.close()

 