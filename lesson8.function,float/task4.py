def water(result):
    return f'''"КлирВотер"."ВодЗавод". {result}р.'''

for name in range(3):
   price = int(input("Enter the price: "))
   print(water(price))



