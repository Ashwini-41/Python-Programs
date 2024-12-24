
add = lambda x,y : x+y
print(add(10,20))

listex = [1,2,3,4,5]

sqr_list = list(map(lambda x: x**2,listex))
print("List square",sqr_list)

sq_lc = [x**2 for x in listex]
print("List sqr lc ",sq_lc)