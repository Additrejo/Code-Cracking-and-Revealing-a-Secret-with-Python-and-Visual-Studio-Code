
print("Hello, cotosoville!")                                  #Usar 'print' para imprimir texto
#This is a comment that won't be interpreted as a command.
#Associate variable town with the value "contosoville"
town = "Contosoville"                                         #asignar la palabara 'Contosoville' a una variable Town

#prnt a massage about the secret location
print("The tow I am looking for is " + town)                  #Imprime la leyenda + la ciudad desde la variable

#Define a power (function) to chant a phrase
def chant( phrase ):                                          #Define una función tipo chant llamada ('phrase')
    #Glue three copies together and prnt it as a massage
    print( phrase + phrase + phrase)                          #Imprime tres veces la función 'phrase'
    
# Invoke the power to chant on the phrase "contosoville!"
chant( "Contosoville!")

def lasso_letter( letter, shift_amoount ):                    #Define una función llama 'Lasso_letter' (letra, número a sumar)
    letter_cod = ord(letter.lower())                          #Asigna a la función 'letter_cod = ord(letter.lower()). la función ord() para convertir la letra a a su código ASCII,


#Cálculo de un carácter descodificcado: Manera sencilla
'''Ahora es el momento de calcular el nuevo carácter. En primer lugar, revise el ejemplo original.
Si empieza con la letra a y quiere obtener la letra c, siga estos pasos:'''
def lasso_letter( letter, shift_amount ):               #Asegúrese de que el valor pasado al parámetro letter está en minúsculas llamando a .lower(). En este caso, la letra que se pasa es a, de modo que .lower() la conservará como a.
    letter_code = ord(letter.lower())                   #Use la función ord() para convertir la letra a a su código ASCII, 97. Guarde el valor de código 97 en la variable letter_code.
    decoded_letter_code = letter_code + shift_amount    #Agregue un valor shift_amount de 2 al valor letter_code de 97 para obtener el nuevo valor de número: 99. Almacene el valor 99 en la variable decoded_letter_code.
    decoded_letter = chr(decoded_letter_code)           #Use la función chr() para descodificar el valor numérico 99 en un carácter para obtener c. (La función chr() simplemente hace lo contrario a la función ord()). Almacene el valor descodificado c en la variable decoded_letter.
    return decoded_letter                               #Devuelva el valor de decoded_letter: c.
#print(lasso_letter('a',2))                              #Intente llamar a esta función mediante el ejemplo anterior para ver si funciona como se espera:
'''Aunque este ejemplo funciona, hay un problema al llegar al final del alfabeto.
Veamos lo que sucedería si ejecutara este código con la primera letra del mensaje secreto real,
N, y la cantidad de desplazamiento, 13.'''
#print(lasso_letter('N',13))

#Para recorrer el alfabeto de forma sencilla, necesita un operador especial llamado mod, que es el signo de porcentaje (%).
three_two = 3 % 2
eleven_four = 11 % 4
five_ten = 5 % 10

print(three_two)
print(eleven_four)
print(five_ten)

'''
#CÁLCULO DE UN CARÁCTER DECODIFICADO: LA MANERA CORRECTA
Con el operador mod en mente, necesita dos variables nuevas:

a_ascii: contiene el valor de código ASCII de la letra "a". Para obtener este valor, se llama a la función ord('a') y se pasa la letra.
alphabet_size: contiene el número de letras del alfabeto, 26.
Esta es la fórmula para averiguar el valor true_letter_code:

*** a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size) ***

Puede revisar esta fórmula con un par de ejemplos.
________________________________________________________________________________________________________
/* Ejemplo 1: letra "a" y desplazamiento de 2 */

Comience con estos dos valores:

letter = 'a'
shift_amount = 2

Variable	            Fórmula	                            Value	     
letter		                                                 "a"	
shift_amount	                               	              2	
letter_code	            ord('a')	                          97	
a_ascii	                ord('a')	                          97	
alphabet_size		                                          26	
true_letter_code	    97 + (((97 - 97) + 2) % 26)	          2   Nota: consulte la explicación detallada de este cálculo después de la tabla.	
decoded_letter	        chr(99)	c

Puede revisar la fórmula de true_letter_code del mismo modo que cualquier otra fórmula matemática.
Siga PEMDAS, donde se evalúa una expresión matemática en el orden de paréntesis, exponentes, multiplicación,
división, suma y resta.

a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

97 + (((97 - 97) + 2) % 26)
97 + ((0 + 2) % 26)
97 + (2 % 26)
97 + 2
99

decoded_letter chr(99) = 'c'
_______________________________________________________________________________________________________
/* Ejemplo 1: letra "a" y desplazamiento de 2 */

Ejemplo 2: letra "N" y desplazamiento de 13
Comience con estos dos valores:

letter = 'N'
shift_amount = 13

Variable	                             Fórmula	                           Value	     
letter		                                                                    'N'	
shift_amount	                                                             	13	
letter_code	                             ord('n')	                            110	
a_ascii                                	 ord('a')	                            97	
alphabet_size		                                                            26	
true_letter_code	               97 + (((110 - 97) + 13) % 26)	            97 Nota: consulte la explicación detallada de este cálculo después de la tabla.	
decoded_letter	                         chr(97)	                            a	

Puede revisar la fórmula de true_letter_code del mismo modo que cualquier otra fórmula matemática 
(acuérdese de PEMDAS):

a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

97 + (((110 - 97) + 13) % 26)
97 + ((13 + 13) % 26)
97 + (26 % 26)
97 + 0
97
'''

