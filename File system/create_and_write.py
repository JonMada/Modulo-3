file_builder = open("logger.txt", "w+") #Modo escritura (w) y en caso de no existir el archivo lo crea (+). En caso de exisitir, sobrescribrimos sobre los datos existentes.

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n") #Write() no crea el salto de línea. Hay que especificarlo (\n).

file_builder.close() #Cerramos el archivo. Garantiza que todos los datos se guarden correctamente