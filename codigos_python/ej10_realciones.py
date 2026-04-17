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

class Persona:
    def __init__(self, car:Carnet = None, cert:CertifNac = None):
        self.__carnet = car
        self.__certifNac = cert

    
    def setCert(self, cer):
        self.__certifNac = cer
        
    def setCar(self, car):
        self.__carnet = car
        
        
        

class Main():
    p = Persona()
    carn1 = Carnet(123, "Lopez", "Garcia", "julian",p,"calle falsa",153453)
    cert1 = CertifNac(321, "Lopez", "Garcia","Julian" ,p,1999,12,12)
    p.setCar(carn1)
    p.setCer(cert1)
    
    p2 = Persona()
    carn2 = Carnet(123, "Mamani", "Chura", "luis",p,"calle falsa",6894865)
    cert2 = CertifNac(321, "Mamani", "Chura","luis" ,p,2000,8,15)
    p.setCar(carn1)
    p.setCer(cert1)