#SON INMUTABLES

S = "cadena"
S = 'cadena'
S = "" # S = ''
S = r'C:\Users\Documents'
S = "C:\\Users\\Documents" # "C: \U sers \D ocuments"
B = b'texto'
#Contenar -> Pegar
C1 = "Hola"
C2 = "Mundo"
C3 = C1 + C2 #HolaMundo

#Operador de repeticion (Star)
N = 3
C1 * N #HolaHolaHola

#Longitud de una cadena
lenght = len(S)

#Acceder a los caracteres individuales
S[0]

#Formatear una cadena
"Hay {0} sillas".format(34)
"El valor es {0:.2f} en {1} cuotas".format(34.98888,12)
#[tipo_msg] HH:MM:SS - msg
"[{0}] {1} - {2}".format("error","12:00:00","Hubo un error grave, cagamo")

#Metodos de las cadenas
S.find('A')
S.replace('A','B')
S.strip() #Remueve antes y despues los especios en blanco
#_ _ _ Auto _ _ _ -> Auto
#_ _ _ Auto _ _ _ -> _ _ _ Auto
#_ _ _ Auto _ _ _ -> Auto _ _ _
S.split() #' ' -> Space
#La notebook se prendio fuego -> ['La','notebook','se','prendio','fuego']
S.split(',')
#14,13,12 -> [14,13,12]
#S.is* 
S.lower()
S.upper()
S.title()
S.capitalize()
S.endswith()
S.startswith()

#Caracteres de escape o string backslash characters

#\\ -> \
#\' -> '
#\" -> "
#\n -> New line
#\r -> Retorno de carro 
#\t -> Genero 4 espacios
#\v -> Tab vertical
#\xhh -> Hexadecimal (hh) 2 digitos
#\ooo -> Octal (ooo) 3 digitos
#\0 -> Null
#\uhhhh -> Unicode 16bits
#\Uhhhhhhhh -> Unicode 32bits

#Listas,tuplas y diccionarios
L = []
L = [1,'A',['B']]
L = list("Abc") #['A','b','c']
L = list(range())
#Range -> Genera una secuencia de valores:
    #range(N) -> 0,...,N-1
    #range(M,N) -> M,...,N-1
    #range(M,N,P) -> M,M+P,M+2P,...,N-1 (P == paso)

    #range(3) -> 0,1,2
    #range(1,3) -> 1,2
    #range(1,9,3) -> 1,4,7
lenght = len(L)
L[0]
L[0][0]
L + L
#Slicing
L[0:3] #-> [0,1,2]
L[:]
L[:N]
L[N:]
L[::2]

#Metodos
L.append()
L.extend()
L.insert()
L.index()
L.count(X)
L.sort()
L.reverse()
L.copy()
L.clear()
L.pop()
L.remove(X)
del L[0]
del L[i:j]

#Lista por comprension
L = [x**2 for x in range(11)]

#Matrices
M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
M[0][0] #1

#Tuplas
T = ()
T = tuple(L)

#Matriz por comprensión
M = [[0 for _ in range(10)] for _ in range(10)]

#Diccionarios
D = {}
D = {'name':'Mirtha','age':200}
D = {'employe':{'name':'Homer','age':37}}
D = dict(name='Mirtha',age=40)
#Acceder a valores
#Dos formas
D['name'] #Valor (PERO) KeyError
D.get('name',"La cagaste")
D['employe']['name']

#Metodos
D.keys()
D.values()
D.items()
D.copy()
D.clear()
D.update()
D.pop('name',"La cagaste otra vez")
D.setdefault('a',"A")
len(D)
D['salary'] = 1000

#Diccionario por comprensión
D = {x: x*2 for x in range(10)}

#Persona
    #Nombre
    #Edad
    #Altura
    #Residencia
    #Estado civil
    #DNI
persona = {
    "nombre":"Juan",
    "edad": 18,
    "altura":1.9,
    "residencia":{
        "calle":"Juan",
        "altura":243
    },
    "estado_civil":"Soltero",
    "dni":444444
}
print(persona.get("nombre","No existe"))