from models import Conteudo

'''
    função para ver todos os conteudos do curso
'''

def executar(instrutor, cursos):
    print("\n--- Conteúdos de um Curso ---")

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

    # 2. Mostra os conteúdos atuais e pergunta a ação
    print(f"\nGerenciando o curso: '{curso_selecionado.titulo}'")
    if not curso_selecionado.conteudos:
        print("Este curso ainda não possui conteúdos.")
    else:
        print("Conteúdos atuais:")
        for conteudo_obj in curso_selecionado.conteudos:
            # O __repr__ da classe Conteudo formata isso!
            print(f"  - {conteudo_obj}")