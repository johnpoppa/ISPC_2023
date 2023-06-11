# Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.
# EJ 4

num = int(input('Ingrese un número del 1 al 7: '))

if num == 1:
    dia_sem = 'Lunes'
elif num == 2:
    dia_sem = 'Martes'
elif num == 3:
    dia_sem = 'Miércoles'
elif num == 4:
    dia_sem = 'Jueves'
elif num == 5:
    dia_sem = 'Viernes'
elif num == 6:
    dia_sem = 'Sábado'
elif num == 7:
    dia_sem = 'Domingo'
else:
    dia_sem = 'El dato ingresado debe ser un número del 1 al 7.'

print('El número ', num, 'tiene asignado el día de semana ',dia_sem)
