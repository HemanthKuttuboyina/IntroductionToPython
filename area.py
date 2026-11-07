import math
import random
def circle_area(r):
    area = math.pi*r*r
    print(f"{area:.2f}")
print(circle_area(1.0))
print(circle_area(2.5))
# print(math.pi())
print(random.seed(3))