class FizzBuzz:
    def __init__(self,r):
        self.rag = r
    def fizzbuzz(self):
        for i in range(1,self.rag+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", end=" ")
            elif i % 3 == 0:
                print("Fizz",end=" ")
            elif i % 5 == 0:
                print("Buzz",end=" ")
            else:
                print(i,end=" ")
ip = int(input("N: "))
p1 = FizzBuzz(ip)
p1.fizzbuzz()