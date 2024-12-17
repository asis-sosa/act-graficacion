num = int(input("Enter the number of rows:"))

for n in range(num):
    print(" " * (num - n), end="")

    print(" ".join(map(str, str(11 ** n))))