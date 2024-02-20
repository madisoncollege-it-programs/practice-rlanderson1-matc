#!/usr/bin/env python3

""" Rae Denruiter
String Formatting"""

name = 'Timmy'
color1 = 'Red'
color2 = 'Green'
color3 = 'Blue'
number = 10.4516295
money = 10.45

# Output:  'Hello Timmy'
print(f'Hello {name}')
# Output:  'Red-Green-Blue'
print(f'{color1}-{color2}-{color3}')
# Output:  'Is this green or blue?'
print(f'Is this {color2.lower()} or {color3.lower()}?')
# Output:  'My name is TIMMY'
print(f'My name is {name.upper()}')
# Output:  '[++Red++]'
print(f'[++{color1}++]')
# Output:   '[green==]'
print(f'[{color2}==]')
# Output:  '[*****blue]'
print(f'[{"*" * 5}{color3}]')
# Output:  'BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue'
print(color3 * 10)
# Output:  '10.4516295'
print(f'{number}')
# Output:  '10.5'
print(f'{number:.1f}')
# Output:  'I have $10.45'
print(f'I have ${money:2f}')
#Output:  '[$$$Red$$$$] [$$Green$$$] [$$$Blue$$$]'
print(f'[$${color1}$$$$1] Second Color:[{color2}] Third Color:[{color3}]')

