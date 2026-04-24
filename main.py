a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a > b) and (a > c):
    print(f"Largest number a is {a}")
elif (b > a) and (b > c):
    print(f"Largest number b is {b}")
else:
    print(f"Largest number c is {c}")