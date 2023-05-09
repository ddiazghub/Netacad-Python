# Ejecuta bubblesort en las encuesta dependiendo de los id de los clientes
def bubblesort_encuesta(lst):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(lst) - 1):
            if lst[i][0].get_id() > lst[i + 1][0].get_id():
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swaps = True


# Clase cliente con atributos id y nombres y getters
class Cliente:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def get_id(self):
        return self.__id


# Clase registro, contiene una lista de encuestas como atributo
class Registro:
    def __init__(self):
        self.__encuestas = []

    # Método registrar, añade una encuesta al registro
    def registrar(self, id_cliente, nombre_cliente, tipo_prenda):
        self.__encuestas.append((Cliente(id_cliente, nombre_cliente), tipo_prenda))

    # Método imprimir, imprime todas las encuestas
    def imprimir(self):
        print("")
        for encuesta in self.__encuestas:
            print("Identificación cliente: ", encuesta[0].get_id(), ", Nombre: ", encuesta[0].get_nombre(), ", Tipo de prenda: ", encuesta[1], sep = "")
        print("")

    # Método imprimir_ord_id, imprime todas las encuestas ordenadas por el id del cliente
    def imprimir_ord_id(self):
        encuestas_ord = self.__encuestas[:]
        bubblesort_encuesta(encuestas_ord)
        print("")
        for encuesta in encuestas_ord:
            print("Identificación cliente: ", encuesta[0].get_id(), ", Nombre: ", encuesta[0].get_nombre(), ", Tipo de prenda: ", encuesta[1], sep = "")
        print("")

    # Método consultar_por_prenda, imprime las encuestas en las cuales el tipo de prenda sea el especificado como parámetro
    def consultar_por_prenda(self, tipo_prenda):
        consulta = []
        print("")
        for encuesta in self.__encuestas:
            if encuesta[1] == tipo_prenda:
                consulta.append(encuesta)
        print("")
        
        for encuesta in consulta:
            print("Identificación cliente: ", encuesta[0].get_id(), ", Nombre: ", encuesta[0].get_nombre(), ", Tipo de prenda: ", encuesta[1], sep = "")
        print("")


# Clase de interfaz de línea de comandos con una tupla de comandos y una instancia de la clase Registro como atributos.
class CLI:
    def __init__(self, registro):
        self.__comandos = ("registrar", "imprimir", "imprimir_organizado", "consultar", "ayuda", "salir")
        self.__registro = registro

    # Método menu_ayuda, imprime los comandos
    def menu_ayuda(self):
        print("\nBienvenido, los comandos para usar el presente sistema son:\n")
        print("registrar <id> <nombre> <apellido> <prenda>              - Registra una encuesta.") # Ejemplo: > registrar 12345678 Pepito Pérez formal
        print("imprimir                                                 - Imprime las encuestas registradas")
        print("imprimir_organizado                                      - Imprime las encuestas registradas ordenadas por id")
        print("consultar <tipo_prenda>                                  - Imprime las encuestas con el tipo de prenda especificado") # Ejemplo: > consultar 
        print("ayuda                                                    - Muestra este menú.")
        print("salir                                                    - Salir del programa.\n")

    # Método ejecutar, contiene el hilo principal de la aplicación, en el cual se leen y ejecutan los comandos ingresados
    def ejecutar(self):
        prendas = ("formal", "informal", "deportiva")
        self.menu_ayuda()
        while True:
            print("> ", end = "")
            comando = input().split(" ")
            try:
                if comando[0] not in self.__comandos:
                    raise BaseException
                if comando[0] == self.__comandos[0]:
                    if comando[4] in prendas:
                        self.__registro.registrar(int(comando[1]), comando[2] + " " + comando[3], comando[4])
                    else:
                        print("\nTipo de prenda incorrecto. Se aceptan los tipos \"formal\", \"informal\" y \"deportiva\"\n")
                if comando[0] == self.__comandos[1]:
                    self.__registro.imprimir()
                if comando[0] == self.__comandos[2]:
                    self.__registro.imprimir_ord_id()
                if comando[0] == self.__comandos[3]:
                    if comando[1] in prendas:
                        self.__registro.consultar_por_prenda(comando[1])
                    else:
                        print("\nTipo de prenda incorrecto. Se aceptan los tipos \"formal\", \"informal\" y \"deportiva\"\n")
                if comando[0] == self.__comandos[4]:
                    self.menu_ayuda()
                if comando[0] == self.__comandos[5]:
                    print("\nSe ha cerrado el programa.\n")
                    break
            except:
                print("Error: Comando o parámetros incorrectos.")



# Main program
cli = CLI(Registro())
cli.ejecutar()



