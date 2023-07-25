
value = float(input('Input value of temperature: '))
temp = input('Temperature type (C, F): ')

if temp.lower() == 'c':
    print(f'Temperature = {value * 1.8 + 32} F.')
elif temp.lower() == 'f':
    print(f'Temperature = {(value - 32) / 1.8} C.')
