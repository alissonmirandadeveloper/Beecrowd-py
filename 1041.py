e = input()
v = e.split(" ")
x = float(v[0])
y = float(v[1])

if x == 0.0 and y == 0.0:
    print("Origem")
elif x != 0.0 and y == 0.0:
    print("Eixo X")
elif x == 0.0 and y != 0.0:
    print("Eixo Y")
elif x > 0.0 and y > 0.0:
    print("Q1")
elif x < 0.0 and y > 0.0:
    print("Q2")
elif x < 0.0 and y < 0.0:
    print("Q3")
elif x > 0.0 and y < 0.0:
    print("Q4")