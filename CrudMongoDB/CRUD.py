import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
#crear bd
db = cliente['ventas']
#crear coleccion
coleccion = db['articulos']
#isnertar datos
articulo1={"Nombre":"camiseta","precio":15.99,"stock":50}
articulo2={"Nombre":"pantalon","precio":39.99,"stock":20}
articulo3={"Nombre":"zapatos","precio":59.99,"stock":15}
articulo4={"Nombre":"gorra","precio":9.99,"stock":100}
articulo5={"Nombre":"chaqueta","precio":79.99,"stock":10}
articulo6={"Nombre":"calcetines","precio":5.99,"stock":200}
#insertar un documento
#coleccion.insert_one(articulo1)

#insertar varios documentos
articulos = [articulo1,articulo2,articulo3,articulo4,articulo5,articulo6]
coleccion.insert_many(articulos)
#listado
colecciones = db.list_collection_names()
print("colecciones en la base de datos")
for col in colecciones:
    print(col)

#listado de documentos
documentos = coleccion.find()
print("\nDocumentos en la coleccion articulos:")
for doc in documentos:
    print(doc)  

#edicion,modificación y borrado
#actualizar un documento
filtro={"Nombre":"camiseta"}
nuevo_valor={"$set":{"stock":45}}
coleccion.update_one(filtro,nuevo_valor)
#eliminar un documento
filtro={"Nombre":"pantalon"}
coleccion.delete_one(filtro)
