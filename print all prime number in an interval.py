# to print all prime number in an interval....
num1 = int(input('enter the first number... :'))
num2 = int(input('enter the last number... :'))
for num in range(num1,num2+1):
    if num >1:
        for i in range(2,num):
            if num % i == 0:
                # print(' not a prime')
                break
        else:
            print("{0} this is prime".format(num))
