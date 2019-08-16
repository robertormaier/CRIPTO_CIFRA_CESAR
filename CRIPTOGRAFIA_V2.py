class Cripto:

    def __init__(self, texto, chave, modo, Todas_possibilidades):
        self.texto = texto
        self.chave = chave
        self.modo = modo
        self.Todas_possibilidades = Todas_possibilidades

    def criptografia_descriptografia(self):
      
        CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        convertido = ''
        texto_convertido = ''
  
        texto = self.texto.upper()
        modo = self.modo.upper()
        chave = self.chave
        Todas_possibilidades = self.Todas_possibilidades.upper()

        if Todas_possibilidades == 'S':
            Contador = 1
            chave = 1
            while Contador <= 26:
                for caractere in texto:
                    if caractere in CARACTERES:
                        num = CARACTERES.find(caractere)
                        if modo == 'E':
                            num = num + chave
                        elif modo == 'D':
                            num = num - chave
                        if num >= len(CARACTERES):
                            num = num - len(CARACTERES)
                        elif num < 0:
                            num = num + len(CARACTERES)
            
                        convertido = convertido + CARACTERES[num]
                    else:
                        convertido = convertido + caractere
               
                if modo == 'E':
                    texto_convertido = print(
                        'O texto criptografado é ', convertido, ' Chave ', str(chave))
                if modo == 'D':
                    texto_convertido = print(
                        'O texto criptografado é ', convertido, 'Chave ', str(chave))
                Contador = Contador + 1
                chave = chave + 1
                convertido = ''
            return texto_convertido
        elif Todas_possibilidades == 'N':          
            for caractere in texto:
                if caractere in CARACTERES:  
                    num = CARACTERES.find(caractere)
                    if modo == 'E':
                        num = num + chave
                    elif modo == 'D':
                        num = num - chave
                    if num >= len(CARACTERES):
                        num = num - len(CARACTERES)
                    elif num < 0:
                        num = num + len(CARACTERES)
                    convertido = convertido + CARACTERES[num]
                else:
                    convertido = convertido + caractere
            
            if modo == 'E':
                texto_convertido = print(
                    'O texto criptografado é ', convertido)
            if modo == 'D':
                texto_convertido = print(
                    'O texto decriptado é ', convertido)
        else:
            texto_convertido = print(
                'Não conseguimos criptografar, verifique os parametros digitados ')
        return texto_convertido
