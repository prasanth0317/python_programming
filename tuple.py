Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
subjects=("PP LAB","DBMS LAB","COM LAB","SDC LAB")

print(subjects)
('PP LAB', 'DBMS LAB', 'COM LAB', 'SDC LAB')
favorite_color=("orange")
print(favorite_color)
orange
good_hero("jrntr")

good_heros("jrntr")

good_hero=("jrntr")
print(good_hero)
jrntr
print(type(good_hero))
<class 'str'>
heros=tuple(("prabhas","jrntr","maheshbabu","ramcharan","jaibalaya")
            heros
            
SyntaxError: incomplete input

heros=tuple(("prabhas","jrntr","maheshbabu","ramcharan","jaibalaya"))
            
heros
            
('prabhas', 'jrntr', 'maheshbabu', 'ramcharan', 'jaibalaya')
heros=tuple(["jrntr","prabhas'])
             
SyntaxError: incomplete input
heros=tuple(["jrntr","prabhas"])
             
heros
             
('jrntr', 'prabhas')
fruits=("apple","cherry","apple","berry")
             
print(fruits)
             
('apple', 'cherry', 'apple', 'berry')
fruits[2]="banana'
             

fruits[2]="banana
             

fruits[2]="banana"
             

fruits[2]="banana"
             
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fruits[2]="banana"
TypeError: 'tuple' object does not support item assignment
fruits=("apple","cherry","apple","berry")
             
print(fruits)
             
('apple', 'cherry', 'apple', 'berry')
fruits[-1]
             
'berry'
fruits[-2]
             
'apple'
fruits[-3]
             
'cherry'
fruits[-4]
             
'apple'
name=("prasanth","alluarjun","prabhas")
             
rno=(105,03,17)
             
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
rno=(105,33,17)
             
print(name+rno)
             
('prasanth', 'alluarjun', 'prabhas', 105, 33, 17)
students=(name,rno)
             
print(students)
             
(('prasanth', 'alluarjun', 'prabhas'), (105, 33, 17))
subj=("AI",)*3
             
subj
             
('AI', 'AI', 'AI')
best_heros=('prabhas','jrntr','maheshbabu','ramcharan','jaibalaya')
             
print(best_heros[:3])
             
('prabhas', 'jrntr', 'maheshbabu')
print(best_heros[1:])
             
('jrntr', 'maheshbabu', 'ramcharan', 'jaibalaya')
print(best_heros[::-1])
             
('jaibalaya', 'ramcharan', 'maheshbabu', 'jrntr', 'prabhas')
print(best_heros[1:5])
             
('jrntr', 'maheshbabu', 'ramcharan', 'jaibalaya')
print(best_heros[::-2])
             
('jaibalaya', 'maheshbabu', 'prabhas')
del best_heros
             
print(best_heros)
             
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(best_heros)
NameError: name 'best_heros' is not defined
prasanth=("good students",true,25)
             
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    prasanth=("good students",true,25)
NameError: name 'true' is not defined. Did you mean: 'True'?
prasanth=("Good students",True,25)
             
print(len(prasanth))
             
3
print(prasanth)
             
('Good students', True, 25)
marks=[23,22,20,22,25]
             
print(tuple(marks))
             
(23, 22, 20, 22, 25)
letters=('a','b','c','d','a','d','c')
...              
>>> letters.count('c')
...              
2
>>> letters.count('a')
...              
2
>>> letters.count('b')
...              
1
>>> for i in range(len(letters)):
...              if letters[i]=='c':
...              print(i)
...              
SyntaxError: expected an indented block after 'if' statement on line 2
>>> for i in range(len(letters)):
...      if letters[i]=='c':
...              print(i)
... 
...              
2
6
