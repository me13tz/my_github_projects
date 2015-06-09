f = open('C:\\Users\blahblah\blahblah\blahblah\blahblah\output.txt', 'w')

for i in range(1, 4004):
    i = str(i)
    if len(i) == 1:
        w = (i + " + " + i + " = " + str(int(i)+int(i))+ '\n')
        print(w)
        f.write(w)
    if len(i) == 2:
        db = i[::-1]
        x = (i + " + " + db + " = " + str(int(i)+int(db))+ '\n')
        print(x)
        f.write(x)
    if len(i) == 3:
        tr = i[::-1]
        y = (i + " + " + tr + " = " + str(int(i)+int(tr))+ '\n')
        print(y)
        f.write(y)
    if len(i) == 4:
        qu = i[::-1]
        z = (i + " + " + qu + " = " + str(int(i)+int(qu))+ '\n')
        print(z)
        f.write(z)
f.close()


