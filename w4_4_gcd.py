import math
n=int(input())
list=[]
i=0
while i<n: 
    try:
      number=int(input())   
      list.append(number) 
      i=i+1
    except ValueError:
      print('Check if input string is parsable integer')
      
    
print(math.gcd(*list))


