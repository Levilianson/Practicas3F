"""
    A.
    Escribe un programa que intente dividir dos números. Si el segundo número es cero,
    captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
    B.
    Escribe un programa que intente sumar un número y una cadena. Si se produce un error
    de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
    C.
    Escribe un programa que intente acceder a una clave que no existe en un
    diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
    un mensaje de error al usuario.
    D.    
    Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
    FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
    embargo, también intenta crear el archivo si no existe.
    E. 
    Escribe un programa que intente dividir dos números. Si el segundo número es cero,
    captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
    captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
"""
def dividirCero(numero1, numero2):
    try:
        #intento castear los numeros
        resultado = int(numero1) / int(numero2)
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except ValueError:
        print("No se pudo dividir error de datos")
    else:
        print(resultado)
    


def sumar(numero1, numero2):
    try:
        resultado = 10 + "Hola"
    except TypeError:
        print("No se pueden sumar un número y una cadena.")

def buscarKeyDiccionario(diccio,clave):
    try:
        codigo = diccio[clave]
        print(codigo)
    except KeyError:
        print(f"La clave '{clave}' no existe.")


def leerArchivo(archivo):
    try:        
        with open(archivo, 'r') as arch:        
            print(arch.read())
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Intentando crearlo...")
        with open(archivo, 'w') as arch:
            arch.write(f"{archivo}Creado con éxito")

def dividir(dividendo, divisor):
    comprobar(dividendo)
    comprobar(divisor)    
    resultado = dividirCero(dividendo,divisor)   
    

def comprobar(numero):
    try:    
        valor = int(numero)
    except ValueError:
        print(f"Error: El numero {numero} no es válido.")
    
    
def main():
    # A
    numero1=10
    numero2=0    
    dividirCero(numero1,numero2)
    # B
    cadena="chau"
    sumar(numero1,cadena)
    # C
    dicc = {"x": 1, "z": 2}
    buscarKeyDiccionario(dicc, "M")
    buscarKeyDiccionario(dicc,"x")
    # D
    leerArchivo('texto.txt')
    # E
    letra='a'
    numero3=2
    dividir(letra,numero1)
    dividir(numero1,letra)
    dividir(numero1, numero3)

main()