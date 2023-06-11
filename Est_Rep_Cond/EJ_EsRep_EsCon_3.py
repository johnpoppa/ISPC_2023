# Ingresar las edades y el sexo de 15 personas y determinar cuántas son
# mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.
#Ej 3

cont_fem = 0
cont_mas = 0
may_edad = 0
men_edad = 0

for i in range(15):
    edad = int(input('Ingrese la edad de la persona {}: '.format(i+1)))
    sexo = input('Ingrse el sexo de la persona {} F/M : '.format(i+1))
    
    if sexo == 'F' or sexo == 'f':
        cont_fem += 1
    elif sexo == 'M' or sexo == 'm':
        cont_mas += 1

    if edad >= 18:
        may_edad += 1
    else:
        men_edad += 1

print("Cantidad de mujeres:", cont_fem)
print("Cantidad de varones:", cont_mas)
print("Cantidad de personas mayores de edad:", may_edad)
print("Cantidad de personas menores de edad:", men_edad)
    

