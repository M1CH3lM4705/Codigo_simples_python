#Pograminha pra calcular preço de venda de um produto

def preencherTela():
    print("-------------------Calculo de venda--------------------")
    print("\n\n")
    print("Insira os dados do 'Valor do Produdo, 'ICMS', 'PIS', 'COFINS' \nE '"
          "MARGEM DE LUCRO'")
    print("Os valores dos impostos tem que ser passado em porcentagem(%)\n"
          "e usando ponto(.) ao invês de virgula(,)")
    print("\n\n")

    while True:
        try:
            vlrProduto = float(input("Digite o valor do produtdo: "))
        except:
            print("\nValor Invvalido!")
            continue
        try:
            icms = float(input("Digite o ICMS: "))
        except:
            print("\nValor Invvalido!")
            continue
        try:
            pis = float(input("Digite o PIS: "))
        except:
            print("\nValor Invvalido!")
            continue
        try:
            cofins = float(input("Digite o COFINS: "))
        except:
            print("\nValor Invvalido!")
            continue
        try:
            margLucro = float(input("Digite a Margem de lucro: "))
        except:
            print("\nValor Invvalido!")
            continue
        vlrFinal = calcularProduto(vlrProduto,icms,pis,cofins,margLucro)
        print(vlrFinal)
        break



def calcularProduto(vlrProduto, icms,pis,cofins,margLucro):

    somaImposto = (icms + pis + cofins + margLucro)/100
    fator_calculo = (1 - somaImposto)*100
    valor_venda = (vlrProduto / fator_calculo)*100

    return valor_venda


def func_erro(valor):
    for x in valor:
        if(x in "ABCDEFGHIJKLMNOPQRSTUVXZabcdefghijklmnopqrstuvxz"):
           return print("Valor Invalido!")
        else:
            break;
