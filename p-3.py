
for num in range(1,3137204):
    if num % num == 0 and num % 1 == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 or num == 2 or num == 3 or num == 5 or num == 7:
        print(num)
        print("this is a prime number..")
    else:
        print(num)
        print("this is not a prime number..")

