"""
introdução try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

numero_float = float(numero_str)

print(f'o dobro de {numero_str} é {numero_float * 2:2.f}')

#uso do isdigit para iniciar o código se forem colocados apenas numeros pelo usuario
numero_str = input("Vou dobrar o número: ")
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:2.f}')
    
else:
    print('Isso não é numero valido')
"""
#f2 para trocar todas as aparições do que vai mudar o nome

numero_str = input("Vou dobrar o número: ")

try:
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:2.f}')
    ...
except:
    print('Isso não é um número válido')
    ...
