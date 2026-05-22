from calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada

print("=== Calculadora ===\n")

while True:
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Sair")
    
    opcao = input("\nDigite a opção (1-7): ")
    
    if opcao == "7":
        print("Até logo!")
        break
    
    if opcao in ["1", "2", "3", "4", "5"]:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            print(f"Resultado: {soma(a, b)}\n")
        elif opcao == "2":
            print(f"Resultado: {subtracao(a, b)}\n")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(a, b)}\n")
        elif opcao == "4":
            try:
                print(f"Resultado: {divisao(a, b)}\n")
            except ValueError as e:
                print(f"Erro: {e}\n")
        elif opcao == "5":
            print(f"Resultado: {potencia(a, b)}\n")
    
    elif opcao == "6":
        a = float(input("Digite o número: "))
        try:
            print(f"Resultado: {raiz_quadrada(a)}\n")
        except ValueError as e:
            print(f"Erro: {e}\n")
    else:
        print("Opção inválida!\n")