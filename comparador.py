def calcular_rendimento(valor_inicial, taxa_anual, meses):
    taxa_mensal = (1 + taxa_anual) ** (1/12) - 1
    return valor_inicial * ((1 + taxa_mensal) ** meses)

valor = 1000
meses = 12

rendimento_poupanca = calcular_rendimento(valor, 0.0617, meses)
rendimento_cdi = calcular_rendimento(valor, 0.105, meses)

print(f'Rendimento Poupança: R$ {rendimento_poupanca:.2f}')
print(f'Rendimento CDI: R$ {rendimento_cdi:.2f}')

# Adicionando o cálculo do MXRF11
rendimento_mxrf11 = calcular_rendimento(valor, 0.12, meses)
print(f'Rendimento MXRF11: R$ {rendimento_mxrf11:.2f}')