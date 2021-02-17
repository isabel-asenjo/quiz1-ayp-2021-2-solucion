'''
## Problema 2 (14pts):
Una compañía de transportes te ha contratado para que programes el modelo de su base de datos para llevar un control eficiente de los registros y datos de sus clientes. La base de datos se ha planteado de tal forma que el programador tendrá un libre albedrío en relación a la estructura o estructuras de datos que serán de soporte para el desarrollo de la misma. Sin embargo, los stakeholders de la compañía de transportes expresan que como mínimo el sistema a desarrollar debe cumplir con los siguientes requerimientos:
- El sistema maneja formularios con mensajes interactivos por consola.
- El monto regular de un boleto es de 40$.
- El sistema deberá solicitar nombre, edad, cédula del cliente.
- El sistema debe manejar los siguientes tipos de descuento:
  - Si la edad del cliente es mayor a 55 años, darle un 40% de descuento en su pago por boleto.
  - Si los tres últimos dígitos de la cédula del cliente es un número incremental, darle un 30% de descuento en el pago de su boleto. 
- Debe mostrarse un mensaje por pantalla con el monto sin descuento, el tipo de descuento aplicado (si es que hay alguno) y el monto final a pagar por el cliente.
- El programa debe contener validaciones para todos los datos ingresados por el usuario y las operaciones pertinentes en cada inciso.
- El sistema deberá proveer opciones en el menú de: agregar, eliminar y consultar todas las personas inscritas en el viaje.
'''

clients = []

while True:
    print("Bienvenido al sistema administrador de clientes de la compañía de transportes.\n1. Agregar cliente\n2. Eliminar cliente\n3. Consultar cliente\n4. Salir")
    action = input("Ingrese el número correspondiente a su elección: ")
    while not action.isnumeric() or int(action) not in range(1,5):
        action = input("Ingreso inválido, ingrese el número correspondiente a su elección: ")

    if action == "1":
        # datos
        name = input("Nombre del cliente: ").title()
        while not ("".join(name.split(" "))).isalpha():
            name = input("Por favor, ingrese un nombre válido: ").title()
        
        age = input("Edad del cliente: ")
        while not age.isnumeric() or int(age) <= 0:
            age = input("Por favor, ingrese una edad válida: ")

        id = input("Cédula del cliente: ")
        while not id.isnumeric() or len(id) < 1:
            id = input("Por favor, ingrese una cédula válida: ")

        print("Precio del boleto: $40.")
        price = 40
        discount = 'None'
        # descuentos. En caso de cumplirse ambas condiciones, aplico el mayor primero y luego el otro
        if int(age) > 50:
            price -= (price*0.40)
            discount = '40%'
            print(f"Por tener más de 55 años, tiene un descuento del 40% del precio del boleto. Su precio final es de {price}")
        if (int(id[-1]) > int(id[-2])) and (int(id[-2]) > int(id[-3])):
            price -= (price*0.30)
            if price == 40:
                discount = '30%'
            else:
                discount = '40% & 30%'
            print(f"Por tener como tres últimos dígitos de su cédula un número incremental, tiene un descuento del 30% del precio del boleto. Su precio final es de {price}")
        
        clients.append({'name': name, 'age': age, 'id': id, 'price': price, 'discount': discount})

        print(f"Cliente registrado con éxito!\n\tNombre: {name}\n\tEdad: {age}\n\tCédula: {id}\n\tPrecio del boleto: ${price}\n\tDescuento recibido: {discount}")

    elif action == "2":
        print("\nCLIENTES REGISTRADOS\n")
        for i,c in enumerate(clients):
            print(f"----{i+1}----")
            print(f"\tNombre: {c['name']}\n\tEdad: {c['age']}\n\tCédula: {c['id']}\n\tPrecio del boleto: ${c['price']}\n\tDescuento recibido: {c['discount']}")
        eliminar = input("Ingrese el número correspondiente al cliente que desea eliminar o ingrese 0 si desea salir: ")
        while not eliminar.isnumeric() or int(eliminar) not in range(0,len(clients)+1):
            eliminar = input("Ingreso inválido, intente de nuevo: ")
        for i in range(len(clients)):
            if i == int(eliminar)-1:
                eliminado = clients.pop(i)
                print(f"El cliente {eliminado['name']} fue eliminado con éxito.")
    
    elif action == "3":
        print("\nCLIENTES REGISTRADOS\n")
        for i,c in enumerate(clients):
            print(f"----{i+1}----")
            print(f"\tNombre: {c['name']}\n\tEdad: {c['age']}\n\tCédula: {c['id']}\n\tPrecio del boleto: ${c['price']}\n\tDescuento recibido: {c['discount']}")

    else:
        print("\nHasta pronto!")
        break

    print("\n")