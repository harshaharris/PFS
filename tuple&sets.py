Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(3,2.8,"harsha",2+9j,True,False)
a
(3, 2.8, 'harsha', (2+9j), True, False)
type(a)
<class 'tuple'>
a.count("harsha")
1
a.index(True)
4
len(a)
6
len("harsha")
6
#sets
#{}
a={2,2.5,"harsha",2+9j,True,False}
a
{False, True, 2.5, 2, 'harsha', (2+9j)}
type(a)
<class 'set'>
#sets methods
a={3,4,5,3,4,5}
a.add(20)
a
{20, 3, 4, 5}
a={1,2,3,4,5,6}
b={5,6,7,8,9}
a.issubset(b)
False
b.issubset(a)
False
a={2,3,4,5}
b={3,4,5}
a.issubset(b)
False
b.issubset(a)
True
b.issubset(b)
True
a={4,3,2,5,6}
b={2,3,4}
a.issuperset(b)
True
b.issuperset(a)
False
a=[4,3,2,4,2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a={4,3,2,4,2}
a
{2, 3, 4}
#union()
a={2,3,4,5,6}
b={6,7,8,9,10}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b.union(a)
{2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection()
a={2,3,4,5,6}
b={2,3,4,7,8}
a.intersection(b)
{2, 3, 4}
#update()
a={2,3,4,5,6}
b={5,6,7,8,9}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
#difference
a={2,3,4,5,6}
b={3,4,5,6,7}
a.difference(b)
{2}
b.difference(a)
{7}
#symmetric_difference()
a={2,3,4,5,6}
b={2,3,4,7,8}
a.symmetric_difference(b)
{5, 6, 7, 8}
b.symmetric_difference(a)
{5, 6, 7, 8}
#difference_update()
a={2,3,4,5,6}
b={5,6,7,8,9}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{5, 6, 7, 8, 9}
#intersection_update()
a={5,6,7,8,9,10]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a={5,6,7,8,9,10}
b={9,10,11,12,13}
a.intersection_update(b)
a
{9, 10}
b.intersection_update(a)
b
{9, 10}
#symmetri_difference()
a={2,3,4,5,6}
b{5,6,7,8,9}
SyntaxError: invalid syntax
b={5,6,7,8,9}
a.symmetric_difference_update(b)
a
{2, 3, 4, 7, 8, 9}
b.symmetri_difference_update(b)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    b.symmetri_difference_update(b)
AttributeError: 'set' object has no attribute 'symmetri_difference_update'. Did you mean: 'symmetric_difference_update'?
b.symmetri_difference_update(a)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    b.symmetri_difference_update(a)
AttributeError: 'set' object has no attribute 'symmetri_difference_update'. Did you mean: 'symmetric_difference_update'?
>>> b.symmetric_difference_update(a)
>>> b
{2, 3, 4, 5, 6}
>>> a={2,3,4,5,6,7}
>>> a.pop()
2
>>> b={3,4,5,6}
>>> b.pop()
3
>>> a.remove(6)
>>> a
{3, 4, 5, 7}
>>> b.remove(4)
>>> 
>>> b
{5, 6}
>>> a=[5,6,7,8,9,10}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a={5,6,7,8,9,10}
>>> a.copy()
{5, 6, 7, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> #disjoin()
>>> a={2,3,4,5}
>>> b={6,7,8,9}
>>> a.isdisjoint(b)
True
>>> a={3,4,5,6}
>>> len(a)
4
