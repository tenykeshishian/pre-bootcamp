#float to int
def num(arg:float)->int:
    return int(arg)
print(num(9.12))
print('-------------------')


#divisible
def divisible(x,y):
    if not x%y:
        print('True')
    else:
            print('False')
print(divisible(9,3))
print(divisible(11,2))
print('-----------------------')

#temprature
def temp(arg):
    return 9.5*float(arg)+32
temprature=float(input('Enter temprature:'))
print('temprature:',temp(temprature))
print('------------------------------------')               
    

def far_to_cel(temp):
    return 9.5*temp+32

print(far_to_cel(100))

print('--------------------------')

#math
def number(arg):
    import math
    return math.pow((math.pow(arg,4)*(math.pi)),5)
print(number(2))
print('---------------------------')


#volume
import math
r1=3
r2=5
v1=4/3*math.pi*r1**3
v2=4/3*math.pi*r2**3
print('pi(radius:3) = ',v1)
print('pi(radius:5) = ',v2)
print('---------------------------------')

# min and max
num=list(input('Enter three number:'))
print('max is:',max(num))
print('min is:',min(num))
print('-------------------------------------')

#password check
password=int(input('Enter password:'))
if password==int(1234):
    print('you have successful login.')
else:
    print('you have nott successul login!')


           
