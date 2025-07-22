
import os
from aluno import certificado 

'''
    mostra o conteúdo do curso escolhido pelo aluno
'''

def executar(aluno_logado, curso_escolhido, cursos):

    if not curso_escolhido.conteudos:
        print("\nEste curso ainda não possui conteúdos.")
        return

    total_conteudos = len(curso_escolhido.conteudos)
    contador_vistos = 0
    for conteudo in curso_escolhido.conteudos:
        if conteudo.check == "Visto":
            contador_vistos += 1
            
    curso_completo = (total_conteudos == contador_vistos)

    
    print("\n--- Conteúdos do Curso ---")
    for i, conteudo in enumerate(curso_escolhido.conteudos):
        print(f"{i + 1} - {conteudo}")

    print("-" * 30)

   
    if curso_completo:
        print("🎉 Parabéns! Você concluiu este curso! 🎉")
        print(f"{total_conteudos + 1} - Emitir Certificado")
    
    print("0 - Voltar")

  
    try:
        escolha = int(input("\nQual conteúdo você deseja ver agora? (ou escolha uma opção): "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        return


    if(1 <= escolha <= total_conteudos):

        conteudo_selecionado = curso_escolhido.conteudos[escolha - 1]

        if conteudo_selecionado.tipo.lower() == "video":
            print(f"-> Abrindo vídeo: {conteudo_selecionado.titulo}")
            os.startfile("video.mp4")
            conteudo_selecionado.check = "Visto"
        
        elif conteudo_selecionado.tipo.lower() == "pdf":
            print(f"-> Abrindo PDF: {conteudo_selecionado.titulo}")
            os.startfile("pdf.pdf")
            conteudo_selecionado.check = "Visto"
            
        elif conteudo_selecionado.tipo.lower() == "quiz":
            print(f"-> Abrindo quiz: {conteudo_selecionado.titulo}")

    elif curso_completo and escolha == total_conteudos + 1:
        certificado.executar(curso_escolhido, aluno_logado)
        input("\nPressione Enter para continuar...")

    elif escolha == 0:
        return # Simplesmente retorna para o menu anterior

    else:
        print("Opção inválida.")