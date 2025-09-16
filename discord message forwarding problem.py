#O discord possui uma brecha na qual é possível enviar mensagens com emojis personalizados mesmo sem ter o nitro, basta somente encaminhar a mensagem com o emoji para a pessoa. Este código resolve justamente este problema

mensagem = """como assim? :oi:""" #mensagem de exemplo

nitro = False

pode = True #se a mensagem pode ou não ser encaminhada

mensagem = mensagem.replace(":",":=")

mensagem  = mensagem.split(":")

quantidade = mensagem.count("=")

for _ in range(0,quantidade):
    mensagem.remove("=")


emojis_padrão = ["art","calendar"] #uma pequena lista dos emojis permitidos (apenas para exemplo)

for trecho in mensagem:

    if ( trecho.startswith("=") ) and ( trecho[1:] not in emojis_padrão ) and ( nitro == False):
        pode = False
        break

if pode:
    print("Mensagem encaminhada com sucesso")
else:
    print("Esta imagem contem emojis personalizados. Você precisa de uma assinatura nitro para encaminhá-la")
    
