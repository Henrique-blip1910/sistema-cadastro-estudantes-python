def mostrar_menu_principal():
    print("\nOlá! Bem-vindo ao menu principal!")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")
    return input("Digite uma das opções válidas acima: ")

def mostrar_menu_de_operacoes():
    print("\nMenu de operações:")
    print("1. Listar")
    print("2. Incluir")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")
    return input("Digite uma das opções válidas do menu de operações acima: ")

def incluir_estudantes(estudantes):
    print("Você selecionou a opção Incluir")
    try:
        codigo = int(input("Digite o seu código de estudante: "))
    except ValueError:
        print("Código inválido. Deve ser um número.")
        return

    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF: ")

    elementos_estudantes = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }
    estudantes.append(elementos_estudantes)
    print(f"Os dados {elementos_estudantes} foram incluídos com sucesso!")

def listar_estudantes(estudantes):
    print("Você selecionou a opção Listar")
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        print("\nLista de Estudantes:")
        for estudante in estudantes:
            print(f" - Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

def excluir_estudantes(estudantes):
    print("Você selecionou a opção Excluir")
    try:
        excluir_cod = int(input("Digite o código do estudante que deseja excluir: "))
    except ValueError:
        print("Código inválido. Deve ser um número.")
        return

    for estudante in estudantes:
        if estudante["codigo"] == excluir_cod:
            estudantes.remove(estudante)
            print(f"Estudante {excluir_cod} removido com sucesso!")
            return

    print(f"Estudante com código {excluir_cod} não encontrado.")

def editar_estudantes(estudantes):
    print("Você selecionou a opção Atualizar")
    try:
        editar_cod = int(input("Digite o código do estudante que deseja editar: "))
    except ValueError:
        print("Código inválido. Deve ser um número.")
        return

    for estudante in estudantes:
        if estudante["codigo"] == editar_cod:
            print(f"Editando estudante: {estudante}")
            estudante["nome"] = input("Digite o novo nome: ")
            estudante["cpf"] = input("Digite o novo CPF: ")
            print("Dados atualizados com sucesso!")
            print(f"Novo registro: {estudante}")
            return

    print(f"Estudante com código {editar_cod} não encontrado para edição.")

# ---------- Execução ----------
estudantes = []

while True:
    opcao1 = mostrar_menu_principal()

    if opcao1 == "1":
        print("Você escolheu a opção: Estudantes")

        while True:
            opcao2 = mostrar_menu_de_operacoes()

            if opcao2 == "1":
                listar_estudantes(estudantes)
            elif opcao2 == "2":
                incluir_estudantes(estudantes)
            elif opcao2 == "3":
                editar_estudantes(estudantes)
            elif opcao2 == "4":
                excluir_estudantes(estudantes)
            elif opcao2 == "5":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção INVÁLIDA! Tente novamente.")

    elif opcao1 in ["2", "3", "4", "5"]:
        print("Função ainda em desenvolvimento.")

    elif opcao1 == "0":
        print("Você saiu do menu principal.")
        break

    else:
        print("Opção INVÁLIDA! Tente novamente.")

