from math import sqrt
print("Giải phương trình bậc 2 : ax^2 +bx + C =0 ")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm!")
                else:
                if c == 0:
                    print("Phương trình có một nghiệm x = 0")
                    else:
                        print("Phương trình có một nghiệm x =", -c/b)
                        else
                        delta = b** 2-4 ** a * c
                        if delta <0:
                            print("Phương trình vô nghiệm!")
                            elif delta == 0:
                            print("Phương trình có 1 nghiệm x =", -b/(2 *a))
                                else:
                                print("Phương trình có 2 nghiêm phân biệt!")
                                print(float((-b - sqrt(delta))/ (2 * a)))
                                print(float((-b + sqrt(delta))/ (2 * a)))