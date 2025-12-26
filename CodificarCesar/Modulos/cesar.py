dezplazamiento = 12
def codifica(texto):
  cifrado = ""
  if texto == texto.upper():
    lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
  else:
    lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    for car in texto:
      if car in lista:
        cifrado += lista[(lista.index(car) + dezplazamiento%(len(lista)))]
      else:
        cifrado += car

    return cifrado
  
def decodifica(texto):
  descifrado = ""
  if texto == texto.upper():
    lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
  else:
    lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    for car in texto:
      if car in lista:
        descifrado += lista[(lista.index(car) - dezplazamiento%(len(lista)))]
      else:
        descifrado += car

    return descifrado 
if __name__ == "__main__":
  cifrado=codifica("Hola")
  decodificado=decodifica(cifrado)