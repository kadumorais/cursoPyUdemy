#not inverte 
#no caso abaixo se não existe senha é false então invertemos o valor do teste para acusar quando false

senha = input('Senha')

if not senha:
    print('Você não digitou nada')