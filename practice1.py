#2. Write a Python program to print all disarium numbers between 1 to 100?
for i in range(1,101):
    Number = i
    length = len(str(Number))

    Temp = Number
    Sum = 0
    rem = 0

    while Temp > 0:
        rem = Temp % 10
        Sum = Sum + int(rem**length)
        Temp = Temp // 10
        length = length - 1

    print("The Sum of the Digits = %d" %Sum)

    if Sum == Number:
        print("\n%d is a Disarium Number." %Number)
    else:
        print("%d is Not a Disarium Number." %Number)