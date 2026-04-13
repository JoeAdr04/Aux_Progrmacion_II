class Empleado:
    def __init__(self,nombre,sueldoporHora,horasTrabajadas):
        self._nombre=nombre 
        self._sueldoporHora=sueldoporHora
        self._horasTrabajadas=horasTrabajadas
    def __str__(self):
        f"nombre={self._nombre}  sueldoporHora={self._sueldoporHora}   horasTrabajadas={self._horasTrabajadas}"

    def VerificarHoras(self):
        if self._horasTrabajadas>8:
            return True
        else:
            return False 
    def CalculodeHorasExtras(self):
        Horas=0
        if self.VerificarHoras==0:
            Horas=self._horasTrabajadas-8
            return Horas
        
    def CalcularSueldo(self):
        sueldomes=0
        Horas=self.CalculodeHorasExtras()
        sueldomes=self._sueldoporHora*8*30
        if self._sueldoporHora==True:
            if self.CalculodeHorasExtras>0:
                sueldomes=sueldomes + (self._sueldoporHora*2*Horas)    
        else:
            sueldomes*=0.5  
        return sueldomes  
    
class EmpleadoProduccion(Empleado):
    def __init__(self, nombre, sueldoporHora, horasTrabajadas,cantidadProducida):
        super().__init__(nombre, sueldoporHora, horasTrabajadas,)
        self.__cantidadProducida=cantidadProducida
    def __str__(self):
        return super().__str__() + f"cantidadProducida={self.__cantidadProducida}"     
    def CalcularSueldo(self):
        sa= super().CalcularSueldo()
        if self.__cantidadProducida<100:
            sa=sa-(sa*0,2)
        return sa 
    
    
    
    
class EmpleadoVentas(Empleado):
    def __init__(self, nombre, sueldoporHora, horasTrabajadas,ventaMensual,comision):
        super().__init__(nombre, sueldoporHora, horasTrabajadas)
        self.__ventaMensual=ventaMensual
        self.__comision=comision
    def __str__(self):
        return super().__str__() +f"ventamensual={self.__ventamensual}  comision={self.__comision}"
    def CalcularSueldo(self):
        sa= super().CalcularSueldo()
        if self.__ventaMensual>1000:
            sa=sa+(sa*self.__comision/100)
        return sa 

class EmpleadoGordo(Empleado):
    def __init__(self, nombre, sueldoporHora, horasTrabajadas,comida):
        super().__init__(nombre, sueldoporHora, horasTrabajadas)
        self.comidda=comida
    def medir(self ):
        if self.comida>5:
            print("estas normal ")
        else:
            print("tenes que ver eso bro")

empleado=Empleado("jaun",10,9)
empleadoprod=EmpleadoProduccion("jaun",10,7,120)
print(empleadoprod.CalcularSueldo())

empleadovent=EmpleadoVentas("jaun",10,9,1200,70)
print(empleadovent.CalcularSueldo())

empleadovent2=EmpleadoVentas("carlso",10,9,800,70)
print(empleadovent2.CalcularSueldo())