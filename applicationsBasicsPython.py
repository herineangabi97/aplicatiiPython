# input = " A string"
# for c in input:
#     if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#         print(c)
#     else:
#         continue

#Write a function that capitalizes the first and fourth letters of a name

# def myfunc(name):
#     first_letter = name[:3]
#     second_letter =name[3:]
#     return first_letter.capitalize() + second_letter.capitalize()
#
# text = input()
# print(myfunc(text))


#MASTER YODA: Given a sentence, return a sentence with the words reversed

# def master_yoda(text):
#     worldlist = text.split()
#     reserved_word_list =worldlist[::-1]
#     return ' '.join(reserved_word_list)
#
# print(master_yoda(' I am home'))

# def paper_doll(text):
#     result = ''
#
#     for char in text:
#         result += char*3
#     return result
#
# print(paper_doll('hello'))

# def has_33(num):
#     for i in range(0, len(num)-1):
#         if num[i] == num[i+1]:
#             return True
#     return False
#
# print(has_33([2,1,2,3]))
#
# string = 'Hello Mr Rogres'
# def num_Upper_Lowe(string):
#     d = {'Upper':0 , 'Lower':0}
#     for letter in string:
#         if letter.isupper():
#             d['Upper'] +=1
#         elif letter.islower():
#             d['Lower']+=1
#         else:
#             pass
#     print(d['Upper'])
#     print(d['Lower'])
# num_Upper_Lowe(string)
#
#
# def unique_list(lst):
#     list=[]
#     for num in lst:
#         if num not in list:
#             list.append(num)
#     return list
#
# print(unique_list([1,1,2,2,2,2,3,3,3,3,4,4,4]))



