# 1 len()-number of elements
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))

#2 append(x)-add element at end
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#3 insert (pos,x)insert at position
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

# 4 remove(x)-remove first occurence
arr=array('i',[10,20,30,20,40])
x=arr.pop()
print("removed:",x)
print(arr)

# 5pop()-remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#6 Index(x)find  Index of Element
from array import array
arr=array('i',[10,20,30,40])
print(arr.index(30))

#7 count (x)-count occurrences
arr=array('i',[10,20,30,40])
print(arr.count(20))

#8Reverse()-reverse array
arr=array('i',[10,20,30,40,])
arr.reverse()
print(arr)
