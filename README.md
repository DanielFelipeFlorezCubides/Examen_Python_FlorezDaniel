(4H) Calculadora de Impuestos

El proyecto **Calculadora de Impuestos** tiene como objetivo desarrollar una herramienta que permita calcular el monto de impuestos sobre productos o servicios según diferentes tasas de impuestos que el usuario ingrese. Este tipo de herramienta es útil para pequeñas empresas, autónomos o cualquier persona que necesite calcular rápidamente el impuesto a pagar sobre el precio de un producto o servicio.

El programa debe permitir al usuario introducir el valor del producto o servicio y luego aplicar la tasa de impuestos especificada. Además, debe mostrar el valor total con impuestos incluidos y permitir al usuario elegir entre distintas categorías de impuestos, como IVA (Impuesto al Valor Agregado), impuestos especiales, entre otros.





# **Problemática**

- **Complejidad de los Cálculos de Impuestos:** Los usuarios necesitan una forma sencilla y confiable para calcular impuestos, ya que puede resultar complicado hacerlo manualmente, especialmente cuando hay diferentes tipos de impuestos o tasas según el producto o servicio.
- **Manejo de Varias Tasas de Impuestos:** Los usuarios deben poder aplicar diferentes tipos de impuestos dependiendo de la categoría del producto o servicio, como IVA, impuestos locales, impuestos especiales, etc.
- **Error Humano:** Los cálculos manuales o incluso el uso de calculadoras físicas pueden generar errores, lo que hace que la precisión sea fundamental. Este proyecto busca evitar esos errores mediante un cálculo automático.



# Funciones Principales

1. Ingreso de Datos:

- Permite al usuario ingresar el precio base de un producto o servicio.
- El usuario puede seleccionar o ingresar la tasa de impuesto a aplicar (por ejemplo, 10% de IVA, 5% de impuestos especiales, etc.).

1. Cálculo del Impuesto:

- Calcula el monto del impuesto a partir de la tasa ingresada y el precio base.
- El programa debe ser capaz de manejar múltiples tasas de impuestos (por ejemplo, IVA y otros impuestos especiales) y calcular cada uno por separado si es necesario.

1. Cálculo del Total con Impuesto:

- Una vez que el impuesto ha sido calculado, se suma al precio base para obtener el precio total que el usuario tendrá que pagar, incluyendo impuestos.

1. Mostrar Resultados:

- El programa muestra al usuario el precio base, el monto de los impuestos calculados y el precio total con impuestos incluidos.
- Si se manejan múltiples impuestos, cada impuesto debe ser mostrado por separado.

1. Opciones de Personalización de Impuestos:

- El usuario puede elegir diferentes tipos de impuestos (IVA, impuestos especiales, impuestos locales, etc.), con tasas definidas o ingresadas manualmente.

1. Validación de Entradas:

- El programa debe verificar que las entradas del usuario (precio y tasa de impuestos) sean números válidos, y notificar al usuario si se ingresan datos incorrectos.

1. Opción de Guardar Resultados (Opcional):

- El usuario puede tener la opción de guardar los resultados de la operación en un archivo (por ejemplo, un archivo de texto o CSV) para referencia futura.





# Ejemplo de Flujo de Trabajo:

1. El usuario ingresa el precio base de un producto (ej. 100).
2. El usuario selecciona la tasa de impuesto a aplicar (ej. 10% de IVA).
3. El programa calcula el impuesto (100 * 10% = 10).
4. El programa calcula el precio total con impuestos (100 + 10 = 110).
5. El programa muestra el precio base, el monto de impuesto y el total (Precio base: 100, Impuesto: 10, Total con impuesto: 110).



# Diseño de Calculadora de Impuestos

https://gist.github.com/programmersland/8000c1426fad99f38a2c9cb867ed2629

Resultado esperado

La entrega de este examen debe ser un enlace a un repositorio en GitHub llamado (Examen_Python_ApellidoNombre) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

- Archivo principal de ejecución basado en Python.
- Archivos modularizados que den funcionalidad al programa principal de Python.
- Archivo JSON que almacene la información del programa en sí.