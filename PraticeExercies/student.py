class Student:
    def __init__(self,name):
        self.name = name
        self.grade = []
    def add_grade(self,g):
        self.grade.append(g)
    def avg_compute(self):
        if len(self.grade) == 0:
            return 0
        avg = sum(self.grade)/len(self.grade)
        return avg
ana = Student("Ana")
for g in [12,14,20,40]:
    ana.add_grade(g)

print("Ana",ana.avg_compute())
ben = Student("Ben")
for g in [20,30,20,40]:
    ben.add_grade(g)
print("Ben",ben.avg_compute())
