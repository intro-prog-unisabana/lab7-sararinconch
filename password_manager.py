import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as miArchivo:
         password = miArchivo.read().strip()

    contraseña = caesar_encrypt(password)
    with open(filename, "w") as f:
        f.write(contraseña)


def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, mode='r') as archivo:
        lector = csv.reader(archivo)
        lista = []
        for fila in lector:
            if fila:
                lista.append(fila)
        for fila in lista[1:]:
            fila[2] = caesar_encrypt(fila[2])
    with open(filename, "w",) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(lista)
   



def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
