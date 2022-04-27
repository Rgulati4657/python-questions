# to find the largest among three numbers
# let x,y,z
x = int(input('Enter the first Number'))
y = int(input('Enter the second Number'))
z = int(input('Enter the third Number'))
if x > y and x > z:
    print('{} is the greatest number'.format(x))
elif y > x and y > z:
    print('{} is the greatest number'.format(y))
elif z > y and z > x:
    print('{} is the greatest number'.format(z))
elif x==y==z:
    print('{}you entered same number'.format(x))
elif x==y and x<z:
    print('{}is the greatest number number'.format(z))
elif y==x and x>z:
    print('{}is the greatest number number'.format(x))
elif y == z and y > x:
    print('{}is the greatest number number'.format(y))
elif y == z and y < x:
    print('{}is the greatest number number'.format(x))
elif x == z and z > y:
    print('{}is the greatest number number'.format(x))
elif x == z and z < y:
    print('{}is the greatest number number'.format(y))










