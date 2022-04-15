import array as arr
import random
arr = arr.array('i', [0,0,0,0,0,0])
for i in range(5000):
    a=random.randint(1,6)
    arr[a-1]=arr[a-1]+1
    
for i in range(6):
    print("Percentage of throws of value {} = {:.2f}%".format(i+1,float(arr[i]*100/5000)))