# program to print the Fibonacci sequence
num = int(input('how many  terms'))
n1, n2 = 0, 1
i = 0
if num<= 0 :
    print('enter a positve number')
while i < num:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    i += 1
