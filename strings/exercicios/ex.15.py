def validar_especie(animal):
    if animal.isalpha():
        print("Espécie de animal válida.")
    else:
        print("Espécie inválida.")

animal = input("Digite uma espécie de animal: ")

validar_especie(animal)