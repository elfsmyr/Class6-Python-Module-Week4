def rollDice(number):
 import array as arr
 import random
 
 arr = arr.array('i', [0,0,0,0,0,0])
 for i in range(number):
      a=random.randint(1,6)
      arr[a-1]=arr[a-1]+1
       
 return arr