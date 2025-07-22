# instrutor/add_remove_conteudo.py

from models import Conteudo

"""
    permite que um instrutor adicione ou remova objetos Conteudo
    de um de seus cursos.
"""
def executar(instrutor, cursos):
    print("\n--- Gerenciar Conteúdos de um Curso ---")

    cursos_do_instrutor = [c for c in cursos if c.instrutor == instrutor]

    if not cursos_do_instrutor:
        print("Você não tem cursos para gerenciar.")
        return

    print("Para qual curso você deseja gerenciar os conteúdos?")
    for i, curso in enumerate(cursos_do_instrutor):
        print(f"{i+1} - {curso.titulo}")

    try:
        escolha_curso_num = int(input("Digite o número do curso: "))
        curso_selecionado = cursos_do_instrutor[escolha_curso_num - 1]
    except (ValueError, IndexError):
        print("Opção de curso inválida.")
        return

    print(f"\nGerenciando o curso: '{curso_selecionado.titulo}'")
    if not curso_selecionado.conteudos:
        print("Este curso ainda não possui conteúdos.")
    else:
        print("Conteúdos atuais:")
        for conteudo_obj in curso_selecionado.conteudos:
            print(f"  - {conteudo_obj}")

    acao = input(
        "\nVocê deseja 'adicionar' ou 'remover' um conteúdo? ").lower()

    if acao == 'adicionar':
        print("\n--- Adicionando Novo Conteúdo ---")
        novo_titulo = input("Digite o título do conteúdo: ")
        novo_tipo = input("Digite o tipo (ex: Video, PDF, Quiz): ")
        try:
            nova_duracao = int(input("Digite a duração em minutos: "))

            # Cria o objeto Conteudo
            novo_conteudo = Conteudo(novo_titulo, novo_tipo, nova_duracao)

            # Adiciona o objeto à lista do curso
            curso_selecionado.conteudos.append(novo_conteudo)
            print(
                f"\nConteúdo '{novo_conteudo.titulo}' adicionado com sucesso!")
        except ValueError:
            print("Erro: A duração deve ser um número inteiro.")

    # 4. Lógica para REMOVER
    elif acao == 'remover':
        if not curso_selecionado.conteudos:
            return  # Sai da função se não há nada para remover

        print("\nQual conteúdo você deseja remover?")
        for i, conteudo_obj in enumerate(curso_selecionado.conteudos):
            print(f"  {i+1} - {conteudo_obj.titulo}")

        try:
            escolha_remover_num = int(
                input("Digite o número do conteúdo a ser removido: "))
            conteudo_removido = curso_selecionado.conteudos.pop(
                escolha_remover_num - 1)
            print(
                f"\nConteúdo '{conteudo_removido.titulo}' removido com sucesso!")
        except (ValueError, IndexError):
            print("Opção de conteúdo inválida.")

    else:
        print("Ação inválida. Tente novamente.")
