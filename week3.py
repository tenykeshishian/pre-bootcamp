#mazrabe 4
for num in range(22,105):
    if not num%4:
        print(num,end=' ')

        
print('\n--------------------------------------')        
# mazrabe 5 hast vali mazrebe 3 nist
for i in range(200,20,-1):
    if not i%5 and i%3:
     print(i,end= ' ')

print('\n----------------------------------------')

#mazrabe 5 ya 6 bashad ba ham + konad 

lst=[y+z for y in range(123,567) for z in range(123,567) if not y%5 or not z%6]
print(lst)
print(sum(lst))
print('/n------------------------------------------')

#jadval zarbe adade 1-10
print('Multiplication table from 1 to 10:')
for i in range(1,11):
    print (i,'\n')
    for j in range(1,11):
        print(i*j,end='\t')

print('\n-----------------------------------------------')

#motvaziol azla

