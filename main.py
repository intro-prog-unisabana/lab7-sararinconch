from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)
    while True:
        opciones = input("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        if opciones == "1":
            sitio = input("Enter the website and the new password:").split()
            if len(sitio) < 2:
                print("Input is in the wrong format!")
                continue
            website, contraseña = sitio[0], sitio[1]
            if len(contraseña) < 12:
                print("Password is too short!")
                continue
            else:
                resultado = change_password(filename, website, contraseña)
            if not resultado:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")

        elif opciones == "2":
            sitio = input("Enter the website, username, and password:\n").split()
            if len(sitio) < 3:
                print("Input is in the wrong format!")
                continue
            website, username, contraseña = sitio[0], sitio[1], sitio[2]
            if len(contraseña) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, contraseña)
            print("Login added.")

        elif opciones == "3":
            break
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()
