from CRIPTOGRAFIA_V2 import Cripto


def Imput_dados():
    texto = input(
        'Digite a mensagem a ser encriptada ou decifrada: ')
    Todas_possibilidades = input(
        'Deseja utilizar todas as possibilidades de deslocamento(26)? Escolha S para Sim ou N para Não: ')
    Todas_possibilidades = Todas_possibilidades.upper()

    if Todas_possibilidades == 'N':
        chave = int(input(
            'Entre com o valor da chave (deslocamento): '))
        modo = input(
            'Escolha E para encriptar ou D para decriptar o texto: ')
    else:
        modo = input(
            'Escolha E para encriptar ou D para decriptar o texto: ')
        chave = 26

    c = Cripto(texto, chave, modo, Todas_possibilidades)
    print(c.criptografia_descriptografia())
    fechar = input(
        'Fechar o programa? S para(Sim) N(Continuar)'
    )
    resultado_imput = fechar.upper()
    return resultado_imput

resultado = Imput_dados()

if resultado == 'S':
    exit()
else:
    Imput_dados()
