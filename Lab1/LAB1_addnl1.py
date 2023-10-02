n = int(input("Enter the start (n): "))
m = int(input("Enter the end (m): "))

if(m<n):
    print("value of m not possible")
    exit()
print(f"Numbers between {n} and {m}:")
for num in range(n + 1, m):
    print(num, end=' ')

