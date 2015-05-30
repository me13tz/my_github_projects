nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 0
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
for i in nums:
    q = i**2
    r = i**3
    s = i**4
    t = i**5
    u = i**6
    v = i**7
    w = i**8
    x = i**9
    a.append(q)
    b.append(r)
    c.append(s)
    d.append(t)
    e.append(u)
    f.append(v)
    g.append(w)
    h.append(x)
    print(str(nums[m])+" squared =    "+str(q))
    print(str(nums[m])+" cubed =      "+str(r))
    print(str(nums[m])+" to the 4th = "+str(s))
    print(str(nums[m])+" to the 5th = "+str(t))
    print(str(nums[m])+" to the 6th = "+str(u))
    print(str(nums[m])+" to the 7th = "+str(v))
    print(str(nums[m])+" to the 8th = "+str(w))
    print(str(nums[m])+" to the 9th = "+str(x))
    print()
    m += 1

print("The sum of the first nine squares is:  "+str(sum(a)))
print("The sum of the first nine cubes is:    "+str(sum(b)))
print("The sum of the first nine powers of 4: "+str(sum(c)))
print("The sum of the first nine powers of 5: "+str(sum(d)))
print("The sum of the first nine powers of 6: "+str(sum(e)))
print("The sum of the first nine powers of 7: "+str(sum(f)))
print("The sum of the first nine powers of 8: "+str(sum(g)))
print("The sum of the first nine powers of 9: "+str(sum(h)))
