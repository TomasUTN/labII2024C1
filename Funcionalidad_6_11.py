# FUNCION 6

def Calcular_promedio(suma,cantidad):

    """
    Calcula el promedio entre la suma de las edades
    :param suma: Resultado de la suma de todas las edades
    :param cantidad: Cantidad de edades ingresadas
    :return: Promedio de las edades ingresadas
        
    """
    try:
        return suma/cantidad
    except:
        print("ERROR")

# FUNCION 11

def orden_asc(edades):
    """
    Ordena listas de menor a mayor
    :param edades: Lista con numeros
    edades
    :return: Lista con numeros ordenados de forma ascendente
    """
    try:
        lista_ordenada = sorted(edades)
    except:
        print("ERROR")
    return lista_ordenada


