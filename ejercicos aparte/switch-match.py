# #Crea un programa que use match para interpretar una calificación del 1 al 5:
# 1 → Muy deficiente  
# 2 → Insuficiente  
# 3 → Aceptable  
# 4 → Notable  
# 5 → Excelente
def interpretar_calificacion(calificacion):
    match calificacion:
        case 1:
            return "Muy deficiente"
        case 2:
            return "Insuficiente"
        case 3:
            return "Aceptable"
        case 4:
            return "Notable"
        case 5:
            return "Excelente"
        case _:
            return "Calificación no válida"
    
try:
    calificacion = int(input("Introduce una calificación del 1 al 5: "))
    resultado = interpretar_calificacion(calificacion)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")