names = []
numbers = []

def new_contact():
    nameAdd = input('Nuevo Contacto (Nombre, Apellido)\n')
    numberAdd = input('Número de teléfono (9 dígitos)\n')
    names.append(nameAdd)
    numbers.append(numberAdd)
    print(names)
    print(numbers)

new_contact()
new_contact()
new_contact()
new_contact()
new_contact()


def show_contacts():
    print(names)
    print(numbers)

def search_number():
    numberAdd = input('Buscar número\n')
    for number in numbers:
        if numberAdd in numbers:
            print('El número pertenece al contacto:', names)
            break
        if numberAdd not in numbers:
            print('El número no existe.\n')
            break

search_number()

def search_name():
    nameAdd = input('Introduzca nombre del contacto\n')
    for name in names:
        if nameAdd in names:
            print('El número del contacto es:', numbers)
            break
        if nameAdd not in names:
            print('El contacto no existe.\n')
            break
