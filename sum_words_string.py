# def sum_word_in_string(string):
#     counts=dict()
#     str_split=str.split(string)
#     for word in str_split:
#         if word in counts:
#             counts[word] +=1
#         else: 
#             counts[word]=1
#     return counts
# print(sum_word_in_string('babka, jajko,babka, kurczak'))

from collections import Counter

def sum_word_in_string(string):

    print(Counter(string))

print(sum_word_in_string('babka, jajko,babka, kurczak'))   



