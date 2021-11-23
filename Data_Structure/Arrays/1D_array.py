from array import *

a = array('i',[])

num = int(input("Enter the number of elements to be added to the array:\n"))

# Insertion and Traversing
for i in range(0,num):
    ele = int(input("Ente the elemenet to be added:"))
    a.append(ele)
for i in a:
    print(i)


# Sorting Array
i = num-1
l = 0
while i>=l:
    j = l
    while j < i:
        if a[j] > a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
        j = j + 1
    i = i - 1

print("Sorted array is: \n")

for i in a:
    print(i)

# Searching Array

search = int(input("Enter the element to be searched:\n"))
for m in a:
    if m == search:
       flag = 1
       break
    else:
        flag = 0

if flag == 1:
    print("Element found!")
else:
    print("Element not found!")








