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
    curso1 = Course("Python Básico", "Curso introdutório de Python", carlos)
    curso2 = Course("Data Science", "Curso de Data Science com Python", laura)
    curso3 = Course("Machine Learning", "Curso de Machine Learning com Python", carlos)
    curso4 = Course("Desenvolvimento Web", "Curso de desenvolvimento web com Django", laura)
    listaCursos.extend([curso1, curso2, curso3, curso4])

