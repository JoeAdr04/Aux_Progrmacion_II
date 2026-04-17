class Documento:
    def __init__(self, nro, pat, mat,nom, per):
        self._nro = nro
        self._paterno = pat
        self._materno = mat
        self._nombre = nom
        self._persona = per
        
    def __str__(self):
        return f"numero:{self._nro} Nombre: {self._paterno} {self._materno} {self._nombre}"
    def setPersona(self,p):
        self._persona = p
class Carnet(Documento):
    def __init__(self, nro, pat, mat, nom, per, dir, huella):
        super().__init__(nro, pat, mat, nom, per)
        self.__direccion = dir
        self.__huella = huella
        
    def __str__(self):
        return super().__str__() + f"direccion:{self.__direccion}, huella: {self.__huella}"
    
class CertifNac(Documento):
    def __init__(self, nro, pat, mat, nom, per, anio, mes, dia):
        super().__init__(nro, pat, mat, nom, per)
        self.__anio = anio
        self.__mes = mes
        self.__dia = dia
    def __str__(self):
        return super().__str__() + f"anio:{self.__anio}, mes:{self.__mes}, dia:{self.__dia}"

class Empresa:
    def __init__(self, nit, dir):
        self.__nit = nit
        self.__direccion =dir
        self.__empleados = []
    
    def __str__(self):
        return f"nit:{self.__nit}, direccion:{self.__direccion} Empleados: \n {self.__empleados}"
    def getDir(self):
        return self.__direccion
class Persona:
    def __init__(self, car:Carnet = None, cert:CertifNac = None, emp:Empresa=None):
        self.__carnet = car
        self.__certifNac = cert
        self.__empresa = emp

    
    def setCert(self, cer):
        self.__certifNac = cer
        
    def setCar(self, car):
        self.__carnet = car
    def setEmp(self, e):
        self.__empresa = e
    def __str__(self):
        return self.__carnet.__str__()+ self.__certifNac.__str__() +"\n"+ self.__empresa.getDir()
class Main():
    emp = Empresa(7890, "av simon bolivar")
    p = Persona()
    carn1 = Carnet(123, "Lopez", "Garcia", "julian",p,"calle falsa",153453)
    cert1 = CertifNac(321, "Lopez", "Garcia","Julian" ,p,1999,12,12)
    p.setCar(carn1)
    p.setCert(cert1)
    p.setEmp(emp)
    
    p2 = Persona()
    carn2 = Carnet(123, "Mamani", "Chura", "luis",p,"calle falsa",6894865)
    cert2 = CertifNac(321, "Mamani", "Chura","luis" ,p,2000,8,15)
    p2.setCar(carn1)
    p2.setCert(cert1)
    p2.setEmp(emp)
    
    print(p)
    