'''
___________________________________________________________________________________________________________
Código final
Ahora que tiene la fórmula del descodificador, puede colocarla en su función.
'''
# Definir una función para encontrar la verdad cambiando la letra por la cantidad especificada
def lasso_letter( letter, shift_amount ):
    
    # Invoque la función ord para traducir la letra a su código ASCII 
    # Guarda el código en la variable letter_code
    letter_code = ord(letter.lower())   
    
    # La representación numérica ASCII de la letra minúscula 'a'
    a_ascii = ord('a')
    
    # El número de letras en el alfabeto
    alphabet_size = 26
    
    # La fórmula para calcular el número ASCII de la letra decodificada 
    # Tenga en cuenta el bucle alrededor del alfabeto
    true_letter_code = a_ascii + (((letter_code - a_ascii)+ shift_amount) % alphabet_size)
    
    # Convierte el número ASCII al carácter o letra
    decoded_letter = chr(true_letter_code)
    
    # Devuelve la carta decodificada
    return decoded_letter
print(lasso_letter('a', 2))

'''_____________________________________________________________________________________________________
/* Ejercicio: Descodificación de una palabra completa con un cifrado César */

Ahora que sabe cómo descodificar una letra dada una cantidad de desplazamiento determinada, 
puede descodificar palabras y frases enteras.
Para descifrar una palabra completa, debe invocar la función lasso_letter() para cada letra de la palabra.
A continuación, coloque todas las letras descodificadas en una palabra descodificada.

Esta vez, escribirá una función denominada lasso_word() que tiene dos parámetros: word y shift_amount.
'''
def lasso_word( word, shift_amount ):
    
    '''
    Palabras como colecciones de letras
    Una manera de pensar en las palabras es que son solo colecciones de letras. 
    Por ejemplo, puede pensar en la palabra "Hola" como: 

    #"H" - "o" - "l" - "a" 

    Una variable puede ser un nombre para un fragmento de datos: una palabra, 
    una letra, una fórmula, una función, y así sucesivamente. Python tiene muchas maneras de representar
    colecciones de datos. Una manera es con una lista.

    Una lista es exactamente lo que parece. Una palabra se puede considerar una lista de letras. 
    Aún mejor: Python tiene una manera de recorrer en bucle cada elemento de una lista de uno en uno.

    Iteración de una lista con un bucle for
    Dado que desea invocar la función lasso_letter() en cada letra,
    debe recorrer en bucle cada letra de la palabra que está intentando descodificar.
    '''

    '''_____________________________________________________________________________________________________
    Iteración de una lista con un bucle for
    Dado que desea invocar la función lasso_letter() en cada letra, debe recorrer en bucle cada letra de la palabra que está intentando descodificar.

    Esta es la sintaxis de un bucle for:
    '''    
    #La palabra que se pasa como parámetro se puede considerar una lista de letras. De este modo, puede escribir:
    for letter in word:
        lasso_letter( letter, shift_amount)
        
    #Ahora que comprende esta funcionalidad de Python, puede hacer algo en cada letra de una palabra, como invocar la función lasso_letter().
    
    '''__________________________________________________________________________________________________
/* Invocación de la función lasso_letter() */
Es bastante sencillo invocar la función lasso_letter() en cada letra de una palabra:'''

def lasso_word( word, shift_amount):
    for letter in word:
        lasso_letter( letter, shift_amount )
        
#Recuerde que cuando escribió la función lasso_letter(), la última línea de código de la función era la siguiente:
'''Recuerde que cuando escribió la función lasso_latter(), la última línea de código de la función era la siguiente:

# send the decoded letter back
return decoded_letter 

Este código se denomina una instrucción "return". 
Esta instrucción devuelve el valor a la línea que invocó la función. 
Para capturar ese valor devuelto, lo único que tiene que hacer es usar una variable:
'''
def lasso_word( word, shif_amount):
    
    for letter in word:
        decoded_letter = lasso_letter(letter, shif_amount)
#Ahora va a invocar una función que escribió, lasso_letter(), desde una nueva función que va a escribir ahora: lasso_word().

