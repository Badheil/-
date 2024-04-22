def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
class Calculator:
    last = None
    def __init__(self):
        self.history_arr = []

    def history(self, n):
        if n == 0:
            operation = self.history_arr[-1]
            for k, v in operation.items():
                key = k
                value = v
            s = "{} == {}".format(key, value)
            return s
        else:
            if n <= len(self.history_arr):
                operation = self.history_arr[-n]
                for k, v in operation.items():
                    key = k
                    value = v
                s = "{} == {}".format(key, value)
                return s
            else:
                return None
        
    def sum(self, a, b): # сложение a и b
        self.history_arr.append({f"sum({a}, {b})": a + b})
        Calculator.last = self.history(1)
        return a + b

    def sub(self, a, b): # вычитание
        self.history_arr.append({f"sub({a}, {b})": a - b})
        Calculator.last = self.history(1)
        return a - b

    def mul(self, a, b): # умножение
        self.history_arr.append({f"mul({a}, {b})": a * b})
        Calculator.last = self.history(1)
        return a * b

    def div(self, a, b, mod=False): # деление


        if mod:
            res = a % b
            self.history_arr.append({f"div({a}, {b})": res})
            Calculator.last = self.history(1)
            return res
        else:
            res = a / b
            ter = toFixed(res, 1)
            self.history_arr.append({f"div({a}, {b})": ter})
            Calculator.last = self.history(1)
            return res
    @classmethod
    def clear(cls): # очистка last
        cls.last = None     
        
# a = Calculator()
# b = Calculator()
# a.sum(8, 9)
# a.sub(100, 41)
# a.div(20, 9)
# a.mul(6, 7)
# b.div(7, 3)
# print(a.last)
# print(b.last)
# print(Calculator.last)
# print(a.history(1))
