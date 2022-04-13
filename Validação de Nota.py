nota_valida = 0
nota = 0
media = 0
while nota_valida != 2:
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        media += nota / 2
        nota_valida += 1
    else:
        print('nota invalida')
print('media = {}'.format(media))




aux=med=0
while True:
    f=float(input())
    if f<0 or f>10:print("nota invalida")
    else:
        aux+=1
        med+=f
    if aux==2:break
print("media = %.2f"%(med/2))




t=int(input())
v=int(input())
litros=(v*t)/12
print("%.3f"%litros)