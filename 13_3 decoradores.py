usuario_autenticado = False
def autetincacion(funcion):
    def envoltura(*args,**kwargs):
        if not usuario_autenticado:
            raise PermissionError("no tienes permisos para ejecutar esta funcion")
        return funcion(*args,**kwargs)
    return envoltura 
@autetincacion
def acceder():
    print("acceso permitido")

acceder()