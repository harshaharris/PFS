Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(5+4)
9
a=10
print(a)
10
x=50
print(x)
50
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
a,b=6,7
print(a,b)
6 7
3=90
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=90
print(a3)
90
5x=10
SyntaxError: invalid decimal literal
x5=10
print(x5)
10
a0123=20
print(a0123)
20
name="harsha"
print(name)
harsha
print("name")
name
city="hyd"
print(city)
hyd
print("city")
city
country="india"
print(country)
india
Country="India"
print(Country)
India
a=8
b=9
print(a+b)
17
17
17
fname="harsha"
lname="koppuravuri"
print(fname+" "+lname)
harsha koppuravuri
print(fname+lname)
harshakoppuravuri
print(fname,lname)
harsha koppuravuri
a=3,b=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=9
print(a+b)
12
a,b=3,9
print(a,b)
3 9
print(a+b)
12
a=2
b=3
print(a+b)
5
#special charactrers
@=9
SyntaxError: invalid syntax
$=10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(_a)
100
a=2,3,4,5,6
print(a)
(2, 3, 4, 5, 6)
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c,f,v,c,r=2,3,4,5,5,6,7,77,8,8
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a,b,c,f,v,c,r=2,3,4,5,5,6,7,77,8,8
ValueError: too many values to unpack (expected 7)
first name="harsha"
SyntaxError: invalid syntax
first_name="harsha"
print(first_name)
harsha
firstname="harsha"
print(firstname)
harsha
 a=3
 
SyntaxError: unexpected indent
a=3
print(a)
3
_a=9
>>> print(-a)
-3
>>> print(_a)
9
>>> #unpacking
>>> a=(1,2,3)
>>> print(a)
(1, 2, 3)
>>> a,b,c=(1,2,3)
>>> print(a,b,c)
1 2 3
>>> #del keyword
>>> a=80
>>> print(a)
80
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> #case sensitive
>>> name="harsha"
>>> print(name)
harsha
>>> Name="harsha"
>>> print(name)
harsha
>>> NAME="harsha"
>>> print(NAME)
harsha
>>> print(Name)
harsha
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
