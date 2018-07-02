n = int(input("please enter the number of fractions: "))
for i in range(n):
    x = int(input(" please enter your %d fraction",i))
    if i==1:
        sum = x
        print(x)
    else:
        sum += x
        print("+ ",x)
print("= +",sum)
        
        
