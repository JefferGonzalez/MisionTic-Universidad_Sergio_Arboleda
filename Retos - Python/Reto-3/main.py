n = input()
response = 'NO DISPONIBLE'
for i in range(int(n)):
    distancia_eje_suelo, bielas, sillin , manilar , costo  = input().split()
    if(int(distancia_eje_suelo) >= 240 and int(distancia_eje_suelo) <= 300):
        if(int(bielas) >= 160 and int(bielas) <= 180):
            if(int(sillin) >= 240 and int(sillin) <= 275):
                if(int(manilar) <= 50):
                    response = costo
print(response)