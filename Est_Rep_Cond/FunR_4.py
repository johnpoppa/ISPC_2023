#Escribir una función que convierta un número decimal en los 
# otros dos sistemas: Binario y Hexadecimal. Mostrar mensajes 
# pertenecientes a cada función.

def conv_dec(decimal):
    def conv_bin(decimal):
        binario = bin(decimal)
        return binario
    
    def con_hexa(decimal):
        hexadecimal = hex(decimal)
        return hexadecimal
    
    binario = conv_bin(decimal)
    hexadecimal = con_hexa(decimal)
    
    print('Numero decimal: ', decimal)
    print('Numero binario: ', binario)
    print('Numero hexadecimal: ', hexadecimal)
    

numero_decimal = 52
conv_dec(numero_decimal)
    
