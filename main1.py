"Estrutura para chamar outras funçoes no estilo do-while"

i = 0

while True:
    print("Escolha uma opção: \n"
          "1 - para vogais \n"
          "2 - para valor do produto \n"
          "3 - para idade atual \n"
          "0 - para sair")
    try:
        vlr = int(input("Selecione o valor: "))
    except:
        print("\nOpção inválida! Digite apenas valores numéricos. \n")
        continue
    print('')
    if(vlr == 1):
        import Vogais
        Vogais.vogais()
        print('')
        
    elif(vlr == 2):
        import preco_venda
        preco_venda.preencherTela()
        print('')

    elif(vlr == 3):
        import idade
        idade.preencherData()
        print('')
        
    elif(vlr == 0):
        break
    else:
        print("Valor Invalido\n")
