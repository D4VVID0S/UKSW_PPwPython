import numpy as np

a = [1,2,3,4]
print("Tablica a to: ", a)
a[2]
print("Drugi element tablicy a to:", a[2])

b = np.array([[5,6,7,8], [3,5,6,7]])
print("Tablica b to:", b)

c = b[0]
print("Tablica c to i zerowy element tablicy b to:", c)

d = c[0]
print("Zerowy element tablicy c oraz d to: ", d)
print("Czy d = c[0]?", d == c[0])

e = (b[0])[0]
print("Czy e jest rowne c[0]?", e == c[0])

f = [[1,2,3,4], [1,2,3,4]]
# tak mozna wyciagac bardziej zagniezdzone elementy w listach
f[0][3]
