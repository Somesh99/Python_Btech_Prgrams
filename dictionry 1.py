Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x={1:1,2:4,3:9,4:16,5:25}
>>> x.keys()
dict_keys([1, 2, 3, 4, 5])
>>> x.values()
dict_values([1, 4, 9, 16, 25])
>>> x.items()
dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
>>> len(x)
5
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0]
KeyError: 0
>>> x.haskey(4)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.haskey(4)
AttributeError: 'dict' object has no attribute 'haskey'
>>> x.has_key(4)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x.has_key(4)
AttributeError: 'dict' object has no attribute 'has_key'
>>> 
