class Personaje:
    #Atributos de la clase 
    '''nombre = 'Default'
    fuerza =  0
    inteligencia = 0
    defensa = 0
    vida = 0'''
    
    #Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿Que significa self? Referencia al mismo objeto
    #¿Que es init? Constructor que inicializa el atributo del objeto
    #¿Por que empieza con doble guion bajo? Porque es metodo magico. Dunder
    #¿En que momento se ejecuta el metodo init? Al construir un objeto

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        #self.fuerza += fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        #return self.vida <= 0

    def dañar(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        if daño <=0:
            print(self.nombre, "ha realizado ", daño, "puntos de daño a ", enemigo.nombre)
        else:
            enemigo.vida <= daño
            print(f"{self.nombre}, Ha realizado {daño} puntos de daño a", enemigo.nombre)
            print("Vida de ", enemigo.nombre, "es ", enemigo.vida)

class Guerrero(Personaje):
    #Sobreescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #Sobreescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:",self.espada)

    def elegir_arma(self):
        opcion = int(input("Elige un arma: \n(1)Lanza de obsidiana, daño 10\n(2)Lanza de chaya, daño 5\n>>>>>> "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 5
        else:
            print("Opción no válida")
            #Regresar a dar otra opción
            self.elegir_arma()

    #Sobreescribir cálculo de daño
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class Mago(Personaje):
    #Sobreescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobreescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:",self.libro)

    def elegir_arma(self):
        opcion = int(input("Elige un libro: \n(1)Hechizos de programación, daño 10\n(2)Recetario de chaya, daño 5\n>>>>>> "))
        if opcion == 1:
           self.libro = 10
        elif opcion == 2:
            self.libro = 5
        else:
            print("Opción no válida")
            #Regresar a dar otra opción
            self.elegir_arma()

    #Sobreescribir cálculo de daño
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

michael_jackson = Personaje("Michael Jackson", 20, 15, 10, 100)
tlatoani = Guerrero("Apocalipto", 50, 70, 30, 100, 5)
merlin = Mago("Merlin", 20, 15, 10, 100, 5)
#tlatoani.elegir_arma()
#merlin.elegir_arma()

#Imprimir antes de la tragedia
michael_jackson.imprimir_atributos()
tlatoani.imprimir_atributos()
merlin.imprimir_atributos()

#Ataques masivos
michael_jackson.atacar(tlatoani)
tlatoani.atacar(merlin)
merlin.atacar(michael_jackson)

michael_jackson.imprimir_atributos()
tlatoani.imprimir_atributos()
merlin.imprimir_atributos()

#print(tlatoani.espada)

#Variable del constructor vacío de la clase

#mi_personaje = Personaje("Dante", 10000, 3, 70, 100)
#mi_personaje.imprimir_atributos()
#mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)
#mi_enemigo.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()


#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
#'''mi_personaje.subir_nivel(10, 1, 5)
#print("____________________________")
#mi_personaje.imprimir_atributos()'''

#mi_personaje.nombre = "Jhonatan"
#mi_personaje.fuerza = 30
#mi_personaje.inteligencia = 12
#mi_personaje.defensa = 28
#mi_personaje.vida = 3
#
#print("El nombre del personaje es ", mi_personaje.nombre)
#print("La fuerza del personaje es ", mi_personaje.fuerza)
#print("La inteligencia del personaje es ",mi_personaje.inteligencia)
#print("La defensa del personaje es ",mi_personaje.defensa)
#print("La vida del personaje es ",mi_personaje.vida)'''