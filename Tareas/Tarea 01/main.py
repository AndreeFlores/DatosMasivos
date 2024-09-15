COLUMNAS = [
    'Airline', # Aerolinea
    'CRSDepTime', #Hora de salida programada
    'DepTime', #Hora de salida actual
    'DepDelay', #Diferencia en minutos entre CRSDepTime y DepTime, tiempos negativos significa salidas tempranas
    'CRSArrTime',
    'ArrTime', #Hora de llegada
    'ArrDelay', #Diferencia de minutos entre la llegada programada y la hora de llegada, tiempos negativos significa llegadas tempranas
    'ActualElapsedTime', #Tiempo de vuelo verdadero
    'CRSElapsedTime', #Tiempo de vuelo programado
    'Distance', #Distancia entre aeropuertos en millas
    'Year', #Año del vuelo
    'Month', #Mes del vuelo
    'DayofMonth', #Dia del mes del vuelo
    'DayOfWeek', #Dia de la semana del vuelo
    'Tail_Number', #Numero de la cola, código para identificar la aeronave
    'Flight_Number_Operating_Airline', #Numero del vuelo
    
    'Origin', #Aeropuerto de origen
    'OriginAirportID', 'OriginAirportSeqID', #codigos del aeropuerto de origen
    'OriginCityName', #Nombre de la ciudad del aeropuerto de origen
    'OriginStateName', #Nombre de estado del aeropuerto de origen
    
    'Dest', #Aeropuerto de destino
    'DestAirportID', 'DestAirportSeqID', #codigos del aeropuerto de destino
    'DestCityName', #Nombre de la ciudad del aeropuerto de destino
    'DestStateName', #Nombre de estado del aeropuerto de destino
    
    'Cancelled', #El vuelo fue cancelado, 1 = Sí
    
    'Diverted', #Si el vuelo fue desviado, 1 = Sí
]

def main():
    pass

if __name__ == "__main__":
    main()