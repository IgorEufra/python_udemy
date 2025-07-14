"""
Fatorial de um número:
1 -> 1*1
2 -> 2*factorial(1)
3 -> 3*factorial(2)
...
"""

# 1 - Fatorial de um número
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
number = int(input("Digite um número para o fatorial:\n"))
print(f"O fatorial de {number} é {factorial(number)}")

# 2 - Soma total de um número
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
num = int(input("Digite um número para a soma:\n"))
print(f"A soma total {num} é {total_sum(num)}")