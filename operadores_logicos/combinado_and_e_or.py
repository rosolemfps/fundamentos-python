#operadores and e or

def posso_entrar_no_show_do_veigh():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade? "))
    nome_esta_na_lista = bool(input("Qual a sua nome_esta_na_lista? "))

    posso_entrar = idade >= 18 and nome_esta_na_lista or POSSUI_INGRESSO

    print(f"posso entrar? {posso_entrar}")

    posso_entrar_no_show_do_veigh()