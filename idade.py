from datetime import date
#Idade exata em dias

def preencherData():#Procedimento de entrada

    dia = int(input("Digite o dia que nasceu: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    calcularData(ano,mes,dia)


def calcularData(ano,mes,dia):#Funcao de calculo da data exata em dias
    dataAtual = date.today()#recebendo a data atual atraves do modulo date

    dataNiver = date(ano,mes,dia)

    diff = dataAtual - dataNiver

    idade_diff =(diff.days/365.2425)
    mes_diff = ((diff.days%365.2425)/30)
    dia_diff = (diff.days%365.2425)%30

    return print('%d anos, %d meses, %d dias' %(idade_diff,mes_diff,dia_diff))
