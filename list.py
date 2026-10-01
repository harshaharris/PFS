Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[4,4.5,"harsha",6+7j,True,False]
print(a)
[4, 4.5, 'harsha', (6+7j), True, False]
type(a)
<class 'list'>
b=2.8
print(b)
2.8
type(b)
<class 'float'>
c=[2.8]
type(c)
<class 'list'>
#append-add
a=["python","ml","java"]
a.append("webdev")
a
['python', 'ml', 'java', 'webdev']
b=["c","c++"]
b.append("java")
b
['c', 'c++', 'java']
a.append(["c","c++")]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a.append(["c","c++"])
a
['python', 'ml', 'java', 'webdev', ['c', 'c++']]
#extend ->adding 2more
a=["python","java","c"]
a.extend(["c++","sql"])
a
['python', 'java', 'c', 'c++', 'sql']
#insert for particular position
a=["python","java","c"]
a.insert(2,"webdev")
a
['python', 'java', 'webdev', 'c']
#index->it shows position
a=["vja","hyd","bang"]
a.index("hyd")
1
#copy()
a.copy()
['vja', 'hyd', 'bang']
b=a=["vja","hyd","bang"]
b
['vja', 'hyd', 'bang']
c=a.copy()
c
['vja', 'hyd', 'bang']
#sort()
a=["apple","banana","kiwi","grapes"]
a.sort()
a
['apple', 'banana', 'grapes', 'kiwi']
b=[7,6,5,4,8,9,10,23,14]
b.sort()
b
[4, 5, 6, 7, 8, 9, 10, 14, 23]
a=["Apple","Mango","Banana"]
a.sort()
a
['Apple', 'Banana', 'Mango']
a=["Apple","mango","banana"]
a.sort()
a
['Apple', 'banana', 'mango']
a=["Apple","Mango","banana"]
a.sort()
a
['Apple', 'Mango', 'banana']
#main priorty upper then lower
b=["Kiwi","apple","Mango","grapes"]
b.sort()
b
['Kiwi', 'Mango', 'apple', 'grapes']
#reverse
a=["red","black","blue","orange"]
a.reverse()
a
['orange', 'blue', 'black', 'red']
b=[2,3,4,2,1,4,5]
b.reverse()
b
[5, 4, 1, 2, 4, 3, 2]
#pop()->deleting
a=["java","c","c++","ml"]
a,pop
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a,pop
NameError: name 'pop' is not defined. Did you mean: 'pow'?
a.pop()
'ml'
a
['java', 'c', 'c++']
>>> b=["python","java","sql","ds"]
>>> b.remove("ds")
>>> b
['python', 'java', 'sql']
>>> c=[20,40,30]
>>> c.clear()
>>> c
[]
>>> c.append(20)
>>> x
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> c
[20]
>>> c.extend(["harsha","k"])
>>> c
[20, 'harsha', 'k']
>>> #len in list
>>> a=["hello","hi"]
>>> len(a)
2
>>> #len in stringmethod
>>> b="hello"
>>> len(b)
5
>>> c=["hello"]
>>> len(c)
1
>>> d=["hi","hello"]
>>> d.count()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> d.count("hello")
1
