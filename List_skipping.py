numbers = []

while True:
    raw = input("Enter a number: ").strip()

    if raw.lower() == "exit":
        break

    if not raw:  
        continue

    try:
        num = int(raw)
        numbers.append(num)
    except ValueError:
        print("Enter a valid integer.")

print(numbers[1::5])
print(numbers[1::2])