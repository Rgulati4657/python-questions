# find the sum of natural numbers
num = int(input('enter a positive number :'))
if num<=0:
    print('enter a positive number plz')
else:
    sum = 0
    while (num>0):
        sum+=num
        num-=1
print(f"this is sum : {sum} " )
























# this  is an alternate method
"""num = int(input('enter a positive number :'))
result = num*(num+1)/2
print(result)"""
