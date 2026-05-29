class FormatoInvalidoException(Exception):
    def __init__(self):
        super().__init__("solo se permiten formatos mp3, mp4 y mkv")
        
class DuracionInvalidaException(Exception):
    def __init__(self):
        super().__init__("Error: Duración fuera de los límites permitidos")
        

class Musica:
    def __init__(self, nom, form, dur, comp):
        self.__nombre = nom
        self.__formato = form
        self.__duracion = dur
        self.__compositor = comp
    
    def __str__(self):
        return f"nombre: {self.__nombre}, formato: {self.__formato}, duracion: {self.__duracion}, compositor: {self.__compositor}"

class PlayList:
    def __init__(self, nom):
        self.__nombre = nom
        self.__musica = []
    
    def agregarCancion(self):
        nomb = input("Nombre de la cancion: ")
        form = input("formato de la cancion: ")
        while True:
            try:
                if(form == "mp3" or form == "mp4" or form =="mkv"):
                    break
                else:
                    raise FormatoInvalidoException()
            except FormatoInvalidoException as f:
                print(f)
                form = input("formato de la cancion: ")
        dur = int(input("Duracion de la cancion: "))
        try:
            if(dur >30):
                raise DuracionInvalidaException()
        except DuracionInvalidaException as d:
            print(d)
            dur = 0
        comp = input("Compositor: ")
        self.__musica.append(Musica(nomb, form, dur, comp))
            
    def __str__(self):
        mus = ""
        for m in self.__musica:
            mus = mus +"1. "+ m.__str__() +"\n"
        return f"PlayList: {self.__nombre} \n {mus}"
            

class Main():
    p = PlayList("clasicas")
    p.agregarCancion()
    print(p)