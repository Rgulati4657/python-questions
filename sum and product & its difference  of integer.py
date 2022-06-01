# program to check the sum ,product and its difference of  an integer
# num = '234'
num = input("enter a number")
sum = 0
product = 1
for i in num:
    # print(int(i))
    sum = sum+int(i)
    product = product* int(i)

print('the sum is :',sum)
print('the product is :',product)
print('the difference is :',product - sum)
