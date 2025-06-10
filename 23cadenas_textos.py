cadena ="EjEmplO de cAdeNa dE tExtO"
cadena= cadena.lower()
print(f"la cadena en minusculas es :{cadena}")
cadena = cadena.upper()
print(f"la cadena en mayusculas es :{cadena}")
cadena2="capital"
cadena2 = cadena2.capitalize()
print(f"la cadena capitalizada es :{cadena2}")
cadena3="titulo"
cadena3 = cadena3.title()
print(f"la cadena en titulo es :{cadena3}")
cadena ="EjEmplO de cAdeNa dE tExtO"
cadena=cadena.swapcase()
print(f"la cadena con mayusculas y minusculas intercambiadas es :{cadena}")
cadenam="MAYUSCULAS"
cadena_mayusculas = cadenam.isupper()
print(f"la cadena {cadenam} es mayusculas :{cadena_mayusculas}")
cadenan="123456789"
es_numerica = cadenan.isnumeric()
print(f"la cadena {cadenan} es numerica :{es_numerica}")
cadenan="3r#" 
cadenan=cadenan.isnumeric()
print(f"la cadena {cadenan} es numerica :{cadenan}")
cadenat="Titulo 1 "
cadenat = cadenat.istitle()
print(f"la cadena {cadenat} es titulo :{cadenat}")
cadenat="esto no es un titulo"
cadenat = cadenat.istitle()
print(f"la cadena {cadenat} es titulo :{cadenat}")
