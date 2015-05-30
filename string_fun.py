import sys
import random


s = "The quick brown fox jumps over the lazy nerd."
x = (s.lower())  ###place string in lowercase
rep = x.replace('.', '')  ###remove periods
d = list(rep.split(' '))  ###create list splitting words by white spaces
print(d)
x = len(d)
w = []
l = []
for word in d:
    c = d[x - 1]
    print(c)
    x -= 1  ###backwards and forwards...
print('........................................................................')
for i in range(len(d)):
    a = len(d)
    a -= 1
    z = d[a]
    w.append(z)
    d.pop()
    a -= 1
print(w)
print('........................................................................')
m = []
for i in range(len(w)):
    b = len(w)
    b -= 1
    l = w[b]
    m.append(l)
    w.pop()
    b -= 1
print(m)
print('........................................................................')
u = []
b = len(m)
for word in m:
    b -= 1
    u.append(m[b])

print(u)
print('........................................................................')
print(m)
print('........................................................................')
str1 = ' '.join(m)  ###join list in a string using spaces
str2 = '.'.join(m) ###join list in a string using periods
str3 = '*'.join(m) ###join list in a string using stars
str4 = ''.join(m)  ###join list using nothing
print()
print(str1)
print(str2)
print(str3)
print(str4)
print('........................................................................')
b = random.sample(m, len(m)) ###randomize the contents of the list
print(b)
random.shuffle(b) ###randomize again
print(b)
b.reverse()  ### reverse the mess
print(b)

for word in b:
    sys.stdout.write(word[-1]) ###prints last letter of randomized list elements on the same line
