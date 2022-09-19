a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a<b+c:
    print("Треугольник существует")
elif b<a+c:
    print("Треугольник существует")
elif c < a + b:
    print("Треугольник существует")
else:
    print("Треугольник не 5существует")
