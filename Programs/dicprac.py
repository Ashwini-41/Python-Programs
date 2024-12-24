dic = {"name":"ash","age":20,"roll no":101,"dep":"comp"}

for key,value in dic.items():
    print(key ,": ",value)
    
my_dict = {1:25,2:40,3:10,4:35}

dic2 = dict(sorted(my_dict.items(), key = lambda x:x[1]))
print("Asc Sorted dic ",dic2)

dic3 = dict(sorted(my_dict.items(),key=lambda x:x[1] , reverse=True))
print("Desc Sorted dic ",dic3)

dic.pop("roll no")
print(dic)
dic["name"] = "Ashwini"
print(dic)

