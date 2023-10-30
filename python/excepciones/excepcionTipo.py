from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionTipo(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(f"Error por tipo de dato:\n{error}")

class ExcepcionVacio(ExcepcionTipo):
    def __init__(self,entradas):
         super().__init__(f"\nFalta llenar entradas: {entradas} \nPor favor ingreselas e intente de nuevo.")
    
    @classmethod
    def valorVacio(cls,valor):
        if valor=="" or valor is None or len(str(valor))==0:
            raise ExcepcionVacio(valor)

class ExcepcionEntero(ExcepcionTipo):
    def __init__(self,valor):
        super().__init__(f"\n{valor} es un texto, por favor modificar a un numero entero.")

    @classmethod
    def tipoInt(cls,valor):
        try:
            if len(valor)>0:
                int(valor)
        except ValueError:
            raise ExcepcionFloat(valor)


class ExcepcionFloat(ExcepcionTipo):
    def __init__(self,valor):
        super().__init__(f"\n{valor} no válido, por favor modificar a un float.")

class ExcepcionString(ExcepcionTipo):
    def __init__(self,valor):
        super().__init__(f"la entrada {valor} contiene al menos un número, debería ser completamente texto, por favor modificar.")

    @classmethod
    def tipoString(cls,valor):
        if len(valor)>0:
            if (any(chr.isdigit() for chr in valor)):
                raise ExcepcionString(valor)

        




