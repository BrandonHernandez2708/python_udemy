def ordenamient_burbuja(arr):
    n = len(arr)
    for i in  range(n): #repite reordenacion
        for j in range(0, n-i-1): #comprara y remplaza elementos adyacentes
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios = True
        if not intercambios: #si no hubo intercambios, la lista ya esta ordenada
            break
numeros=[5,3,8,4,2]
print("Lista original:", numeros)
ordenamient_burbuja(numeros)
print("Lista ordenada:", numeros)
