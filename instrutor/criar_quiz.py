from models import PerguntaQuiz, Conteudo, Quiz


"""
    permite que um instrutor crie quiz
"""
def executar(instrutor, cursos):
    print("\n------ CRIAR NOVO QUIZ ------")

    
    cursos_do_instrutor = [c for c in cursos if c.instrutor == instrutor]

    if not cursos_do_instrutor:
        print("Você precisa criar um curso antes de adicionar um quiz.")
        return

    
    print("Você deseja criar um quiz para qual curso?")
    for i, curso in enumerate(cursos_do_instrutor):
        print(f"{i + 1} - {curso.titulo}")
    
    

    try:
        escolha_num = int(input("\nDigite o número do curso: "))
        curso_selecionado = cursos_do_instrutor[escolha_num - 1]
    except (ValueError, IndexError):
        print("Opção de curso inválida.")
        return



    print(f"\nCriando quiz para o curso: '{curso_selecionado.titulo}'")
    

    perguntas_do_quiz = []
    while True:
        enunciado = input("\nDigite o enunciado da pergunta: ")
        opcoes = [opt.strip() for opt in input("Digite as opções separadas por vírgula: ").split(',')]
        
        try:
            resposta_idx = int(input(f"Digite o número da resposta correta (1 a {len(opcoes)}): ")) - 1
            if not (0 <= resposta_idx < len(opcoes)):
                print("Índice de resposta inválido. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue
            
        nova_pergunta = PerguntaQuiz(enunciado, opcoes, resposta_idx)
        perguntas_do_quiz.append(nova_pergunta)

        continuar = input("Deseja adicionar mais perguntas? (s/n): ").lower()
        if continuar != 's':
            break

    if not perguntas_do_quiz:
        print("Nenhuma pergunta foi criada. Quiz cancelado.")
        return


    titulo_quiz = "Quiz sobre " + curso_selecionado.titulo
    novo_quiz_obj = Quiz(titulo_quiz, perguntas_do_quiz)

    conteudo_quiz = Conteudo(titulo_quiz, "Quiz", quiz_obj=novo_quiz_obj)
    curso_selecionado.conteudos.append(conteudo_quiz)

    #Conteudo -> Quiz -> Pergunta quiz
    #Conteudo -> quiz_obj -> perguntas

    print(f"\nQuiz '{novo_quiz_obj.titulo}' adicionado com sucesso ao curso '{curso_selecionado.titulo}'!")