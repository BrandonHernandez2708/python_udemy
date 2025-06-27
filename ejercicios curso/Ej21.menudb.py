import alumnosdb as db
def menu():
   print("""
         1. Insertar alumno
         2. Mostrar alumnos
         3. Actualizar alumno
         4. Borrar alumno)
         5. Salir
         """)
   print("*"*48)
   opcion=int(input())
   return opcion
while True:
   opcion=menu()
   if opcion == 1 :
      nombre = input("Introduce el nombre del alumno: ")
      notas = input("Introduce las notas del alumno: ")
      alumno = (nombre, notas)
      db.insertar(alumno)
   elif opcion == 2:
      db.mostrar_datos()
   elif opcion == 3:
        nombre = input("Introduce el nombre del alumno: ")
        notas = input("Introduce las notas del alumno: ")
        id = int(input("Introduce el ID del alumno a actualizar: "))
        db.actualizar(id, nombre, notas)     
   elif opcion == 4:
        id = int(input("Introduce el ID del alumno a borrar: "))
        db.borrar(id)
   elif opcion == 5:
      print("Saliendo del programa")
      break
   else:
      print("indica una opcion correcta \n")



