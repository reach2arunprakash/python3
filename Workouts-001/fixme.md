#Fix the below in paper -

##Mandatory : Dont use compiler till you solve in paper

Input: -

Expected Output: GUVI
```
myname='GUVI'
print(Myname)
```

---------------------------------------

Expected Output: GUVI

```
if 3.5 % 1.5 == 0:
	op = "GUVI"
else:
	op ="Geek" 
print(op)
```
---------------------------------------
Whats the output?

```
a = 3.5 

if( a == 7//2 ):
	print("GUVI")
else:
	print("Geek")
```

---------------------------------------
Whats the output?

```
for i in range(7):
	if i==3: continue
print(i)


for i in range(7):
    if i==3: break
print(i)

```
---------------------------------------

Input: -

Expected Output: 3

```
data = 0
for i in range(7):
	if i==3: continue
	else: data = i
print(data)
```

---------------------------------------
Expected Output: print "HELLO" 5 times
```
for i in range(1, 10,3):
    print("HELLO")
```
---------------------------------------

Input: -

Expected Output: 13579
```
a = range(1,10,2)
print (a)
```
---------------------------------------
Input: 50

Expected Output: 1275

```
a=input("Enter a number")
sum=0
for i in range (1,a):
    sum=sum+i
print(sum)
```
---------------------------------------

Input: guvi

Expected Output: You entered an alphabet

```
a=input("Press any key...\n")
if a.isalpha() == 0:
    print("You entered an alphabet")
else:
    print("Please try again")
  ```
---------------------------------------	

Input: A

Expected Output: You entered a vovel

```	
a=input("Enter an ALPHABET...\n")
if a=='a'or a=='e'or a=='i'or a=='o'or a=='u':
    print("You entered a vowel")
else:
    print("You entered a consonant")
```
---------------------------------------
Input: 100 12 2

Expected Output: 24

```
p=input("Enter the principal amount")
r=input("Enter the rate")
t=input("Enter the time")
SI=p*t*r/100
print(SI)
```
---------------------------------------
Whats the output?

```
a = [1,2,3,4]
print(a[:1:-1])

a=[0,1,2,3,4]
print(a[-1])

','.join('12345')

```
---------------------------------------

Expected Output: ['a', 'b', 'c', 'e']

```
mydict={'a':1,'b':2,'c':3,'e':5}
a = [mydict.keys()]
print(a)
```
---------------------------------------
Input: 5

Expected Output: {1: 1, 2: 4, 3: 9, 4: 16}


```
n=int(input())
d=dict()
for i in range(0,n+1):
	d[i]=i*i
	print(d)
```
---------------------------------------
Whats the output?

```	
a, b = 2, 3
minvalue = a if a < b else b
print(minvalue)
```
---------------------------------------
Whats the output?

```
g = lambda x, y : x*y
print(g(1, 2))
```
---------------------------------------
Whats the output?

```
g = lambda x, y = 0, z = 0: x+y+z
print(g(1))
```
---------------------------------------
Whats the output?

```
global_var = "GUVI" # global variable
def info():
    addr = "World"     # local variable
    email = "reach@guvi.in"
    print(f'{global_var} address:{addr} and his email is {email}')

info()
```
---------------------------------------
Whats the output?

```
a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 2
finally:
    a += 1
print(a)
```
---------------------------------------
Whats the output?

```
mylist=[0,1,2,3,4,5,6,7,8]
print(mylist[-3:-1])
```
---------------------------------------
Input: 0

Expected Output: "You entered Zero"


```
a=input("Enter a number...\n")
a=int(a)
if a >= 0:
    print("The number is Positive")
elif a<= 0:
    print("The number is Negitive")
else:
    print("You entered Zero")
```
---------------------------------------
Input: -

Expected Output: [10]

```
List = [1,2,3,4,5,6,7,8,9,10]
print(List[:])
```
---------------------------------------
Input: -

Expected Output: [9,8,7]

```	
List = [1,2,3,4,5,6,7,8,9,10]
print(List[:])
```

---------------------------------------
Input: -

Expected Output: ['2002', '2009', '2016']


```
l=[]
for i in range(2000, 2020):
    if (i%7==0) and (i%5==0):
        l.append(str(i))
print(l)
```
