def print_table(n, i=1):
    if i <= 10:
        print(f"{n} * {i} = {n*i}")
        print_table(n, i+1)

n = int(input("ENTER THE NUMBER FOR THE MUL. TABLE: "))

print("YOUR TABLE IS:")
print_table(n)