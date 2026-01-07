import fitz
def dividir_pdf(archivo_pdf,nombre_pagina1,nombre_pagina2):
    documento_pdf = fitz.open(archivo_pdf)
    if len(documento_pdf) < 2:
        print("El documento no se puede dividir")
        return
    pdf_pagina1 = fitz.open()
    pdf_pagina1.insert_pdf(documento_pdf, from_page=0, to_page=0)
    pdf_pagina1.save(nombre_pagina1)
    pdf_pagina2 = fitz.open()
    pdf_pagina2.insert_pdf(documento_pdf, from_page=1, to_page=1)
    pdf_pagina2.save(nombre_pagina2)

archivo_pdf="ejemplo.pdf"
nombre_pagina1="pagina_1.pdf"
nombre_pagina2="pagina_2.pdf"
dividir_pdf(archivo_pdf,nombre_pagina1,nombre_pagina2)