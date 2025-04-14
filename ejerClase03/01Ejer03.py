"""
      A
   Calcular el mayor de dos números ingresados por teclado usando un operador
   ternario
      B
   Buscar una palabra en una lista ingresada por teclado usando args y un operador
   ternario
      C
   Determinar si un número es par o impar
      D
   Calcular el promedio de una lista de números usando args y un operador ternario
   Imprimir un mensaje de error si no se pasan suficientes argumentos


"""
def esPar(valor1):
   return "par" if valor1 % 2 == 0 else "impar"

def promedio(*numeros):
   resultado = round(sum(numeros)/len(numeros),1) if len(numeros)>=1 else -1
   return resultado

def mayor(valor1, valorB):
   mayor=valor1 if valor1 > valorB else valorB if valorB >valor1 else 'son iguales'
   return mayor

def buscarPalabra(busqueda, *parrafo):
   palabraBuscada = busqueda in parrafo
   return palabraBuscada 

def main():
   # A hay que colocar los verificadores si son numeros
   #dato1=int(input("Ingresar primer numero = "))
   # dato2=int(input("Ingresar segundo numero = "))   
   # print(f"el mayor es = " , mayor(dato1, dato2))
   # # B
   # palabras=input("Ingrese frase: ")
   # aBuscar= input("Palabra de busqueda : ")
   # creo una lista que es iterable con el separador de espacio
   # frase = palabras.split(" ")
   # print(f"no buscas nada" if aBuscar =="" else aBuscar + " esta en " + palabras 
   #       if buscarPalabra(aBuscar, *frase)else aBuscar +" no esta en "+palabras)
   # # C
   # print(f"El numero {dato1} es "+ esPar(dato1))     
   # D
   valores={6,5,8,9,1,0,4,6}
   #valores={9}     
   print(f"el promedio de {valores} es {promedio(*valores)}" if len(valores)>1 else "faltan numeros")
main()