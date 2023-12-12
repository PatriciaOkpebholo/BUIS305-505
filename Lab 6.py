
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    num = int(input("Enter a number: "))
    if num> 0:
        break
    else:
        print("Wrong input, enter number >0")

if num % 2 == 0:
    print(f"{num} is an even number", end=" ")
else:
    print(f"{num} is an odd number", end=" ")

if is_prime(num):
    print("and it is prime.")
else:
    print("and it is nonprime.")
