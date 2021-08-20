hen = '変数'
print(hen)
mo = '文字列'
print(mo)

s = 'test'
print(s)
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('Hello. \nHow are you?')
print(r'C:\name\name')

print("""
line1
line2
line3
""")

print("############")
print("""\
line1
line2
line3\
""")
print("############")

print('Hi.' * 3 + 'Mike.')

print('Py' + 'thon')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbb')
print(s)


moji = '文字列のインデックスとスライス'
print(moji)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('#############')
print(word[0:2])
print(word[:2])
print(word[2:])
print('#############')
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)

mes = 'メソッド'
print(mes)

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

print('#############')

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))