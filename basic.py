Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='hello,world'
>>> s.title(1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.title(1)
TypeError: title() takes no arguments (1 given)
>>> s.title()
'Hello,World'
>>> l='hai'
>>> type(1)
<class 'int'>
>>> l=['hai']
>>> type(l)
<class 'list'>
>>> s[0]
'h'
>>> s[1]
'e'
>>> s[-1]
'd'
>>> s[::-1]
'dlrow,olleh'
>>> s.join('hia')
'hhello,worldihello,worlda'
>>> l=[1,2,3,4,'pdf','axis']
>>> len(l)
6
>>> len(0)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    len(0)
TypeError: object of type 'int' has no len()
>>> len[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.apend
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.apend
AttributeError: 'list' object has no attribute 'apend'
>>> l=[1,2,3,4,'pdf','aces']]
SyntaxError: invalid syntax
>>> 
