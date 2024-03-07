#Estructura básica

x = 3
resultado = 'x menor que 3' if x<3 else 'x mayor que 3' if x>3 else 'x es igual a 3'
print(resultado)

#Ejemplo
rol = 'usuario_registrado'
autorización_acceso_web = 'puedes acceder' if rol == 'master' else 'puedes acceder con restricciones' if rol == 'usuario_registrado' else 'no puedes acceder'
print(autorización_acceso_web)

#La estructura es la misma que los condicionales al uso
if rol == 'master':
    autorización_acceso_web = 'puedes acceder'
elif rol == 'usuario_registrado':
    autorización_acceso_web = 'puedes acceder con restricciones'
else:
    autorización_acceso_web = 'no puedes acceder'

print(autorización_acceso_web)