from data_base import alunos, cursos, instrutores
from models import Course, Student, Instructor

def menu_instrutor(instrutor, cursos):

    while True:
        # Menu do instrutor
        print(f"\n--- Menu do Instrutor: {instrutor.nome} ---")
        print("1 - Listar Meus Cursos")
        print("2 - Criar Curso")
        print("3 - Sair")

        choose = int(input("Escolha uma opção: "))

        while choose not in [1, 2, 3]:
            print("Opção inválida. Tente novamente.")
            choose = int(input())

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

        elif choose == 2:
            nome_curso = input("Digite o nome do novo curso: ")
            descricao_curso = input("Digite a descrição do curso: ")
            novo_curso = Course(nome_curso, descricao_curso, instrutor)
            cursos.append(novo_curso)
            print(f"Curso '{nome_curso}' criado com sucesso!")

        elif choose == 3:
            print("Saindo do menu do instrutor. Até logo!")
            exit()