# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[e]ntrar  [s]air ')
senha_digitada = input('senha: ')

senha_permitida = '123456'
if entrada == 'e' and senha_digitada == senha_permitida:
    print('entrar')
    
else:
    print('sair')
    
#avaliação de curto circuito    
print(True and False and True)
    
#or
senha = input('Senha: ') or 'Sem senha'
print(senha)