def validar_usuario(usuario):
    usuario_validado = usuario.isalnum()
    if usuario_validado:
        print("usuario valido!!")
    else:
        print("utilize apenas letras e numeros!!")

        nome_usuario =input("digite seu usuario: ")
        validar_usuario(nome_usuario)



     #analizando uma frase
        def analisar_frase(frase,palavra):
           frase_limpa = frase.strip()

           qtde_caracteres = len(frase_limpa)
           qtde_palavras = len(frase_limpa.split())
           ocorrencias_palavra = frase_limpa.count(palavra)

           print(f'frase completa: {frase_limpa}')
           print(f'total de caracteres: {qtde_caracteres}')
           print(f'total de palavras: {qtde_palavras}')
           print(f'ocorrencias das palavra pesquisadas: {ocorrencias_palavra}')


           frase_input = input('digite uma frase: ')
           ocorrencias_palavra = input('digite uma palavra para contar a ocorrencia: ')
           analisar_frase(frase_input,ocorrencias_palavra)