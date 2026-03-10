#1. importing array module
from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))
#2 positive indexing 
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])
#3 negative indexing
from array import array
arr=array('i',[10,20,30,40,30])
print(arr[-1])
print(arr[-2])
print(arr[-5])
#4 modifying  indexing
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)
#slicing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:1])
print(arr[:1])
#with step
from array import array
arr=(array['i',10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::3])
print(arr[::3])

#negative
from array import array
arr=array('i',[10,20,390,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])
#reserve
from array import array
arr=array('i',[10.20,30,40,50])
print(arr[::-1])
#modifying 
from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)
