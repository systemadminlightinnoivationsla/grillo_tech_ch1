def to_seconds(time_str):
    """
    Convierte una cadena de tiempo en formato 'hh|mm|ss' a un valor total en segundos.
    
    La idea aquí es convertir una representación de tiempo fácil de leer para humanos 
    (horas, minutos y segundos) a un formato numérico (segundos) que sea más adecuado 
    para cálculos aritméticos. Esto facilita operaciones como la suma, comparación y 
    cálculo de promedios.

    Parameters:
    time_str (str): Una cadena que representa un tiempo en el formato 'hh|mm|ss'.

    Returns:
    int: El número total de segundos que representa la cadena de tiempo.
    """
    # 'map(int, time_str.split('|'))' convierte cada componente del tiempo (hh, mm, ss)
    # de una cadena a un entero, separándolos por el delimitador '|'.
    h, m, s = map(int, time_str.split('|'))
    
    # Convertimos todo a segundos: 1 hora = 3600 segundos, 1 minuto = 60 segundos.
    # Este enfoque asegura que cualquier cálculo posterior se realice con valores numéricos simples.
    return h * 3600 + m * 60 + s

def to_hms(seconds):
    """
    Convierte un valor de tiempo en segundos a una cadena de tiempo en formato 'hh|mm|ss'.
    
    Esta función es complementaria a `to_seconds`, transformando el resultado numérico 
    (que es fácil de manipular en cálculos) de vuelta a un formato de tiempo legible por humanos.

    Parameters:
    seconds (int): El tiempo total en segundos.

    Returns:
    str: Una cadena que representa el tiempo en formato 'hh|mm|ss'.
    """
    # Usamos la división entera para calcular cuántas horas, minutos y segundos hay en el total de segundos.
    # Esto permite descomponer el valor numérico en componentes de tiempo convencionales.
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    
    # Formateamos el resultado en 'hh|mm|ss', asegurando que cada componente tenga al menos dos dígitos.
    # Este formato facilita la lectura y comparación de tiempos.
    return f"{h:02}|{m:02}|{s:02}"

def stat(s):
    """
    Calcula el rango, promedio y mediana de una serie de tiempos dados en formato 'hh|mm|ss'.
    
    La función sigue un flujo de trabajo ordenado y eficiente:
    1. Convertimos los tiempos de formato legible a segundos para facilitar los cálculos.
    2. Calculamos el rango, el promedio y la mediana usando operaciones estándar sobre listas.
    3. Convertimos los resultados numéricos de vuelta a un formato de tiempo legible.

    Parameters:
    s (str): Una cadena que contiene varios tiempos en formato 'hh|mm|ss' separados por comas.

    Returns:
    str: Una cadena que resume el rango, promedio y mediana en formato 'hh|mm|ss'.
          Si la entrada está vacía, retorna una cadena vacía.
    """
    # Si la cadena está vacía, devolvemos una cadena vacía inmediatamente.
    # Este es un manejo básico de errores que asegura que la función no intente operar en datos inválidos.
    if not s:
        return ''
    
    # Dividimos la cadena en tiempos individuales, luego convertimos cada tiempo a segundos para facilitar los cálculos.
    # List comprehension se utiliza aquí por su eficiencia y legibilidad.
    times = [to_seconds(time) for time in s.split(', ')]
    
    # Ordenamos la lista de tiempos en segundos para facilitar el cálculo del rango y la mediana.
    # Python usa Timsort, un algoritmo eficiente en la práctica para listas parcialmente ordenadas.
    times.sort()
    
    # Calculamos el rango como la diferencia entre el mayor y el menor tiempo.
    # Esta operación es directa ya que los tiempos están en formato numérico simple (segundos).
    range_seconds = max(times) - min(times)
    
    # Calculamos el promedio sumando todos los tiempos y dividiendo por la cantidad de tiempos.
    # Usamos la división entera para asegurar que el resultado sea un valor entero en segundos.
    avg_seconds = sum(times) // len(times)
    
    # Calculamos la mediana, que requiere considerar si el número de elementos es par o impar.
    # Esto garantiza que la mediana sea representativa de la distribución de tiempos.
    if len(times) % 2 == 1:
        # Si el número de tiempos es impar, la mediana es el valor central en la lista ordenada.
        median_seconds = times[len(times) // 2]
    else:
        # Si el número de tiempos es par, la mediana es el promedio de los dos valores centrales.
        median_seconds = (times[len(times) // 2 - 1] + times[len(times) // 2]) // 2
    
    # Convertimos los resultados de rango, promedio y mediana de segundos a formato 'hh|mm|ss' para la presentación final.
    range_hms = to_hms(range_seconds)
    avg_hms = to_hms(avg_seconds)
    median_hms = to_hms(median_seconds)
    
    # Devolvemos una cadena bien formateada con los resultados solicitados.
    # Este formato es específico del problema y asegura que los resultados sean fáciles de leer y comparar.
    return f"Range: {range_hms} Average: {avg_hms} Median: {median_hms}"

# Casos de prueba para validar la implementación.
# Usamos `assert` para comprobar que la función retorna los resultados esperados.
# Si una aserción falla, el mensaje especificará cuál prueba no pasó, facilitando la depuración.
test_1 = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")
assert test_1 == "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34", \
    "❌ Test 1 failed!"
print("✅ Test 1 passed!")

test_2 = stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")
assert test_2 == "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00", \
    "❌ Test 2 failed!"
print("✅ Test 2 passed!")

test_3 = stat("")
assert test_3 == "", "❌ Test 3 failed!"
print("✅ Test 3 passed!")
