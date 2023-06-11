# Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.
# Ej 2

monto = float(input('Ingrese el monto a abonar: '))
tipo_pago = int(input('Seleccione el tipo de pago (1: Contado, 2:Tarjeta de Crédito, 3: Tarjeta de Débito): '))

descuento = 0
intereses = 0

if tipo_pago == 1:
    descuento = monto * 0.10
    monto_total = monto - descuento
elif tipo_pago == 2:
    intereses = monto * 0.10
    monto_total = monto + descuento
elif tipo_pago == 3:
    intereses = monto * 0.05
    monto_total = monto - descuento
else:
    print('Forma de pago no válida')
    
print('Importe: $', monto)
print('Descuento: $', descuento)
print('Intereses: $', intereses)
print('Monto Total: $', monto_total)
