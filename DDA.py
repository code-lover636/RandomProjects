import matplotlib.pyplot as plt

x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

Dx = x1-x0
Dy = y1-y0
m = Dy/Dx

if abs(Dx) >= abs(Dy): steps = abs(Dx)
else: steps = abs(Dy) 

Xincrement = Dx/float(steps)
Yincrement = Dy/float(steps)

V = 0
x = []; y = []
while V<steps:
    x0 += Xincrement
    y0 += Yincrement
    x.append(x0); y.append(y0)
    print(f"X0:{round(x0)}, Y0:{round(y0)}")
    V +=1

plt.plot(x,y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("DDA Algorithm")

plt.show()