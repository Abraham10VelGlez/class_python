print('hola mundo')

dictamen_nobre = 'Empresa de datos del StudioA'
print(dictamen_nobre)

entero = 10

decimal = 10.501

boolean_verdadero=True

boolean_falso=False

#esttructturas
listaconindice = [ 15, 30 , 45 , 55 , 80 , 100]

print(listaconindice[5])
#listas de texto o listas mixtas





#diccionario de numero a texto
avaluos = {
    100 : 'Dictamen/Bimbo/000100',
    104 : 'Dictamen/Bimbo/000100',
    108 : 'Dictamen/Bimbo/000100'
}
print(avaluos[108])
#diccionario de  texto a texto

#diccionario de  texto a listas


#constantes
#su valor no puede ser cambiantes
Pi= 3.1416
print(Pi)


#Operadores simbolos para hacer operaciones + - * /
print(5+5)
print(10+5)
print(5-5)
print(5/5)

#Operadores comparativos
#print(5==5)
#print(10 == '10')
#print(5 != 10)
#print(100>=10)
#print(20<=10)


#operadores logicos , util en condicionales
print(True or True)
print(True or False)
print(False or True)
print(False or False)



acceso_autorizado_al_codiminio = True


if acceso_autorizado_al_codiminio:
    print('Puede acceder al condominio')
else:
    print('No puede acceder al condominio')

       

valor = 10000 #2

if valor == 1000:
    print('son iguales')
elif valor <= 15:
    print(f"no es menor a 15 el numero {valor}")
else:
    print('este numero es mayor de 1000')
    
    
    
tipologia = 'HB3'
#comparacion de varios casos
match tipologia:
    case 'HB1':
        print(f"escogiste la tipología {tipologia}")
    case 'HB3':
        print(f"escogiste la tipología {tipologia}")
    case 'HC1':
        print(f"escogiste la tipología {tipologia}")
    case _:
        print('No tenemos conocimiento acerca de esa tipología')
        
        
        
#funciones (bloqu de codigo)


def funcion1( x , y ):
    return x + y


resultado = funcion1(5,5)
print(resultado)
    

#retornar lista
listaconindicexfuncion = [ 15, 30 , 45 , 55 , 80 , 100]
def funcion2( lista ):
    return lista[0] + lista[2]

    
resultado2 = funcion2(listaconindicexfuncion)
print(resultado2)

#ciclos,bucles o loops

list = [ 'madera' , 'concreto' , 'aluminio', 'tablaroca']

for listar in list:
    print(listar)


lista_numeros = [ 15, 30 , 45 , 55 , 80 , 100]
for listar2 in lista_numeros:
    print(listar2 * 2)


numeroinicio = 1
numerotermino = 99
while numeroinicio < numerotermino: #<=
    print(numeroinicio)
    numeroinicio += 1
    


#OBJETOS
#TRAER DATOS DEL MUNOD REAL A UN OBJETO
inmobiliaria = {
  "nombredelsitio": "Casa de leones",
  "propiedades": [
    {
      "id": 1,
      "titulo": "Departamento en el centro de la ciudad",
      "tipo": "renta",
      "precio": 15000,
      "moneda": "MXN",
      "ubicacion": {
        "direccion": "Av. Reforma 123, Ciudad de México",
        "ciudad": "CDMX",
        "pais": "México"
      },
      "caracteristicas": {
        "metros_cuadrados": 80,
        "habitaciones": 2,
        "baños": 2,
        "estacionamientos": 1,
        "amueblado": True
      },      
      "descripcion": "Hermoso departamento en el centro de la ciudad con vista panorámica.",
      "contacto": {
        "nombre": "Carlos Pérez",
        "telefono": "+52 55 1234 5678",
        "email": "carlos@inmobiliaria.com"
      }
    },
    {
      "id": 2,
      "titulo": "Casa en zona residencial",
      "tipo": "venta",
      "precio": 3500000,
      "moneda": "MXN",
      "ubicacion": {
        "direccion": "Calle Primavera 45, Guadalajara",
        "ciudad": "Guadalajara",
        "pais": "México"
      },
      "caracteristicas": {
        "metros_cuadrados": 200,
        "habitaciones": 4,
        "baños": 3,
        "estacionamientos": 2,
        "amueblado": False
      },      
      "descripcion": "Espaciosa casa con jardín y terraza en zona residencial tranquila.",
      "contacto": {
        "nombre": "Ana López",
        "telefono": "+52 33 5678 9101",
        "email": "ana@inmobiliaria.com"
      }
    }
  ]
}


print(inmobiliaria['nombredelsitio'])

#print(inmobiliaria['propiedades'])
#print(inmobiliaria['propiedades'][0]['id'])


def filtrardatos(diccionario):
    return ('La %s es una inmobiliaria que vende un %s' % (diccionario['nombredelsitio'], diccionario['propiedades'][0]['titulo'] ))    

print(filtrardatos(inmobiliaria))


#Clases

class tiposdeviviendas:
    def __init__(self,nombre,tipologia,edad,numero_pisos):
        self.nombre = nombre
        self.tipologia = tipologia
        self.edad = edad
        self.numero_pisos = numero_pisos
    
    def llamado(self):
        return '%s tiene una tipología %s, con una edad de %s años y tiene %s pisos construidos' % (self.nombre, self.tipologia, self.edad, self.numero_pisos )

#crea un objeto de la clase
objeto = tiposdeviviendas('Infonavit','HB1',10,2)
#mencion del objeto de la clase
print(objeto.llamado()) 

