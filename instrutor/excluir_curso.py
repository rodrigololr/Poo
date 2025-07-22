# instrutor/excluir_curso.py

"""
    permite que o instrutor exclua um de seus cursos da plataforma.
"""

def executar(instrutor, cursos):

    print("\n--- Excluir Curso ---")
    cursos_do_instrutor = [curso for curso in cursos if curso.instrutor == instrutor]

    if not cursos_do_instrutor:
        print("Você não tem cursos para excluir.")
        return

    print("Qual curso você deseja excluir?")
    for i, curso in enumerate(cursos_do_instrutor):
        print(f"{i+1} - {curso.titulo}")

    try:
        escolha_num = int(input("Digite o número do curso: "))
        curso_para_excluir = cursos_do_instrutor[escolha_num - 1]

        confirmacao = input(f"Tem certeza que deseja excluir o curso '{curso_para_excluir.titulo}'? (s/n): ").lower()

        if confirmacao == 's':
            cursos.remove(curso_para_excluir)
            instrutor.cursos.remove(curso_para_excluir)
            print("\nCurso excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")

    except (ValueError, IndexError):
        print("Opção inválida.")