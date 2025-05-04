import calendar
#Escribe una funcion que indique si un año es bisiesto o no
def year_biciesto(year):
  dias_del_year=calendar.isleap(year)
  if (dias_del_year):
   print("el año es biciesto")
  else:
    print("el año No es biciesto")
year = 2020
year_biciesto(year)






