numbers = []

for i in range(7):
    n = int(input(f"Enter integer {i + 1}: "))
    numbers.append(n)

smallest = numbers[0]
largest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("Smallest =", smallest)
print("Largest =", largest)