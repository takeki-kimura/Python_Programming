# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""

>>> 2 +2
4
>>> 5 - 2
3
>>> 50 - 5 * 6
20
>>> 5 *6
30
>>> (50 - 5) * 6
270
>>> 8 / 5
1.6

>>> 'a is {}' .format('a')
'a is a'

>>> 'a is {}' .format('test')
'a is test'

>>> 'a is {} {} {}'.format(1,2,3)
'a is 1 2 3'

>>> 'a is {0} {1} {2}'.format(1,2,3)
'a is 1 2 3'

>>> 'a is {2} {1} {0}'.format(1,2,3)
'a is 3 2 1'

>>> 'My name is {0} {1}'.format('Takeki','Kimura')
'My name is Takeki Kimura'

>>> 'My name is {0} {1}.watashi ha {1} {0}'.format('Takeki','Kimura')
'My name is Takeki Kimura.watashi ha Kimura Takeki'

>>> 'My name is {name} {family}.watashi ha {family} {name}'.format(name = 'Takeki',family = 'Kimura')
'My name is Takeki Kimura.watashi ha Kimura Takeki'

>>> 1
1
>>> '1'
'1'
>>> str(1)
'1'

>>> x = str(1)
>>> type(x)
<class 'str'>

>>> str(3.14)
'3.14'

>>> str(True)
'True'

a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
 
name = 'Takeki'
family = 'Kimura'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

>>> l = [1, 20, 4, 50, 2, 1, 2]
>>> l[0]
1
>>> l[1]
20
>>> l[-1]
2
>>> l[-2]
1
>>> l[0:2]
[1, 20]
>>> l[:2]
[1, 20]
>>> l[2:5]
[4, 50, 2]
>>> l[2:]
[4, 50, 2, 1, 2]
>>> l[:]
[1, 20, 4, 50, 2, 1, 2]
>>> len(l)
7
>>> type(l)

>>> list ('abcdefg')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> l[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> n = [1,2,3,4,5,6,7,8,9,10]
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n[::2]
[1, 3, 5, 7, 9]
>>> n[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a = ['a','b','c']
>>> n = [1,2,3]
>>> x = [a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[1]
[1, 2, 3]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> x[1][2]
3

#リストの操作
>>> s = ['a', 'b', 'c','d','e','f','g']
>>> s
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[0]
'a'
>>> s[0] = 'x'
>>> s[0]
'x'
>>> s[0]
'x'
>>> s
['x', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[2:5]
['c', 'd', 'e']
>>> s[2:5] = ['c', 'd', 'e']
>>> s
['x', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[2:5] = ['C', 'D', 'E']
>>> s
['x', 'b', 'C', 'D', 'E', 'f', 'g']
>>> s[2:5] = []
>>> s
['x', 'b', 'f', 'g']
>>> s[:] = []
>>> s
[]
>>> n = [1,2,3,4,5,6,7,8,9,10]
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n.append(1009)
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1009]
>>> n.insert(0,200)
>>> n
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1009]
>>> n.pop()
1009
>>> n
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n.pop(0)
200
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del n [0]
>>> n
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del n
>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> n = [1,2,2,2,3]
>>> n.remove(2)
>>> n
[1, 2, 2, 3]
>>> n.remove(2)
>>> n.remove(2)
>>> n
[1, 3]
>>> n.remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 

＃リストの結合

>>> a = [1,2,3,4,5]
>>> b = [6,7,8,9,10]
>>> a
[1, 2, 3, 4, 5]
>>> b
[6, 7, 8, 9, 10]
>>> x = a + b
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5]
>>> b
[6, 7, 8, 9, 10]
>>> a += b
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [1,2,3,4,5,]
>>> y = [6,7,8,9,10]
>>> x.extend(y)
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""