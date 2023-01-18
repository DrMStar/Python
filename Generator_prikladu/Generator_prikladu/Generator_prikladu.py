
import random

#pocet = input('Zadejte pocet prikladu')
pocet = 100
#inmin = input('Zadejte spodni limit vstupni hodnoty')
inmin = 0
#inmax = input('Zadejte horni limit vstupni hodnoty')
inmax = 10
#outmin = input('Zadejte spodni limit vysledku')
outmin = 0
#outmax = input('Zadejte horni limit vysledku')
outmax = 10
i=0

while i < pocet:
  ok = 0
  while ok < 1:
      #0 - scitani, 1 - odcitani, 2 - nasobeni, 3 - deleni
      operace = random.randint(0,1)
      
      #scitani
      if operace == 0:
          a = (random.randint(inmin,1000 * inmax)) // 1000
          b =  (random.randint(inmin,1000 * inmax)) // 1000
          if ((a+b)>=outmin and (a+b)<=outmax):
              print("{0} + {1} =".format(a, b))
              ok = 1
        
       #odcitani
      if operace == 1:
          a =  (random.randint(inmin,1000 * inmax)) // 1000
          b = (random.randint(inmin,1000 * inmax)) // 1000
          if ((a-b)>=outmin and (a-b)<=outmax):
              print("{0} - {1} =".format(a, b))
              ok = 1             
              
  i += 1

