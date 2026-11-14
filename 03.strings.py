#strings

print("welcome to my page")
print('welcome to my website')

print('this is my "page"')


a=("my name is hamda")
b=a

print(b)

a=('this is my web page')
print(a)


#length

a=("rohi learning hub")
print(len(a))

#indexing

a=('pakistan software export software board')
print(len(a) -1)

#positive indexing
print(a[0])
print(a[1])
print(a[15])

#negative indexing
print(a[-1])
print(a[-2])
print(a[-10])


#slicing
a=('pakistan software export software board')
print(a[:])
print(a[5:9])
print(a[10:15])
print(a[:-15])
print(a[7:-10])


#strings methods

#upper and lower case

a=("hello world")
print(a.upper())
print(a.lower())

#strip

a=("     my name is hamda       ")
print(a.strip())

#replace

a=("lets go for a walk")
print(a.replace("walk","run"))


#split

a=("lets go for a walk")
print(a.split(' walk'))

#center

a=("pakistan board of software export")
print(a.center(100))

#string formating

#.format

username=("hamda")
age=(23)

print("Hello, my name is {} and I am {} years old. ".format(username,age))

#fstring

username=("hamda")
age=(20)

print(f"Hello, my name is {username} and I am {age} years old.")


#string concatenation

a=("hamda")
b=("ayesha")
c = a+b
print(c)


a=("pakistan")
b=("softwareboard")
c = a+b
print(c)


import math

num=10.5
print(math.floor(num))


num=3.7
print(math.floor(num))


num=4.6
print(math.ceil(num))


#number systems

#decimal to binary, octal and hexadecimal

num=25
#binary

print(bin(num))

# octal
print(oct(num))

#hexadecimal

print(hex(num))