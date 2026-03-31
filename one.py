src=open("atmiya.txt","r")
data=src.read()
src.close()

dst=open("student.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")