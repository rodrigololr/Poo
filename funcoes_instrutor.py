from data_base import alunos, cursos, instrutores
from models import Course, Student, Instructor
import inicial


def menu_instrutor(instrutor, cursos):

    while True:
        # Menu do instrutor
        print(f"\n--- Menu do Instrutor: {instrutor.nome} ---")
        print("1 - Listar Meus Cursos")
        print("2 - Criar Curso")
        print("3 - Atualizar informações Curso")
        print("4 - Excluir Curso")
        print("5 - Adicionar/Remover conteúdos do curso")
        print("6 - Chat e Forum")
        print("7 - Sair")

        choose = int(input("Escolha uma opção: "))

        while choose not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opção inválida. Tente novamente.")
            choose = int(input())

        # LISTAR MEUS CURSOS
        if choose == 1:
            print("\nCursos disponíveis:")
            for curso in cursos:
                if curso.instrutor == instrutor:
                    print(f"- {curso.titulo} (Descrição: {curso.descricao})")
                    if curso.students:
                        print("  Alunos inscritos:")
                        for student in curso.students:
                            print(f"  - {student.nome}")
                    else:
                        print("  Nenhum aluno inscrito.")

        # CRIAR UM NOVO CURSO
        elif choose == 2:
            nome_curso = input("Digite o nome do novo curso: ")
            descricao_curso = input("Digite a descrição do curso: ")
            novo_curso = Course(nome_curso, descricao_curso, instrutor)
            cursos.append(novo_curso)
            print(f"Curso '{nome_curso}' criado com sucesso!")

        # ATUALIZAR  INFORMAÇÕES BASICAS CURSO
        elif choose == 3:
            print("Qual curso você querer editar?")
            for i, curso in enumerate(cursos):
                if (curso.instrutor == instrutor):
                    print(f"{i} - {curso.titulo}")

            indice_curso = int(
                input("Digite o número do curso que você deseja editar: "))
            if 0 <= indice_curso < len(cursos):
                curso = cursos[indice_curso]
                novo_nome = input(
                    f"Digite o novo nome do curso (atual: {curso.titulo}): ")
                nova_descricao = input(
                    f"Digite a nova descrição do curso (atual: {curso.descricao}): ")
                curso.titulo = novo_nome
                curso.descricao = nova_descricao
                print("Curso atualizado com sucesso!")
            else:
                print("Curso não encontrado.")

        # EXCLUIR CURSO ALGUM CURSO
        elif choose == 4:
            print("Qual curso você deseja excluir?")
            for i, curso in enumerate(cursos):
                if (curso.instrutor == instrutor):
                    print(f"{i} - {curso.titulo}")

            indice_curso = int(
                input("Digite o número do curso que você deseja excluir: "))
            if 0 <= indice_curso < len(cursos):
                curso = cursos[indice_curso]
                cursos.remove(curso)
                print(f"Curso '{curso.titulo}' excluído com sucesso!")
            else:
                print("Curso não encontrado.")

        # ADICIONAR/REMOVER CONTEÚDOS DO CURSO
        elif choose == 5:
            print("Qual curso você deseja adicionar/remover conteúdos?")
            for i, curso in enumerate(cursos):
                if (curso.instrutor == instrutor):
                    print(f"{i} - {curso.titulo}")
            indice_curso = int(
                input("Digite o número do curso que você deseja editar: "))

            print("Conteúdos disponíveis:")
            for i, conteudo in enumerate(curso.conteudos):
                print(f"{i} - {conteudo}")

            if 0 <= indice_curso < len(cursos):
                curso = cursos[indice_curso]
                print("Você quer adicionar ou remover conteúdo?")
                acao = input(
                    "Digite 'adicionar' para adicionar ou 'remover' para remover: ")
                acao = acao.lower()
                if acao == "adicionar":
                    novo_conteudo = input(
                        f"Digite o novo conteúdo para o curso (exemplo: PDF - Sobre Python, Vídeo - Introdução...): ")
                    curso.conteudos.append(novo_conteudo)

                    print(
                        f"Conteúdo '{novo_conteudo}' adicionado ao curso com sucesso!")
                elif acao == "remover":
                    conteudo_remover = int(
                        input(f"Digite o número do conteudo que você deseja remover do curso: "))
                    if 0 <= conteudo_remover < len(curso.conteudos):
                        curso.conteudos.pop(conteudo_remover)
                        print(f"Conteúdo removido do curso com sucesso!")
                    else:
                        print(
                            f"Conteúdo '{conteudo_remover}' não encontrado no curso.")
                else:
                    print("Ação inválida.")
            else:
                print("Curso não encontrado.")

        # CHAT E FORUM
        elif choose == 6:
            print("Chat e Fórum")
        # SAIR
        elif choose == 7:
            print("Saindo do menu do instrutor. Até logo!")
            inicial.inicial()
            break
