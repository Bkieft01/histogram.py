Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def histogram(word):
...     d=dict()
...     for char in word:
...         if char not in d:
...             d[char]=1
...         else:
...             d[char]+=1
...     return d
... 
