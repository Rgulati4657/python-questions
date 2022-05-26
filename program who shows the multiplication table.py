# to write a program who shows the multiplication table
num = int(input('enter the number of multiples'))
num2 = int(input('enter the table number '))
for i in range(1, num+1):
    nume = num2*i
    print("{0} x {1} = {2} ".format(num2, i, nume))
