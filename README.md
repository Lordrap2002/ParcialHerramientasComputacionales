# **_Parcial Herramientas Computacionales_**

El problema a resolver trata sobre las cafeterias de la universidad, las cuales desean otorgar descuentos a sus clientes dependiendo de su rol.

El archivo que resuelve este problema se llama _cafeteria.py_.

El algoritmo recibe como entrada los siguientes datos en este orden: 
  * Numero de cedula del cliente: Tipo de dato: Numero entero.
  * Rol del cliente: Tipo de dato: Una de dos cadenas, "profesor" o "estudiante":
  * Codigo del producto: Tipo de dato: Numero entero.
  * Cantidad del producto: Tipo de dato: Numero entero.
  * Precio del producto: Tipo de dato: Numero entero.
  
La salida del algoritmo es una cadena que contiene los siguientes datos:
  1. Rol del cliente.
  2. Numero de cedula del cliente.
  3. Valor total a pagar.
  4. Codigo del producto.
  
  La cadena general sería la siguiente:
   + ”El **_(1)_** con cedula **_(2)_**, debe pagar **_(3)_** por el producto **_(4)_**”
    
Para encontrar el valor total a pagar, primero, el algoritmo multiplica el valor del producto por la cantidad de producto a llevar, despues, dependiendo del rol de cliente, calcula el valor con  el descuento multiplicando el total por 1 menos el porcentaje de descuento.
