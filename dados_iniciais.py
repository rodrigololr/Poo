from models import Course, Student, Instructor
from data_base import alunos, cursos, instrutores

def dados_iniciais(listaAlunos, listaInstrutores, listaCursos):

    # ALUNOS
    lucas = Student("Lucas", "coxinha123")
    larissa = Student("Larissa", "bolacha456")
    maria = Student("Maria", "pudim456")
    listaAlunos.extend([lucas, larissa, maria])

    # INSTRUTORES
    carlos = Instructor("Carlos", "prof123")
    laura = Instructor("Laura", "ensino456")
    listaInstrutores.extend([carlos, laura])

    # CURSOS
    curso1 = Course("Python Básico", "Curso introdutório de Python", carlos, ["PDF - Sobre Python", "Vídeo - Introdução"], [lucas, larissa])
    curso2 = Course("Data Science", "Curso de Data Science com Python", laura, ["PDF - Introdução ao Data Science", "Vídeo - Análise de Dados"], [larissa, maria])
    curso3 = Course("Machine Learning", "Curso de Machine Learning com Python", carlos, ["PDF - Fundamentos de ML", "Vídeo - Algoritmos de ML"], [lucas, maria])
    curso4 = Course("Desenvolvimento Web", "Curso de desenvolvimento web com Django", laura, ["PDF - Introdução ao Django", "Vídeo - Criando APIs com Django"], [larissa])
    listaCursos.extend([curso1, curso2, curso3, curso4])

