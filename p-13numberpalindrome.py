n = "123"
length = len(n)

for i in range(len(n)):
    n = n + n[length -1 -i]
print(n)
