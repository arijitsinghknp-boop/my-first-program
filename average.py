a=[]
#user input
for i in range(10):
    item=int(input("enter a no."))
    a.append(item)
sum=0
#calculating sum
for j in a:
    sum=sum+j
print("sum of numbers",sum)
#calculating average
average=sum/10
print("average of numbers are",average)