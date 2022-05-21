#Modelos la realidad, lo hacemos por medio de objetos (Generalmente)
#En Python, para definir y modelar los objetos por medio de clases, se usan palabras reservadas

class Persona:
    #Todas las variables de la clase
    #SON PARA TODOS OBJETOS VISIBLES
    __contadorPersonas = 0

    #init es un "constructor" en Python
    def __init__(self, nombre="Homero",apellido="Simpson") -> None:
        self.__nombre   = nombre
        self.__apellido = apellido
        Persona.__contadorPersonas+=1
        print("Hola soy",self.__nombre,self.__apellido,"soy la persona #",self.__contadorPersonas)
    
    def saludar(self):
        print("Hola soy",self.__nombre)
def main():
    foo = Persona("Mr","Burns") #Creando el objeto
    print(foo)
    foo1 = Persona("Bart","Simpson") #Creando el objeto
    print(foo1)
    foo2 = Persona() #Creando el objeto
    print(foo2)
    foo.saludar()
    foo1.saludar()
    foo2.saludar()
    #Persona.__contadorPersonas+=1
    #print(Persona.__contadorPersonas)
    pass
if __name__=="__main__":
    main()