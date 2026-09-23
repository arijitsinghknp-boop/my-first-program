a=[]
b=[]
n=int(input("enter no of numbers"))
for i in range(n):
     item=int(input("enter a no."))
     a.append(item)
for j in range(len(a)-1,-1,-1):
     b.append(a[j])
print("the reversed list is",b)