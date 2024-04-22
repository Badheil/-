import copy
class BaseWallet:
    exchange_rate = 1
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return "Base Wallet {} {}".format(self.name, self.amount)
    def spend_all(self):
        if self.amount >= 0:
             self.amount = 0
            #  return self
    def to_base(self):
        return self.amount * self.exchange_rate

    def __add__(self, other): # a - b
        tmp = copy.copy(self)
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount += other.to_base() / self.exchange_rate
        else:
            tmp.amount += float(other)
        return tmp
    def __radd__(self, other): # 1 + b
        return self.__add__(other)
    def __iadd__(self, other):  # b += 1
        return self.__add__(other)


    def __sub__(self, other): # a - b
        tmp = copy.copy(self)
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount -= other.to_base() / self.exchange_rate
        else:
            tmp.amount -= float(other)
        return tmp

    def __rsub__(self, other):  # 1 - b 
        tmp = copy.copy(self)
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount = other.to_base() / self.exchange_rate - tmp.amount
        else:
            tmp.amount = float(other) - tmp.amount
        return tmp
    def __isub__(self, other):  # b -= 1
        return self.__sub__(other)


    def __mul__(self, other): # a * b
        tmp = copy.deepcopy(self)
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount *= other.to_base() / self.exchange_rate
        else:
            tmp.amount *= float(other)
        return tmp
    def __rmul__(self, other): # 1 * b
        return self.__mul__(other)
    def __imul__(self, other): # b *= 1
        return self.__mul__(other)


    def __truediv__(self, other): # a / b
        tmp = copy.deepcopy(self)
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount /= other.to_base() / self.exchange_rate
        else:
            tmp.amount /= float(other)
        return tmp
    def __rtruediv__(self, other): # 1 / b
        return self.__truediv__(other)
    def __itruediv__(self, other): # b /= 1
        return self.__truediv__(other)

    def __eq__(self, other): # a == b
        if (self.exchange_rate == other.exchange_rate) and (self.amount == other.amount):
            return True
        else:
            return False
    

class RubbleWallet(BaseWallet):
    exchange_rate = 1
    def __init__(self, name, amount):
        return super(RubbleWallet, self).__init__(name, amount)
    def __str__(self):
        return "Rubble Wallet {} {}".format(self.name, self.amount)

class DollarWallet(BaseWallet):
    exchange_rate = 60
    def __init__(self, name, amount):
        super(DollarWallet, self).__init__(name, amount)
    def __str__(self):
        return "Dollar Wallet {} {}".format(self.name, self.amount)

class EuroWallet(BaseWallet):
    exchange_rate = 70
    def __init__(self, name, amount):
        super(EuroWallet, self).__init__(name, amount)
    def __str__(self):
        return "Euro Wallet {} {}".format(self.name, self.amount)


D = DollarWallet("D", 15)
E = EuroWallet("E", 20)
R = RubbleWallet("R", 3)

# print("D ==", D)
# print("E ==", E)
# print("R ==", R)
# print("D + R ==", D + R)
# print("R - E ==", R - E)
# print("E - R ==", E - R)
# print("D - R ==", D - R)
# print("R - 1 ==", R - 1)
# print("1 - R ==", 1 - R)
# E -= 1
# print("E -= 1", E)
# E -= R
# print("E -= R", E)
    
# x + y __add__, x += y  __iadd__(self, other)
# x - y __sub__, x -= y  __isub__(self, other)
# x * y __mul__, x *= y  __imul__(self, other)
# x / y __truediv__, x /= y  __itruediv__(self, other)
# x // y __floordiv__, x //= y  __ifloordiv__(self, other)
# x % y __mod__, x %= y  __imod__(self, other)
# Рубль: 1
# Доллар: 60
# Евро: 7