# Empresa TudoWeb
# Pesquisa de opnião
# estrutura FOR
# contadores para entrevistados

excelente = 0
ruim = 0

print("--- Pesquisa de Satisfação Tudo Web ---")

# repetição FOR = 50 entrevistados
for i in range(1, 3): 
    print(f"\nEntrevistado nº {i}")
    
    # Coleta de dados
    nome = input("Qual o seu nome: ")
    idade = int(input("Qaual a sua idade: "))
    
    print("Opinião: 1-EXCELENTE | 2-BOM | 3-RUIM")
    opniao = int(input("Sua Opnião: "))

    # Estrutura de decisão FOR (processamento)
    if opniao == 1:
        excelente += 1
    elif opniao == 3:
        ruim += 1
    else:
        bom +=1
    

# Exibição dos resultados (Saída)
print("\n" + "="*30)
print(f"Total de respostas EXCELENTE: {excelente}")
print(f"Total de respostas RUIM: {ruim}")
print("="*30)
