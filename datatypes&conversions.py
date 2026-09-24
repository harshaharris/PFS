Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
a=10
type(a)
<class 'int'>
b=7.8
type(b)
<class 'float'>
v="harsha"
type(v)
<class 'str'>
a=7j+6
type(a)
<class 'complex'>
a=5j
type(a)
<class 'complex'>
v=True
type(v)
<class 'bool'>
b=False
type(b)
<class 'bool'>
k=9i
SyntaxError: invalid decimal literal
l=j
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l=j
NameError: name 'j' is not defined
a=9+5j
type(a)
<class 'complex'>
a=9i+6j
SyntaxError: invalid decimal literal
a=9+4j
type(a)
<class 'complex'>
z="true"
type(z)
<class 'str'>
#Data types
#int()
int(5)
5
int(9.0)
9
\
int("harsha")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int("harsha")
ValueError: invalid literal for int() with base 10: 'harsha'
int(8+5j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(8+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(2)
2.0
float(2.7)
2.7
float("harsha")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float("harsha")
ValueError: could not convert string to float: 'harsha'
float(9+2j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(9+2j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str()
str(3)
'3'
str(2.8)
'2.8'
str(harsha)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    str(harsha)
NameError: name 'harsha' is not defined. Did you mean: 'hash'?
>>> str("harsha")
'harsha'
>>> str(7+2j)
'(7+2j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex()
>>> complex(2)
(2+0j)
>>> complex(3.4)
(3.4+0j)
>>> complex("harsha")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    complex("harsha")
ValueError: complex() arg is a malformed string
>>> complex(3+4j)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool()
>>> bool(2)
True
>>> bool(2.4)
True
>>> bool("harsha")
True
>>> bool(2+3j)
True
>>> bool(True)
True
>>> bool(False)
False
