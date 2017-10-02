class MathDojo(object):
    def __init__(self):
        self.result = 0
        return None
    
    def add(self, *input):
        for i in input:
            if type(i) == int:
                self.result += i
            if type(i) == list:
                for k in i:
                    self.result += k
        return self
        
    def subtract(self, *input):
        for i in input:
            if type(i) == int:
                self.result += i
            if type(i) == list:
                for k in i:
                    self.result -= k
        return self

md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result


