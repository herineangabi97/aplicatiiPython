#Polulatie bacterii se dubleaza pe timp de zi si se injumatatesc pe timp de noapte
#Cu cat se inmultesc dupa z zile?
from typing import Tuple

# h1= int(input('Ore de zi:'))
# h2= int(input('Ore de noapte:'))
# z= int(input('ZILE:'))
# bacterii= ((h1*2) - (h1/2)) * z
# print(bacterii)



# def is_even_odd(x:int):
#     if x%2 == 0:
#         return 'The number is even'
#     else:
#         return "The number is odd"
#
# numar = int(input("numar de la tastatura: "))
# mesaj = is_even_odd(numar)
# print(mesaj)
# print(is_even_odd(numar))


# Print numbers using for loop from a to b number

# def printNumbers(a:int, b:int):
#     for num in range(a,b,1):
#         print(num)
#
# x=int(input("citeste a: "))
# y=int(input("citeste b: "))
# printNumbers(x, y)


# Write a program that calculates the factorial of a number using a while loop.

# def factorial(x:int):
#     rezultat=1
#     while x>0:
#         rezultat= rezultat * x
#         x=x-1
#     return rezultat
#
# a = int(input("numar de la tastatura: "))
# print("factorialul numarului",a,"este : ", factorial(a))


# Create a list of your favorite foods and print each item in the list.
# def lista(lista:list):
#     for item in lista:
#         print(item)
#
# num=int(input('numar de iteme in lista: '))
# lst=[]
# for i in range(0,num):
# #     word= input("mancare preferata: ")
# #     lst.append(word)
# lista(lst)



# Write a program that finds the largest number in a list.

# def LargestNumer(lista:list):
#      maxim = 0
#      for item in lista:
#          if int(item) > maxim:
#             maxim = int(item)
#      return maxim
# num=int(input('numar de iteme in lista: '))
# lst=[]
# for i in range(0,num):
#     numar= int(input("numere aleatorii: "))
#     lst.append(numar)
#
# print(LargestNumer(lst))



#Write a function that takes two numbers as parameters and returns their sum.
# def TwoNumber(a:int, b:int):
#     print(a+b)
# x=int(input("Insert first number: "))
# y=int(input("Insert second number: "))
# TwoNumber(x,y)



#Write a function that takes a list of numbers as a parameter and returns the average.
# def lista(lista:list):
#     sum=0
#     for item in lista:
#         sum = (sum + int(item))
#     print("media aritmetica  ", sum / len(lista))
#
# num=int(input('numar de iteme in lista: '))
# lst=[]
# for i in range(0,num):
#      numar= int(input("numere aleatorii: "))
#      lst.append(numar)
# lista(lst)



# Write a program that counts the number of vowels in a string.
# def Vocale(a:str):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     vocale=[]
#     for character in string:
#         if character in vowels:
#             count += 1
#             vocale.append(character)
#         else:
#             continue
#     vocale.sort()
#     vocale_sorate= vocale
#
#     print("Se afiseaza numarul de vocale", count)
#     print("Se afiseaza vocalele: ", vocale_sorate)
# string = input("introduceti caractere: ")
# Vocale(string)



#Write a program that reverses a string.

# def stringReverse(string,str):
#     print("Reversed string: " ,text[::-1])
#
# text = str(input("Insert string : "))
# stringReverse(text,str)


#Create a dictionary of words and their meanings.

# my_dict= {"fructe" : "mere",
#           "legume" : "morcovi",
#           "citrice" : "mandarine"}
# key_dict= my_dict.keys()
# item_dict=my_dict.items()
# print(my_dict)
# print(key_dict)
# print(item_dict)
# print(len(my_dict))
# print('These are the key objects : ', (my_dict["legume"]), my_dict["citrice"], my_dict["fructe"])


#Write a program that creates a tuple containing the names of your favorite fruits.
# my_tuple=("apples", "orange", "strawberry")
# print(my_tuple)
# print(my_tuple[2])
#
# #Tuple Unpacking
# my_tuple1= ("Gabi" , 21)
# (name, age)=my_tuple1
# print(name)
# print(age)
#
# # concatenation of tuple
# tuples= my_tuple + my_tuple1
# print(tuples)


# #Create a tuple containing the numbers from 1 to 10. Use slicing to print only the even numbers from the tuple.
# num_pare = []
# num_impare=[]
# for num in range(0,10,1):
#     if num%2 == 0:
#         num_pare.append(num)
#     else:
#         num_impare.append(num)
# tuple_pare = tuple(num_pare)
# tuple_impare = tuple(num_impare)
# print(tuple_pare)
# print(tuple_impare)

#Create two tuples containing the same elements but in different orders. Write a program to compare whether the two tuples are equal.

# Tuple_1 = (1,2,3,4)
# Tuple_2 = (3,2,4,1)
# sorted_ = tuple(sorted(Tuple_2))
# print(Tuple_1 == sorted_)

#Write a program using function that calculate sum and multiple of 2 numbers and print them in a tuple

# def SumProd (a:int , b:int):
#     result= []
#     result_tuple=()
#     result.append(a+b)
#     result.append(a*b)
#     result_tuple= tuple(result)
#     print(result_tuple)
# SumProd(2,3)
# SumProd(7,8)

#write a program that print integers from 0 to 100 and print multiples of 3 print Fizz for multiple of 5 print Buzz and for both FizzBuzz

# for num in range(0,31,1):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#         continue
#     elif num % 5 ==0:
#         print("Buzz")
#         continue
#     else:
#         print(num)



