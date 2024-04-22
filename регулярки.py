import re
def check_string(string): # return boolean
    pattern_phone =re.compile("^((\+7)|7|8)?[ (-]{0,2}(\d{3})[ )-]{0,2}(\d{3})(\-)?(\d{2})(\-)?(\d{2})$")
    pattern_email = re.compile("^(\w+)(\.)?(\w+)?(@){1}(\w){2,}(\.)(\w){2,}(\.\w{2,})*$")
    if pattern_phone.match(string) or pattern_email.match(string):
        return True
    return False

print(check_string(input()))

# check_string("")
# s = []
# re.compile(r'[+789.d{3}.)][0-9]{10}')

# phones = [
# "+79160000000",
# "7960000000",
# "89160000000",
# "9160000000",
# "8(916)000-00-00",
# "+7(916)000-00-00",
# "(916)000-00-00",
# "8-(916)-000-00-00",
# "+7 (916) 000-00-00",
# "(916) 000-00-00",
# "8(916)0000000",
# "+7(916)0000000",
# "(916)0000000",
# "8-916-000-00-00",
# "+7-916-000-00-00",
# "916-000-00-00"]
# emails = [
# # Валидным адресом электронной почты будем считать строки, содержащие @ 
# # и не меньше одной точки (после точки - не меньше двух символов), например:
# "abc@abc.ab",
# "abc@abc.ab.ab",
# "a@ab.ab",
# "abc.abc@abc.abc",
# "Невалидные адреса",
# "@abc.abc",
# "abc@abc",
# "abc@abc.a",
# "abc@abc.abc.a",
# "abc@abc.",
# "abc@abc@abc"]
# ret = (*phones, *emails)
# print(ret)
# #?.*[+78]?[\-\(](\d{3})[\-\)]?(\d{3})[\-\(]?(\d{2})[\-\(]?(\d{2})[\d{10}]
# pattern_phone =re.compile("^(\+)?[78]?[ (-]{0,2}(\d{3})[ )-]{0,2}(\d{3})(\-)?(\d{2})(\-)?(\d{2})$")
# pattern_email = re.compile("^(\w+)(\.)?(\w+)?(@){1}(\w){2,}(\.)(\w){2,}(\.\w{2,})*$")
# for i in ret:
#     if pattern_phone.match(i) or pattern_email.match(i):
#         print(i, 'yes', sep="\t")
#     else:
#         print(i, 'no', sep="\t")