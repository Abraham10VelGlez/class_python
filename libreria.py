
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
#print(objeto.llamado()) 


#se puede reutilizar el codigo 
objeto = tiposdeviviendas('La casa del presidente','IA1',30,5)

#print(objeto.llamado()) 

