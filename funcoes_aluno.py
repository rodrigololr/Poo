from models import Course, Student, Instructor
from data_base import alunos, cursos, instrutores


def menu_aluno(aluno_logado, cursos):
    while True:
        print("\n--- Menu do Aluno ---")
        print("1 - Ver Cursos Inscritos")
        print("2 - Inscrever em Curso")
        print("3 - Sair")

        choose = int(input("Escolha uma opção: "))

        while choose not in [1, 2, 3]:
            print("Opção inválida. Tente novamente.")
            choose = int(input())


        # VER CURSOS INSCRITOS
        if choose == 1:
            if aluno_logado.cursos_inscritos:
                print("\nCursos Inscritos:")
                for curso in aluno_logado.cursos_inscritos:
                    print(f"- {curso.titulo}")
            else:
                print("Você não está inscrito em nenhum curso.")

        # MATRICULAR EM CURSO
        elif choose == 2:
            print("\nCursos Disponíveis:")
            for curso in cursos:
                print(f"- {curso.titulo} (Instrutor: {curso.instrutor.nome})")

            titulo_curso = input(
                "Digite o título do curso para se matricular: ")
            curso_encontrado = None

            for curso in cursos:
                if curso.titulo.lower() == titulo_curso.lower():
                    curso_encontrado = curso
                    break

            if curso_encontrado:
                aluno_logado.cursos_inscritos.append(curso_encontrado)
                curso_encontrado.students.append(aluno_logado)
                print(
                    f"Você se inscreveu no curso '{curso_encontrado.titulo}' com sucesso!")
            else:
                print("Curso não encontrado.")

        elif choose == 3:
            print("Saindo do menu do aluno. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
