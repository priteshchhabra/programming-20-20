from fractions import Fraction
class instance:
    def __init__(self,n):
        self.n=n
    def instances(self):
        self.n = int(input("please enter the number of fractions: "))
        return(self.n)  
        
def compute():
    n = instance
    sum = 0
    for i in range(n.instances(n)):
        x = int(input(" please enter your %d fraction"%(i+1)))
        sum += 1/x
    return Fraction(sum.as_integer_ratio())
print(compute())    
