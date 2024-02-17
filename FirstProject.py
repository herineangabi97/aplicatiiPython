#print('hello world')
#introduc un numar de la tastatura, si sa fac suma fi sa fac suma cifrelor'
print("Introduceti nr de la tastatura: ")
x=int(input())
print('Numarul citit de la tastatura este: ', x)
suma = 0;
while x:
    suma = suma + x%10
    x=int(x/10)
print(suma)

# print("Introduceti nr de la tastatura: ")
# x=input()
# print('Numarul citit de la tastatura este: ', x)
# suma = 0;
# for numar in str(x):
#     suma = suma + int(numar)
# print(suma)

