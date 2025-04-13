"""
      A
   Calcular el mayor de dos números ingresados por teclado usando un operador
   ternario
      B
   Buscar una palabra en una lista ingresada por teclado usando args y un operador
   ternario

"""
def mayor(valor1, valorB):
   mayor=valor1 if valor1 > valorB else valorB if valorB >valor1 else 'son iguales'
   return mayor

def buscarPalabra(busqueda, *parrafo):
   palabraBuscada = busqueda in parrafo
   return palabraBuscada 

def main():
   # A hay que colocar los verificadores si son numeros
   dato1=int(input("Ingresar primer numero = "))
   dato2=int(input("Ingresar segundo numero = "))   
   print(f"el mayor es = " , mayor(dato1, dato2))
   # B
   palabras=input("Ingrese frase: ")
   aBuscar= input("Palabra de busqueda : ")
   frase = palabras.split(",")
   print(f"se busco {frase}", buscarPalabra(aBuscar, *frase))

main()