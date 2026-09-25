Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=3
b=1
print(a+b)
4
print(a-b)
2
print(a*b)
3
print(a//b)
3
print(a/b)
3.0
print(a**b)
3
print(a%b)
0
#assignment
a=5
b=8
a+=b
a
13
b-=3
b
5
b*=5

b
25
b//=25
b
1
b/=3
b
0.3333333333333333
b**=2
b
0.1111111111111111
b%=4
b
0.1111111111111111
#comparision
a=3
b=6
a>b
False
a<b
True
b>a
True
b<a
False
a>=b
False
b<=b
True
a!=b
True
b!=b
False
a==b
False
b==a
False
a=2
b=2
a==b
True
#logical
a=10
b=15
a>b and b<a
False
a>=b and b>=a
False
a!=b and a==b
False
a<b and b>a
True
a>b or b<a
False
a==b or a!=b
True
not true
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify
a=4
type(a)
<class 'int'>
type(a) is int
True
type(a) is float
False
type(a) is not float
True
type(a) is not string
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    type(a) is not string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(a) is not str
True
type(a) is str
False
type(a) is complex
False
type(a) is not complex
True
type(a) is boolean
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    type(a) is boolean
NameError: name 'boolean' is not defined
type(a) is bool
False
type(a) is not bool
True
#membership
a=3,4,5,6,7
9 in a
False
9 not in a
True
4 in a
True
4 not in a
False
#bitwise
a=3
b=2
a&b
2
>>> bin(2)
'0b10'
>>> bin(3)
'0b11'
>>> a^b
1
>>> a=2
>>> b=5
>>> a|b
7
>>> b|a
7
>>> a=3
>>> b=5
>>> a|b
7
>>> a=3
>>> ~a
-4
>>> a=3
>>> b=2
>>> a^b
1
>>> a=4
>>> a<<3
32
>>> bin(32)
'0b100000'
>>> a=2
>>> a<<1
4
>>> bin(4)
'0b100'
>>> a=9
>>> a>>2
2
>>> a=3
>>> a>>4
0
