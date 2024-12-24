arr = [15,20,35,40]

for i in arr:
    # print(i)
    if i % 2 == 0:
        print(i)
arr.remove(35)
print(arr)
arr.append(10)
print(arr)
arr.insert(1,67)
print(arr)

arr1 = [10,11,23,5,67,65,43,21,56,89,76]

print("Array : ",arr1)
max_num = max(arr1)
print("Maximum number is : ",max_num)