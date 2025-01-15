class Personaje:
    #Atributos de la clase 
    '''nombre = 'Default'
    fuerza =  0
    inteligencia = 0
    defensa = 0
    vida = 0'''
    
    #Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    #¿Que significa self? Referencia al mismo objeto
    #¿Que es init? Constructor que inicializa el atributo del objeto
    #¿Por que empieza con doble guion bajo? Porque es metodo magico. Dunder
    #¿En que momento se ejecuta el metodo init? Al construir un objeto

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        #self.__fuerza += fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        #return self.__vida <= 0

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado ", daño, "puntos de daño a ", enemigo.__nombre)
        print("Vida de ", enemigo.__nombre, "es ", enemigo.__vida)
    
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0
            print("Error, valor negativo")
        else:
            self.__fuerza = fuerza

#Variable del constructor vacío de la clase
mi_personaje = Personaje("Dante", 100, 3, 70, 100)
#mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
#mi_enemigo.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()
#mi_personaje.fuerza = 0
#mi_personaje.imprimir_atributos

mi_personaje.set_fuerza(-5)
print(mi_personaje.get_fuerza())

#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
'''mi_personaje.subir_nivel(10, 1, 5)
print("____________________________")
mi_personaje.imprimir_atributos()'''
'''
mi_personaje.__nombre = "Jhonatan"
mi_personaje.__fuerza = 30
mi_personaje.__inteligencia = 12
mi_personaje.__defensa = 28
mi_personaje.__vida = 3
'''
'''
print("El nombre del personaje es ", mi_personaje.__nombre)
print("La fuerza del personaje es ", mi_personaje.__fuerza)
print("La inteligencia del personaje es ",mi_personaje.__inteligencia)
print("La defensa del personaje es ",mi_personaje.__defensa)
print("La vida del personaje es ",mi_personaje.__vida)'''


