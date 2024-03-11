#Ejemplo práctico

def saludos (momento_dia, *args, **kwargs):
    print(f'Hola {' '.join(args)}. Espero que estes teniendo una buena {momento_dia}.')

    if kwargs: #Si hay 'kwargs'
        print('Esta es tu lista de tareas')
        for key, val in kwargs.items():
            print(f'{key} --> {val}')


saludos('mañana',
       'Jon', 'Madariaga', 'Ortega',
       primera_tarea = 'Lavar el coche',
       segunda_tarea = 'Comprar el pan',
       tercera_tarea = 'Preparar la comida')
