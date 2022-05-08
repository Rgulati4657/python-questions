# program to find the Armstrong Number in an Interval
num1 = int(input('enter the first number of interval: '))
num2 = int(input('enter the last number of interval: '))
for num in range(num1,num2+1):
    order = len(str(num))
    sum = 0
    temp = num
    while (temp >0):
        digit = temp % 10
        sum += digit ** order
        temp = temp // 10
    if sum == num:
        print(num)







