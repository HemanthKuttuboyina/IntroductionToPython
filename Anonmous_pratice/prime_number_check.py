class Prime:
    def __init__(self,v):
        self.val = v
    def check(self):
        # count = 0
        for i in range(2,self.val):
            if self.val % i == 0:
                return "Not a Prime"
        return "Prime Number"
            
num = int(input("ENter a num to check prime/not prime: "))
p = Prime(num)
print(p.check())