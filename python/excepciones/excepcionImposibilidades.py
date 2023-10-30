from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionImposibilidad(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(f"Error por tipo de dato:\n{error}")

class ExcepcionPositivo(ExcepcionImposibilidad):
    def __init__(self, entrada):
        super().__init__(f"\nEl valor debe ser positivo.")

    @classmethod
    def valorPositivo(cls,valor):
        if valor<=0:
            raise ExcepcionPositivo(valor)

class ExcepcionValorMaximo(ExcepcionImposibilidad):
    def __init__(self, entrada):
        super().__init__(f"\nEl valor debe ser positivo.")

    @classmethod
    def menorQue(cls,valor,maximo):
        if maximo<valor:
            raise ExcepcionValorMaximo(valor)