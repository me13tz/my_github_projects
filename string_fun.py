import sys

d = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'nerd']
x = 0
w = []
l = []
for word in d:
    c = d[x]
    print(c)
    x+=1
print('...')
for i in range(len(d)):
    a = len(d)
    a -= 1
    z = d[a]
    w.append(z)
    d.pop()
    a -= 1
print(w)
print('...')
m = []
for i in range(len(w)):
    b = len(w)
    b -= 1
    l = w[b]
    m.append(l)
    w.pop()
    b -= 1
print (m)
print('...')
u = []
b = len(m)
for word in m:
    b -= 1
    u.append(m[b])
print()
print(u)
print()
print(m)
print()
str1=' '.join(m)
str2='.'.join(m)
str3='*'.join(m)
str4=''.join(m)
print()
print(str1)
print(str2)
print(str3)
print(str4)
print()
if 'heaven' in str2:
    print('Found it!')
print()
print(m)
for word in m:
    sys.stdout.write(word[-1]) ###prints it all on the same line, from a list

