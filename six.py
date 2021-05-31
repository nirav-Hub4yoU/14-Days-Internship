num = int(input("Enter a Number  :"))

factorial = 1
if num < 0:
    print("Factorial Does not exist ")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The Facorial of ", num, "is ", factorial)
