# Função para calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso adequado"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo e exibição do resultado
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
#aw fa~iv~çfa