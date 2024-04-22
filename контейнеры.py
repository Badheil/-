import re

class Field(dict):
   
    def __getitem__(self, key):
        k = self.find(key)
        if self.check(k):
            return super(Field, self).__getitem__(k)
        else:
            raise ValueError
    
    def __setitem__(self, key, value):
        if (type(key) == str or type(key) == tuple):
            k = self.find(key)
            if self.check(k):
                return super(Field, self).__setitem__(k, value)
            else:
                raise ValueError
        else:
            raise TypeError
    
    def __delitem__(self, key):
        k = self.find(key)
        return super(Field, self).__delitem__(k)
    
    def __missing__(self, key):
        return None       

    def __iter__(self):
        return iter(self.values())
    
    def __contains__(self, key):
        k = self.find(key)
        return self[k] != self.__missing__(k)
    
    @staticmethod
    def find(x):
        a = ''.join(str(i).lower() for i in x)
        index = 0
        for i in range(len(a)):
            if a[i].isalpha():
                index = i
        strr = a[index:len(a)] + a[0:index]
        return strr
    @staticmethod
    def check(x):
        pattern_en = re.compile(r'^([a-zA-Z]\d{1,}|\d{1,}[a-zA-Z])$')
        pattern_ru = re.compile(r'^([а-яА-Я]\d{1,}|\d{1,}[а-яА-Я])$') 
        if (pattern_en.match(x) or pattern_ru.match(x)):
            return True
        else:
            False

field = Field()
field['b', 2] = 100
print(field['2b'])

# a1 = "".join(str(i) for i in a).lower()
# b1 = "".join(str(i) for i in b).lower()
# c1 = "".join(str(i) for i in c).lower()
# a = [1, 'b']
# b = ['1B']
# print(frozenset(b))
# print('a1 ', a1)
# print('b1 ', b1)
# print('c1 ', c1)
# a = [1, 'b']
# b = ['b1']
# n = ['1b']
# s = "".join(str(i) for i in a)
# print(a)
# print(b)
# print(s)




     