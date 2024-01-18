"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

Hinput = int(input("Que horas são? "))


if Hinput >= 0   or Hinput <= 11:
    print(f'Bom dia! {Hinput}')
    
elif 12 >= Hinput or 17 <= Hinput:
    print(f'Boa tarde! {Hinput}')
    
elif 18 >= Hinput or 23 <= Hinput:
    print(f'Boa noite! {Hinput}')  