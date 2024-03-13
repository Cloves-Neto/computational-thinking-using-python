''' Operadores lógicos em python

< MAIOR
> MENOR
>= MENOR IGUAL A
<= MAIOR IGUAL A
== IGUA A
!= DIFERENTE DE
'''

a = 9
b = 10



print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a < b)
print(a > b)

''' No caso de palavras o operador vai comparar a ordem alfabetica da string'''

#Verificar se uma pessoa é maior de idade:

idade = int(input("Informe qual é a sua idade: "))
print(f'Maior de idade? { idade >= 18}')


