#variables

name=("hamda")
print(name)

age=(23)
print(age)


sum=(12+12)
print(sum)


multiplication=(12*12)
print(multiplication)

#floating numbers in to int

num=3.14
print(num)
print(int(num))



from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") + Decimal("0.3")-Decimal("0.6"))


#random numbers

import random

print(random.random())

print(random.randint(1,10))

print(random.choice(["hamda","ayesha","sara","fatima"]))

students=["hamda","ayesha","sara","fatima"]
random.shuffle(students)
print(students)



#complex num in to int

complex_num=complex(2,3)
print(complex_num)

print(int(complex_num.real))


complex_num=2+3j
print(complex_num)

print(int(complex_num.real))


#subtraction

subtraction=(20-12)
print(subtraction)

#division

division=(20/2)
print(division)

#floor division

floor_division=(20//3)
print(floor_division)

#modulus

modulus=(10%2)
print(modulus)

#exponentiations

exponentiations=(2**3)
print(exponentiations)


#booleans

true=(50>5)
print(true)

false=(10<2)
print(false)

sum=(true+true)
print(sum)

sum=(true+false)
print(sum)

sum = (true+false+true+false)
print(sum)


#for spacing
print("welcome \t to \t my python \t page")

#next line spacing

print("welcome to \n my python \n page \n website")

#operator precedence

num=(10+(10*10))
print(num)

num=((20/2)*10)
print(num)


num=(17%5)
print(num)

#camel case

myName="hamda"
print(myName)

#SNAKE CASE

my_name="laiba"
print(my_name)

#pascal case

MyName="ayesha"
print(MyName)







