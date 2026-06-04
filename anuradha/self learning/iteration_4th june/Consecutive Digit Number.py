n = int(input("Enter a number: "))

temp = n
prev = temp % 10
temp = temp // 10
flag = True

while temp > 0:
    digit = temp % 10

    if prev - digit != 1:
        flag = False
        break

    prev = digit
    temp = temp // 10

if flag:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")