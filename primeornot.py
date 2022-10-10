# Program to check if a number is prime or not
# prime numbers are greater than 1
# If the number is less than 1, its also not a prime number.

num = int(input("Enter a number: "))
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
	print(num, "is not a prime number")