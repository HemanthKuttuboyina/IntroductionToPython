class Table:
    def __init__(self,tb):
        self.table = tb
    def Print_table(self):
        for i in range(21):
            print(f"{self.table} x {i} = {self.table*i}")
print(Table(7).Print_table())