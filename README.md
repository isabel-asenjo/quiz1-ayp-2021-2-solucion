# QUIZ 1 - ALGORITMOS Y PROGRAMACIÓN 2021-2
## Problema 1 (6pts):
Crea un módulo para validación de contraseñas. Dicho módulo deberá cumplir con los siguientes criterios de aceptación:
- La contraseña debe contener un mínimo de 8 caracteres.
- Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
- La contraseña no puede contener espacios en blanco.
- Contraseña válida: retorna “Contraseña ingresada correctamente”.
- Contraseña no válida: retorna el mensaje "La contraseña elegida no es válida".


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
-------------------------------------------------------------------------------------------

### Definiciones:
- **Número incremental:** todo número de dos o más dígitos que van en orden ascendente de izquierda a derecha. Ejemplo: El número 123 es un número incremental dado que 1 es menor a 2 y a su vez 2 es menor a 3.
