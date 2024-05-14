# Lista para armazenar as temperaturas máximas de cada mês
temperaturas_maximas = []

# Dicionário para mapear os meses em formato numérico para o formato por extenso
meses_por_extenso = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}

# Função para validar a temperatura inserida pelo usuário
def validar_temperatura(temperatura):
    try:
        temperatura = float(temperatura.replace(",", "."))
        return -60 <= temperatura <= 50
    except ValueError:
        return False

# Loop para ler as temperaturas máximas de cada mês
for mes in range(1, 13):
    temperatura = None
    while temperatura is None or not validar_temperatura(temperatura):
        try:
            temperatura = input(f"Digite a temperatura máxima para o mês {mes}: ")
            if not validar_temperatura(temperatura):
                print("Temperatura inválida. A temperatura máxima deve estar entre -60°C e +50°C.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    temperaturas_maximas.append(float(temperatura.replace(",", ".")))

# Calcular média das temperaturas máximas
media_anual = sum(temperaturas_maximas) / len(temperaturas_maximas)

# Contar quantidade de meses escaldantes (temperatura > 33°C)
meses_escaldantes = sum(1 for temperatura in temperaturas_maximas if temperatura > 33)

# Encontrar o mês mais quente e o mês menos quente
mes_mais_quente = meses_por_extenso[temperaturas_maximas.index(max(temperaturas_maximas)) + 1]
mes_menos_quente = meses_por_extenso[temperaturas_maximas.index(min(temperaturas_maximas)) + 1]

# Mostrar os resultados
print(f"Temperatura média máxima anual: {media_anual:.2f}°C")
print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {mes_mais_quente}")
print(f"Mês menos quente do ano: {mes_menos_quente}")