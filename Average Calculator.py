print("Enter numbers to find their average!")
print("Enter '0' when done")

x = int(input("First number: "))
y = 1
w = 0

while y != 0:
    y = int(input("next: "))
    z = x + y
    x = z
    w = w + 1

print(z/w)