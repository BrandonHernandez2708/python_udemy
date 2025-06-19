#Crear un script que indique si has terminado tu jornada laboral, 
# por ejemplo que compruebe si son las 19.30, 
# en caso contrario indicar cuanto tiempo queda. Hacer uso del modulo datetime, para comprobar la hora.
from datetime import datetime
hora_actual = datetime.now().time()
hora_fin = datetime.strptime("19:30", "%H:%M").time()
if hora_actual >= hora_fin:
    print("Has terminado tu jornada laboral.")
else:
    tiempo_restante = datetime.combine(datetime.today(), hora_fin) - datetime.combine(datetime.today(), hora_actual)
    print(f"te queda {tiempo_restante} para terminar tu jornada laboral.")
