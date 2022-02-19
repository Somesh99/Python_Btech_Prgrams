Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## copying and alias
>>> x={1:1,2:2,3:3}
>>> x
{1: 1, 2: 2, 3: 3}
>>> z=x.copy()
>>> z
{1: 1, 2: 2, 3: 3}
>>> x
{1: 1, 2: 2, 3: 3}
>>> z[4]=4
>>> z
{1: 1, 2: 2, 3: 3, 4: 4}
>>> x
{1: 1, 2: 2, 3: 3}
>>> x=z
>>> x
{1: 1, 2: 2, 3: 3, 4: 4}
>>> 
