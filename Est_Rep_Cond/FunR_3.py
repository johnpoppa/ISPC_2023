#Escribir una función que calcule el total de una factura tras 
# aplicarle el IVA. La función debe recibir la cantidad sin IVA 
# y el porcentaje de IVA a aplicar, y devolver el total de la 
# factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

def facturacion_total(cant_sin_iva, porc_iva=21):
    total = cant_sin_iva * porc_iva / 100
    return total    

cant_sin_iva = 100

fac_total = facturacion_total(cant_sin_iva)
print('Total de la factura: ', fac_total)

iva_modificar = 10
fac_per_total = facturacion_total(cant_sin_iva, iva_modificar)
print('Total de facturación con iva modificado: ', fac_per_total)

