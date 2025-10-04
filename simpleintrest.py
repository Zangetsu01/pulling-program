
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))


si = (p * r * t) / 100


a = p * (1 + r/100) ** t
ci = a - p


print("\nResults ")
print("Simple Interest =", si)
print("Compound Interest =", ci)
print("Total Amount with Compound Interest =", a)
