'''Documentacion consumo de fechas en Python'''
# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Importamos la función system para ejecutar comandos del sistema
from os import system
# ==========================================================
# TRABAJANDO CON FECHAS Y HORAS (datetime)
# ==========================================================
# datetime  : para crear / manejar fechas y horas
# timedelta : para sumar o restar tiempo (días, horas, etc.)
# ==========================================================
from datetime import datetime, timedelta
# ----------------------------------------------------------
# 9) CAMBIAR IDIOMA/LOCALIZACIÓN (locale) - CON CONTROL DE ERRORES
# ----------------------------------------------------------
import locale

# Intentamos limpiar la consola en Linux / macOS.
# Si falla (retorna distinto de 0), usamos el comando de Windows.
if system("clear") != 0:
    system("cls")


# ----------------------------------------------------------
# 1) OBTENER FECHA Y HORA ACTUAL
# ----------------------------------------------------------
# datetime.now() devuelve la fecha y hora del sistema en este momento
fecha_actual = datetime.now()
print(f"1) Fecha y hora actual: {fecha_actual}")


# ----------------------------------------------------------
# 2) CREAR UNA FECHA Y HORA ESPECÍFICA
# ----------------------------------------------------------
# datetime(año, mes, día, hora, minuto, segundo)
fecha_especifica = datetime(2023, 1, 12, 15, 30, 0)
print(f"2) Fecha específica: {fecha_especifica}")


# ----------------------------------------------------------
# 3) FORMATEAR FECHAS Y HORAS (strftime)
# ----------------------------------------------------------
# strftime convierte datetime -> string (texto) con el formato deseado
# %Y = año 4 dígitos (2026)
# %y = año 2 dígitos (26)
# %m = mes (01-12)
# %d = día (01-31)
# %H = hora 24h (00-23)
# %M = minuto (00-59)
# %S = segundo (00-59)

fecha_formateada_1 = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
fecha_formateada_2 = fecha_actual.strftime("%d/%m/%y %H:%M:%S")

print(f"3) Fecha formateada (ISO): {fecha_formateada_1}")
print(f"3) Fecha formateada (Latam): {fecha_formateada_2}")


# ----------------------------------------------------------
# 4) OPERACIONES CON FECHAS Y HORAS (timedelta)
# ----------------------------------------------------------
# Sumar 5 días a la fecha actual
cinco_dias_mas = fecha_actual + timedelta(days=5)
print(f"4) Fecha futura (5 días después): {cinco_dias_mas}")

# Restar 2 horas a la fecha actual
dos_horas_antes = fecha_actual - timedelta(hours=2)
print(f"4) Fecha pasada (2 horas antes): {dos_horas_antes}")

# Medio día después usando 0.5 días (12 horas)
medio_dia_despues = fecha_actual + timedelta(days=0.5)
print(f"4) Medio día después: {medio_dia_despues}")


# ----------------------------------------------------------
# 5) OBTENER COMPONENTES INDIVIDUALES
# ----------------------------------------------------------
ano = fecha_actual.year
mes = fecha_actual.month
dia = fecha_actual.day
hora = fecha_actual.hour
minuto = fecha_actual.minute
segundo = fecha_actual.second

print(
    f"5) Año:{ano}, Mes:{mes}, Día:{dia}, Hora:{hora}, Minuto:{minuto}, Segundo:{segundo}"
)


# ----------------------------------------------------------
# 6) DIFERENCIA ENTRE DOS FECHAS
# ----------------------------------------------------------
# Ojo: si restás "fecha_actual - fecha_futura", la diferencia será NEGATIVA
# porque la fecha futura aún no ocurrió.

mi_cumpleanos = datetime(2026, 11, 27, 15, 30, 0)

diferencia = mi_cumpleanos - fecha_actual  # así te da "cuánto falta"
print(f"6) Tiempo que falta para mi cumpleaños: {diferencia}")

# Podemos obtener días y segundos por separado:
print(f"6) Días restantes: {diferencia.days}")
print(f"6) Segundos restantes (sobrantes del día): {diferencia.seconds}")


# ----------------------------------------------------------
# 7) CALCULAR EDAD (FORMA CORRECTA)
# ----------------------------------------------------------
# No alcanza con: año_actual - año_nacimiento
# Porque si todavía NO cumpliste este año, te suma 1 de más.
fecha_nacimiento = datetime(1978, 11, 27)

edad = ano - fecha_nacimiento.year

# Si todavía no llegó tu cumpleaños este año, restamos 1
# (mes, día) compara tu cumpleaños con la fecha actual
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print(f"7) Mi edad es: {edad}")


# ----------------------------------------------------------
# 8) PARSEAR (CONVERTIR) STRING A FECHA (strptime)  ✅ MUY IMPORTANTE
# ----------------------------------------------------------
# strptime convierte string -> datetime
TEXTO_FECHA = "27/11/1978 15:30:00"
fecha_parseada = datetime.strptime(TEXTO_FECHA, "%d/%m/%Y %H:%M:%S")
print(f"8) Fecha parseada desde texto: {fecha_parseada}")

# En muchos sistemas 'es_ES.UTF-8' puede NO estar instalado.
# Por eso hacemos try/except y probamos alternativas típicas.

locales_posibles = [
    "es_ES.UTF-8",   # Linux común
    "es_ES",         # algunos Linux
    "Spanish_Spain.1252",  # Windows común
    "es_AR.UTF-8",   # a veces en Argentina
    "es_AR"          # alternativa
]

LOCAL_COFIGURABLE = False

for loc in locales_posibles:
    try:
        locale.setlocale(locale.LC_TIME, loc)
        LOCAL_COFIGURABLE = True
        break
    except locale.Error:
        pass

if LOCAL_COFIGURABLE:
    # %A = nombre del día (lunes, martes...)
    # %B = nombre del mes (enero, febrero...)
    fecha_formateada_es = fecha_actual.strftime("%A, %d de %B de %Y")
    print(f"9) Fecha en español: {fecha_formateada_es}")
else:
    print("9) No se pudo configurar locale en español en este sistema.")


# ----------------------------------------------------------
# 10) EXTRA ÚTIL: TIMESTAMP (segundos desde 1970-01-01)
# ----------------------------------------------------------
timestamp = fecha_actual.timestamp()
print(f"10) Timestamp actual: {timestamp}")
