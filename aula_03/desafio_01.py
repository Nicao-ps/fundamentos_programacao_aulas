print('\n'+(89*'='))
print((18*' ')+'Welcome to the freight cost calculator! (Version 1.0)'+(18*' '))
print((89*'=')+'\n')

distance = float(input('Please enter the distance to be covered in km: '))

print('\n'+'Calculating freight cost... Please wait.')

if distance > 10.0:
    print('\n'+'Sorry, we do not deliver to distances over 10 km.')
elif distance > 5.0:
    freight_cost = 10.00
    print('\n'+f'The freight cost for {distance:.2f} km is R$ {freight_cost:.2f}.')
elif distance > 0.0:
    freight_cost = 5.00
    print('\n'+f'The freight cost for {distance:.2f} km is R$ {freight_cost:.2f}.')
else:
    print('\n'+'Invalid distance input. Please enter a positive float number.')

print('\n'+((35*'=')+' Ending Aplication '+(35*'='))+'\n')
