#shopping cart task

cart=("apple" , "watermelon" , "guava" , "mango")

cart=list(cart)
print(cart)

#append
cart.append("kivi")
print(cart)

#insert
cart.insert(1,"orange")
print(cart)

#pop

cart.pop(2)
print(cart)


#remove

cart.remove("mango")
print(cart)



#table of 7

table = [7 * i for i in range (1,11)]
print(table)



#student record

students=("hamda", 1055,158)

rollno, name, marks = students

print (f"My name is {"name"},my roll no is {"roll no"}, my marks is {"marks"}")



#copy or not

a=[30,25,35]

b=a
c=a.copy()

a.append(80)
print("a=",a)
print("b=",b)
print("c=",c)


