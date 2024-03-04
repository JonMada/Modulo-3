#Imaginemos que tenemos una empresa de paquetería y cada paquete tiene un orden de prioridad de envio:

index_priority = {
    (1,'premier') : [12,13,154],
    (1,'luxury') : [89,34,23],
    (2, 'standard') : [56,52,87]
}

#Las claves representan el orden de prioridad de envio y el nombre del servicio.
#Los valores representan los identificadores de los envios.

#Esta estructura es útil si por ejemplo, queremos saber cuáles son los paquetes con mayor prioridad.

print(list(index_priority.keys()))