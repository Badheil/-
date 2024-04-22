string_inp = input()
pod_str = input()
word_list = string_inp.split()
for i, word in enumerate(word_list):
    if word == " ":
        word_list.pop(i)
word_str = " ".join(word_list)
print(word_str)