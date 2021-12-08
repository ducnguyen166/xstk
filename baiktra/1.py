print("bài 1:")
import array as arr
a = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
b = []
for i in a:
    if(i < 30):
        b.append(i)
        print(b)
c = int(input("Nhập 1 số: "))
d = []
for i in a:
    if i < c:
        d.append(i)
        print(d)