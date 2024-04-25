from typing import List

# 1 - Calcular Média de Valores em uma Lista
#      
#   def calcular_media(valores: list[float]) -> float:
#       return sum(valores) / len(valores)
#   
#   valores = [10, 20, 30, 40, 50]
#   print(calcular_media(valores)) 



#   2 - Filtrar Dados Acima de um Limite
#   
#   def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
#       resultado = []
#       for valor in valores:
#           if valor > limite:
#               resultado.append(valor)
#       return resultado
#   
#   valores = [10.5, 20.7, 30.9, 40.1, 50.3]
#   limite = 40.0
#   
#   resultados_filtrados = filtrar_acima_de(valores, limite)
#   print(resultados_filtrados)
   


# 3 - Contar Valores Únicos em uma Lista
#   
#   def contar_valores_unicos(lista: List[int]) -> int:
#       return len(set(lista))
#   
#   lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#   resultado = contar_valores_unicos(lista)
#   print(resultado)


# 4 - Converter Celsius para Fahrenheit em uma Lista
#   
#   def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
#       return [(9/5) * temp + 32 for temp in temperaturas_celsius]
#   
#   temperaturas_celsius = [0, 10, 20, 30, 40]
#   temperaturas_fahrenheit = celsius_para_fahrenheit(temperaturas_celsius)
#   print(temperaturas_fahrenheit) 


# 5 - Calcular Desvio Padrão de uma Lista
#   
#   def calcular_desvio_padrao(valores: List[float]) -> float:
#       media = sum(valores) / len(valores)
#       variancia = sum((x - media) ** 2 for x in valores) / len(valores)
#       return variancia ** 0.5
#   
#   valores = [1, 2, 3, 4, 5]
#   desvio_padrao = calcular_desvio_padrao(valores)
#   print(desvio_padrao)



# 6 - Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

sequencia = [1, 2, 3, 4, 5, 7, 9, 13]
valores_ausentes = encontrar_valores_ausentes(sequencia)
print(valores_ausentes) 