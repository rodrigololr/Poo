# Classes
class Course:
    def __init__(self, titulo, descricao, instrutor, conteudos=None, students=None):
        self.titulo = titulo
        self.descricao = descricao
        self.instrutor = instrutor
        self.conteudos = conteudos if conteudos is not None else []
        self.students = students if students is not None else []


class Student:
    def __init__(self, nome, senha, cursos_inscritos=None):
        self.nome = nome
        self.senha = senha
        self.cursos_inscritos = cursos_inscritos if cursos_inscritos is not None else []


class Instructor:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.cursos = []
