#   valor_1 = 4
#   valor_2 = 6
#   
#   valor_4 = 50
#   valor_5 = 30
#   
#   valor_8 = 0
#   
#   def soma(valor_1_para_somar:float, valor_2_para_somar:float = 10) -> float:
#       """
#       uma função simples para soma de valores float que retorna float
#       """
#       resultado_da_soma = valor_1_para_somar + valor_2_para_somar
#       return resultado_da_soma
#   
#   valor_3 = soma(valor_1_para_somar = valor_1, valor_2_para_somar = valor_2)
#   valor_6 = soma(valor_4, valor_5)
#   valor_7 = soma(valor_8)   # 10
#   valor_10 = soma(0,0)   # 0
#   
#   
#   print(valor_3)
#   print(valor_6)
#   print(valor_7)
#   print(valor_10)


def cumprimentar(mensagem, nome):
    cumprimento = f"{mensagem}, {nome}!"
    return cumprimento

# Exemplo de uso:
nome = "Maria"
mensagem = "Seja bem-vinda"
print(cumprimentar(mensagem, nome))  # Isso imprimirá "Bem-vindo, João!"
