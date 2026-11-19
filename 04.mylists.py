#lists

cities =["karachi","lahore","multan","bahawalpur"]
print(cities)

#methods
#append method adds an elememt to the last of the list

cities.append("lahore")
print(cities)

#insert method add element to the specific index

cities.insert(3,"rahim yar khan")
print(cities)

#remove method remove the specific element from the list

cities.remove("multan")
print(cities)

#pop method remove last items

cities.pop(2)
print(cities)

#copy method take no arrgument in their index

cities.copy()
print(cities)


#build a list in one line

square=[x ** 3for x in range(20)]
print(square)


#multidata list

a=["data", 5 ,["this is my listy"], 'computer science', ]
print(a)

#range 

b=range(0,10)
print(b)

for i in range(80,100):
    print(i)

#copyy
 
mylist=["apple","watermelon","kivi","guava"]
list=mylist.copy()
print(list)





