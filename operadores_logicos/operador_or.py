# operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(inpuT("voce tem dinheiro para comprar"))
    print(f"tem_dinheiro? {tem_dinheiro}")
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"vou comer um mc-donalds hoje? {autorizado}")

    posso_comprar()