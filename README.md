# ParcialHerramientasComputacionales

El problema a resolver trata sobre las cafeterias de la universidad, las cuales desean otorgar descuentos a sus clientes dependiendo de su rol.

El archivo que resuelve este problema se llama cafeteria.py.

El algoritmo recibe como entrada los siguientes datos en este orden: 
  1. Numero de cedula del cliente: Tipo de dato: Numero entero.
  2. Rol del cliente: Tipo de dato: Una de dos cadenas, "profesor" o "estudiante":
  3. Codigo del producto: Tipo de dato: Numero entero.
  4. Cantidad del producto: Tipo de dato: Numero entero.
  5. Precio del producto: Tipo de dato: Numero entero.
  
La salida del algoritmo es una cadena que contiene los siguientes datos:
  1. Rol del cliente.
  2. Numero de cedula del cliente.
  3. Valor total a pagar.
  4. Codigo del producto.
  
  La cadena general sería la siguiente:
    ”El (1) con cedula (2), debe pagar (3) por el producto (4)”
    
Para encontrar el valor total a pagar, primero, el algoritmo multiplica el valor del producto por la cantidad de producto a llevar, despues, dependiendo del rol de cliente, calcula el valor con  el descuento multiplicando el total por 1 menos el porcentaje de descuento.
