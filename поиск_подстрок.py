string_inp = input()
sub_str = input()
string_list = string_inp.split()

low_sub_str = sub_str.lower()
for word in string_list:
    if low_sub_str in word.lower():
        print(word)