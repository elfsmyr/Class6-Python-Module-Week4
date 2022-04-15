import my_dice 
arr=[]
n=int(input())
arr=my_dice.rollDice(n)
for i in range(6):
    print("Percentage of throws of value {} = {:.2f}%".format(i+1,arr[i]*100/n))