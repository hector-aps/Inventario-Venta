# Sistema de Inventario y Venta
![](https://github.com/hector-aps/Inventario-Venta/blob/main/README%20Images/Captura%20de%20pantalla%20(454).png?raw=true)

Sistema de manejo de inventario y de venta simple, habia hecho este mismo programa hace unos meses como aplicacion de consola pero ahora lo recree con una interfaz grafica y funcionalidades extra.


## Caracteristicas
Algunas de las caracteristicas del proyecto son las siguientes:

- Manejo de inventario mediante documento **CSV**, los productos pueden tener **3** caracteristicas: Nombre, precio, existencias (cantidad).

- Capacidad de **agregar** nuevos productos y **modificar** o **eliminar** los existentes.

- Realizar **ventas** dentro del mismo programa, se agregaran los productos a comprar en el carrito de compra y al finalizar se creara un ticket de compra, el cual se guardara en la carpeta "tickets" que se creara en la misma carpeta en la que estan los documentos principales, ademas se restaran los productos adquiridos de las existencias del inventario y si llegaran a cero, se eliminaria el producto del inventario.

## Imagenes:
Imagen de la ventana de venta:

![](https://github.com/hector-aps/Inventario-Venta/blob/main/README%20Images/Captura%20de%20pantalla%20(455).png?raw=true)

Imagen de un ticket de compra generado por el programa:

![](https://github.com/hector-aps/Inventario-Venta/blob/main/README%20Images/Captura%20de%20pantalla%20(457).png?raw=true)

El programa esta dividido en dos archivos, uno se encarga de toda la logica y la POO **(modulo_inventario.py)**, y el principal se encarga de mostrar la interfaz grafica y manejar la interaccion con el usuario **(main.pyw)**:

![](https://github.com/hector-aps/Inventario-Venta/blob/main/README%20Images/Captura%20de%20pantalla%20(458).png?raw=true)

El Inventario se almacena en un documento **CSV**, y los tickets de compra en una carpeta donde se guardan con la fecha y hora en que fueron creados como nombre:

![](https://github.com/hector-aps/Inventario-Venta/blob/main/README%20Images/Captura%20de%20pantalla%20(459).png?raw=true)

-La documentacion de funciones no se ha agregado, pero lo hare pronto-
