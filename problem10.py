# write a program to find gravitational force
G = 6.674 * (10 ** -11)   

m1 = float(input("Enter mass 1 (kg): "))
m2 = float(input("Enter mass 2 (kg): "))
r = float(input("Enter distance between them (m): "))

force = G * (m1 * m2) / (r ** 2)

print("Gravitational Force is:", force, "Newtons")
