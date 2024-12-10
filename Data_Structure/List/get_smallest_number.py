#  Write a Python program to get the smallest number from a list.

mylist = [10,30,25,8,76,45]

small = mylist[0]

for i in range(len(mylist)) :
    if mylist[i] < small :
        small = mylist[i]
        
print("Smallest number from list is : ",small)