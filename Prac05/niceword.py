__author__ = 'jc444921'

text = input("Text: ")
word_list = text.split()

count_dict={}
for word in text.split():
    if word in count_dict:
      count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)

for key, value in count_dict.items():
    print(key, value)
