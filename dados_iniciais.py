from models import Course, Student, Instructor, Conteudo
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


    #CONTÉUDOS
    conteudos_py = [
        Conteudo("PDF - Sobre Python", "PDF", 10),
        Conteudo("Vídeo - Introdução ao Python", "video", 30),
    ]
    conteudos_ds = [
        Conteudo("PDF - Introdução ao Data Science", "PDF", 15),
        Conteudo("Vídeo - Análise de Dados", "video", 45)
    ]
    conteudos_ml = [
        Conteudo("PDF - Fundamentos de Machine Learning", "PDF", 20),
        Conteudo("Vídeo - Algoritmos de Machine Learning", "video", 50)
    ]
    conteudos_web = [
        Conteudo("PDF - Introdução ao Django", "PDF", 25),
        Conteudo("Vídeo - Criando APIs com Django", "video", 60)
    ]


    #CURSOS
    curso1 = Course("Python Basico", "Curso introdutório de Python", carlos, conteudos_py, [lucas, larissa])
    curso2 = Course("Data Science", "Curso de Data Science com Python", laura, conteudos_ds, [larissa, maria])
    curso3 = Course("Machine Learning", "Curso de Machine Learning com Python", carlos, conteudos_ml, [lucas, maria])
    curso4 = Course("Desenvolvimento Web", "Curso de desenvolvimento web com Django", laura, conteudos_web, [larissa])
    listaCursos.extend([curso1, curso2, curso3, curso4])

    for curso in listaCursos:
        for aluno in curso.students:
            if curso not in aluno.cursos_inscritos:
                aluno.cursos_inscritos.append(curso)