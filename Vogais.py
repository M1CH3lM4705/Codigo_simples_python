def vogais (vogais_Cons):
    contVogais = 0
    contCons = 0
#for para percorrer a lista a procura de vogais e consoantes
    for vogais_Cons in lista_vogais:
        if(vogais_Cons in "aeiouAEIOU"):
       
           contVogais += 1
        if(vogais_Cons in "bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVWXZ"):

           contCons += 1

    return print("A palavra {} tem {} vogais e {} consoantes"
              .format(lista_vogais, contVogais, contCons))

    

def preencherVogais():
    
    print("Contador de vogais e consoantes!\n\n")

    vogais_Cons = (input("Digite uma palavara: "))

    vogais(vogais_Cons)
