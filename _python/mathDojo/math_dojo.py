class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result += num
        for i in nums:
            self.result += i
        return self
    
    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for i in nums:
            self.result -= i
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)    # should print 5

y = md.add(100, 60, 40).subtract(10, 13, 54).result
print(y)

z = md.add(7098, 8932).subtract(541, 416).result
print(z)