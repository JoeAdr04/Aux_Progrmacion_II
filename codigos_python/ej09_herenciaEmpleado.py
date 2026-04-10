class Empleado:
    def __init__(self,nombre,sueldoporHora,horaTrabajadas):
        self._nombre=nombre
        self._sueldoporHora=sueldoporHora
        self._horaTrabajadas=horaTrabajadas
    def __str__(self):
        return f"nombre{self._nombre}, sueldoHora:{self._sueldoporHora}, horas Trabajadas:{self._horasTrabajadas}"

    def verificarHoras(self): #funcion para verificar las horas
        if(self._horasTrabajadas >8):
            return True
        else:
            return False

    def calculoHorasExtra(self):
        horaExtra = 0
        if(self.verificarHoras() == True):
            horaExtra = self._horasTrabajadas -8
        return horasExtra

    def calcularSueldo(self):
        sueldoMes = 0
        horasExtra = self.calculoHorasExtra()
        sueldoMes = (self.sueldoHora*8)*30
        if(self.verificarHoras() == True):
            if(self.calculoHorasExtra() > 0):
                sueldoMes = sueldoMes + (horasExtra*2*self.sueldoHora)
        else:
            sueldoMes = sueldoMes*0.5
    
class EmpleadoProduccion(Empleado):
    def __init__(self,nombre,sueldoporHora,horaTrabajadas, cantidadProducida):
        super().__init__(nombre,sueldoporHora,horaTrabajadas)
        self.__cantidadProducida = cantidadProducida
    def calcularSueldo(self):
        suelMes = super.calcularSueldo()
        if(self.__cantidadProducida <100):
            suelMes =suelMes-(suelMes*0.2)
        return suelMes
        
class empleadoVentas(Empleado):
    def __init__(self,nombre,sueldoporHora,horaTrabajadas,ventaMensual, comision):
        super().__init__(nombre,sueldoporHora,horaTrabajadas)
        self.__ventaMensual = ventaMensual
        self.__comision = comision
