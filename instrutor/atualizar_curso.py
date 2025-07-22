# instrutor/atualizar_curso.py


"""
    permite que o instrutor edite o título e a descrição de um de seus cursos.
"""
def executar(instrutor, cursos):

    print("\n--- Atualizar Curso ---")
    cursos_do_instrutor = [curso for curso in cursos if curso.instrutor == instrutor]

    if not cursos_do_instrutor:
        print("Você não tem cursos para atualizar.")
        return

    print("Qual curso você deseja editar?")
    for i, curso in enumerate(cursos_do_instrutor):
        print(f"{i+1} - {curso.titulo}")

    try:
        escolha_num = int(input("Digite o número do curso: "))
        curso_selecionado = cursos_do_instrutor[escolha_num - 1]

        print(f"\nEditando o curso: {curso_selecionado.titulo}")
        novo_nome = input(f"Digite o novo nome (ou enter para manter '{curso_selecionado.titulo}'): ")
        nova_descricao = input(f"Digite a nova descrição (ou enter para manter): ")

        if novo_nome:
            curso_selecionado.titulo = novo_nome
        if nova_descricao:
            curso_selecionado.descricao = nova_descricao
            
        print("\nCurso atualizado com sucesso!")

    except (ValueError, IndexError):
        print("Opção inválida.")