# instrutor/criar_curso.py

from models import Course
"""
    cria um novo objeto curso, associando ao instrutor.
"""
def executar(instrutor, lista_geral_de_cursos):

    print("\n--- Criando Novo Curso ---")
    nome_curso = input("Digite o nome do novo curso: ")
    descricao_curso = input("Digite a descrição do curso: ")
    
    
    novo_curso = Course(nome_curso, descricao_curso, instrutor, [], [])
    lista_geral_de_cursos.append(novo_curso)
    instrutor.cursos.append(novo_curso)
    
    print(f"\nCurso '{nome_curso}' criado com sucesso!")