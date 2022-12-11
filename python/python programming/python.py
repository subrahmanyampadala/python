arr=[]
count=1
for i in range(5):
    while count<6 :
        n=int(input('enter a postive number'))
        if n>0 :
            arr.append(n)
            count+=1
summ = sum(arr)
print(summ)
x = open("question1", "w")
print(summ, file=x)
x.close()