'''___________________________________________________________________________________________________________

***Disposición de letras juntas***
Con el código que acaba de escribir, tendrá un valor en la variable decoded_letter. Cuando el bucle se ejecuta de nuevo, la variable se actualiza.

Puede realizar un seguimiento del código para ver cómo funciona:

word = "gdkkn"
shift_amount = 1

Loop
iteration               	Valor de                      Valor de
                            letter	                    decoded_letter	

1	                          'g'	                          'h'	
2	                          'd'	                          'e'	
3	                          'k'	                          "l"	
4	                          'k'	                          "l"	
5	                          'n'	                          "o"
Se le deja una variable denominada decoded_letter que tiene un valor solo con la letra "o". 
Pero lo que quería era una variable denominada decoded_word para tener el valor hello. Recuerde que, 
a partir de los conceptos básicos de Python que hemos revisado anteriormente en este módulo, puede usar 
el signo más (+) entre dos palabras o letras para combinarlas.

'''
'''
def lasso_word( word, shift_amount ):
    
    decoded_word = ""
    
    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amount)
        decoded_word = decoded_word + decoded_letter
        
    return decoded_word
'''
'''Con esté código la palabra completa se almacena ahora en la variable decoded_word. 
Puede devolver este valor a la línea donde se invocó esta función. Puede realizar un seguimiento del 
código como antes:

Loop                          Valor de                     Valor de                 Valor de
iteration                     letter                       decoded_letter	        decoded_word
1	                           'g'	                            'h'                	     "h"	
2	                           'd'	                            'e'	                     "he"	
3	                           'k'	                            "l"	                     "hel"	
4	                           'k'	                            "l"	                     "hell"	
5	                           'n'	                            "o"	                     "Hola"
'''
'''__________________________________________________________________________________________________________
***Creación de comentarios en el código***

No olvide agregar comentarios al código, para que sepa exactamente lo que sucede. 
(Si vuelve a este ejercicio más adelante, no querrá tener que descifrar su propio código).

'''

'''__________________________________________________________________________________________________________
***Revisión del archivo completo***
Ahora que ha escrito dos funciones lasso, el archivo completo decrypt.py debe tener este aspecto:
'''

# Definir una función para encontrar la verdad en un mensaje secreto
# Cambia las letras de una palabra en una cantidad específica para descubrir la palabra oculta

# Define a function to find the truth by shifting the letter by a specified amount
def lasso_letter( letter, shift_amount ):
    # Invoque la función ord para traducir la letra a su código ASCII
    # Guarda el valor del código en la variable llamada letter_code
    letter_code = ord(letter.lower())
    
    # La representación numérica ASCII de la letra a minúscula
    a_ascii = ord('a')

    # El número de letras en el alfabeto
    alphabet_size = 26

    # La fórmula para calcular el número ASCII de la letra decodificada
    # Tenga en cuenta el bucle alrededor del alfabeto
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Convierte el número ASCII al carácter o letra
    decoded_letter = chr(true_letter_code)

    # Devuelve la carta decodificada
    return decoded_letter

# Definir una función para encontrar la verdad en un mensaje secreto 
# Cambia las letras de una palabra en una cantidad específica para descubrir la palabra oculta
def lasso_word( word, shift_amount ):

    # Esta variable se actualiza cada vez que se decodifica otra letra
    decoded_word = ""

    # Este ciclo for itera a través de cada letra en el parámetro de palabra
    for letter in word:
        # La función lasso_letter() se invoca con cada letra y la cantidad de cambio 
        # El resultado (la letra decodificada) se almacena en una variable llamada decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # El valor decoded_letter se agrega al final del valor decoded_word
        decoded_word = decoded_word + decoded_letter

    # La palabra decodificada se devuelve a la línea de código que invocó esta función
    return decoded_word

# Intenta decodificar la palabra "terra"
print( "Shifting terra by 13 gives: \n" + lasso_word( "terra", 13 ) )

'''__________________________________________________________________________________________________________
***EJERCICIO: USO DEL DESCODIFICADOR Lasso PARA MOSTRAR EL MENSAJE SECRETO+++
Este es el mensaje secreto que debe descifrar:
(Vease la imagen en la carpeta de archivos en el repositorio)

Después de nuestro análisis en este módulo, esto es lo que debe hacer para descodificar el mensaje:

La palabra "Ncevy" debe desplazarse 13 veces.
La palabra "gpvsui" debe desplazarse 25 veces.
La palabra "ugflgkg" debe desplazarse 18 veces.
La palabra "wjmmf" debe desplazarse 1 vez.

***Adición de instrucciones print***

Al igual que cuando probó la función lasso_word() en la palabra "terra" y la desplazó 13 veces, 
puede agregar instrucciones print() a la parte inferior del archivo decrypt.py para imprimir todas las palabras descodificadas.
'''

print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )

'''Este código pertenece a Descifrado de código y revelación de un secreto con Python y Visual Studio Code de Learn Microsoft'''