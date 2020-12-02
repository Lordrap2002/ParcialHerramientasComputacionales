def cafeteria():
    n=input("Introduzca su cedula:")
    r=input("Introduzca su Rol:")
    cod=int(input("Codigo del Producto:"))
    u=int(input("Cuantos va a llevar:"))
    v=int(input("Precio del Proudcto:"))
    precio=v*u
    if r=="profesor":
        total=precio*0.8
    elif r=="estudiante":
        total=precio*0.5

    print("El %s con cedula %s, debe pagar %d por el producto %d" % (r,n,total,cod))
        
cafeteria()    
