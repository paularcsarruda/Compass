import hashlib

while True:
    string_input = input("Digite uma string (ou 'sair' para encerrar): ")

    if string_input.lower() == 'sair':
        print("Encerrando o programa...")
        break

    hash_object = hashlib.sha1(string_input.encode())

    print("O hash SHA-1 da string é:", hash_object.hexdigest())