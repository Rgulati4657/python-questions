# program to check the Armstrong number
num = int(input('enter the number'))
sum =0
order =len(str(num))
copy_num = num
while(num>0):
    digit = num%10
    sum += digit**order
    num = num//10
if sum == copy_num:
    print(f'{copy_num} : this is  an armstrong number')
else:
    print(f'{copy_num} : this is not an armstrong number')

