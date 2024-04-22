import re

class Field(dict):

    def __getitem__(self, key):
        k = self.find(key)
        if self.check(k):
            return super(Field, self).__getitem__(k)
        else:
            raise ValueError()
    
    def __setitem__(self, key, value):
        if (type(key) == str or type(key) == tuple):
            k = self.find(key)
            if self.check(k):
                return super(Field, self).__setitem__(k, value)
            else:
                raise ValueError()
        else:
            raise TypeError()
    
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

    def __getattribute__(self, key):
        k = key.lower()
        return super().__getattribute__(k)
 
    def __getattr__(self, key):
        k = key.lower()
        return super(Field, self).__getitem__(k)

    def __setattr__(self, key, value):
        k = key.lower() 
        if self.check(k):
                return super(Field, self).__setitem__(k, value)
        else:
            return super().__setattr__(k, value)

    def __delattr__(self, item):
        k = item.lower()
        if self.check(k):
            return super(Field, self).__delitem__(k)
        else:
            return super(Field, self).__delattr__(k)
    @staticmethod
    def find(x):
        a = ''.join(str(i).lower() for i in x)
        index = 0
        for i in range(len(a)):
            if a[i].isalpha():
                index = i
                break
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

# field = Field()
# field['a1'] = 100
# field['b3'] = 23
# field.b123 = 3
# field.B1 = 25
# field.abcd5432e = 125
# field.abcde = 125
# field.ASD321Fsd = 3
# print(field)
# print(field.__dict__)
# del field.a1
# print(field.abcde, field.__dict__['abcde'] == 125)
# print(field)
# print(field.__dict__)