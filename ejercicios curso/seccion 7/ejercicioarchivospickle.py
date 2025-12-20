import pickle


#grabar 
with open('nombres.pickle', 'wb') as f:
    lista=["jose","M de mar","luisa","eva"]
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(lista, f, pickle.HIGHEST_PROTOCOL)
    print("fichero aguardado")

#leer
with open('nombres.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    lista = pickle.load(f)
    print(lista)
    print("fichero leido")